
import json

import requests
from oauthlib.oauth2 import BackendApplicationClient
from datetime import datetime, timedelta
from functools import wraps
from django.utils import timezone
import django
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.utils import timezone as tz
from django.shortcuts import get_object_or_404, render
import redis
import pdb
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fundoo.settings import PORT, DB, TWITTER_PAGE, logging, SOCIAL_AUTH_GITHUB_KEY, \
    SOCIAL_AUTH_GITHUB_SECRET
from note.documents import NotesDocument
from note.serialized import NotesSerializer, UpdateSerializer, ShareSerializer, LabelSerializer, \
    NotesDocumentSerializer  # ArchiveSerializer
from lib.amazones3 import AmazoneS3
from note.decorators import login_decorator, label_coll_validator_put  # , label_coll_validator_post
from lib.redis import red
# import logging
from .models import Notes, Label
from pymitter import EventEmitter

ee = EventEmitter()
s3 = AmazoneS3()

@method_decorator(login_decorator, name='dispatch')
class NoteCreate(GenericAPIView):
    """
        Summary:
        --------
            Note class will let authorized user to create and get notes.

        Methods:
        --------
            get: User will get all the notes.
            post: User will able to create new note.

    """
    serializer_class = NotesSerializer

    def get(self, request):
        """
           Summary:
           --------
                All the notes will be fetched for the user.

           Exception:
           ----------
               PageNotAnInteger: object
               EmptyPage: object

           Returns:
           --------
               Html_page: pagination.html    Jinja-arg=['notes']
        """
        notes_list = Notes.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(notes_list, 1)
        user = request.user
        try:
            notes = paginator.page(page)
        except PageNotAnInteger:
            logger.warning("got %s error for getting note for user %s", str(PageNotAnInteger), user.username)
            notes = paginator.page(1)
        except EmptyPage:
            logger.warning("got %s error for getting note for user %s", EmptyPage, user)
            notes = paginator.page(paginator.num_pages)
        logger.info("all the notes are rendered to html page for user %s", user)
        return render(request, 'user/pagination.html', {'notes': notes}, status=200)

    # parser_classes = (FormParser,FileUploadParser)
    @staticmethod
    def post(request):
        """
             Summary:
             --------
                 New note will be create by the User.

             Exception:
             ----------
                 KeyError: object

             Returns:
             --------
                 response: SMD format of note create message or with error message
        """

        user = request.user
        try:
            # data is taken from user
            # pdb.set_trace()
            data = request.data
            if len(data) == 0:
                raise KeyError
            user = request.user
            collaborator_list = []  # empty coll  list is formed where data is input is converted to id
            try:
                # for loop is used for the getting label input and coll input ids
                data["label"] = [Label.objects.filter(user_id=user.id, name=name).values()[0]['id'] for name in
                                 data["label"]]
            except KeyError:
                logger.debug('label was not added by the user %s', user)
                pass
            try:
                collaborator = data['collaborators']
                # for loop is used for the getting label input and coll input ids
                for email in collaborator:
                    email_id = User.objects.filter(email=email)
                    user_id = email_id.values()[0]['id']
                    collaborator_list.append(user_id)
                data['collaborators'] = collaborator_list
                print(data['collaborators'])
            except KeyError:
                logger.debug('collaborator was not added by the user %s', user)
                pass
            serializer = NotesSerializer(data=data, partial=True)
            if serializer.is_valid():
                note_create = serializer.save(user_id=user.id)
                response = {'success': True, 'message': "note created", 'data': []}
                if serializer.data['is_archive']:
                    red.hmset(str(user.id) + "is_archive",
                              {note_create.id: str(json.dumps(serializer.data))})  # created note is cached in redis
                    logger.info("note is created for %s with note id as %s", user, note_create.id)
                    return HttpResponse(json.dumps(response, indent=2), status=201)
                else:
                    if serializer.data['reminder']:
                        red.hmset("reminder",
                                  {note_create.id: str(json.dumps({"email": user.email, "user": str(user),
                                                                   "note_id": note_create.id,
                                                                   "reminder": serializer.data["reminder"]}))})
                    red.hmset(str(user.id) + "note",
                              {note_create.id: str(json.dumps(serializer.data))})

                    logger.info("note is created for %s with note data as %s", user, note_create.__repr__())
                    return HttpResponse(json.dumps(response, indent=2), status=201)
            logger.error(" %s for  %s", user, serializer.errors)
            response = {'success': False, 'message': "note was not created", 'data': []}
            return HttpResponse(json.dumps(response, indent=2), status=400)
        except KeyError as e:
            print(e)
            logger.error("got %s error for creating note as no data was provided for user %s", str(e), user)
            response = {'success': False, 'message': "one of the field is empty ", 'data': []}
            return Response(response, status=400)
        except Exception as e:
            print(e)
            logger.error("got %s error for creating note for user %s", str(e), user)
            response = {'success': False, 'message': "something went wrong", 'data': []}
            return Response(response, status=400)



@method_decorator(login_decorator, name='dispatch')
class NoteUpdate(GenericAPIView):
    """
        Summary:
        --------
             Note update class will let authorized user to update and delete note.
        Methods:
        --------
            get: User will get particular note which he want.
            put: User will able to update existing note.
            delete: User will able to delete  note.
    """
    serializer_class = UpdateSerializer

    @staticmethod
    def get(request, note_id):
        """
              Summary:
              --------
                  Note will be fetched by the User.
              Exception:
              ----------
                  Notes.DoesNotExist: object
              Returns:
              --------
                  response: will return all the note data or will return
                            error msg if note id does not exist
        """
        try:
            # pdb.set_trace()
            redis_data = red.hmget(str(request.user.id) + "note", str(note_id))
            user = request.user
            if redis_data == [None]:
                note = Notes.objects.filter(id=note_id)
                serialized_data = NotesSerializer(note, many=True)
                logger.info("note was fetched from database for user %s", user)
                return HttpResponse(json.dumps(serialized_data.data, indent=1), status=200)

            logger.info("note was fetched form redis for user %s", user)
            return HttpResponse(redis_data, status=200)
        except Notes.DoesNotExist:
            logger.error("Note id doesnt exists, node_id:", note_id)
            response = {'success': False, 'message': "note does not exists", 'data': []}
            return Response(response, status=404)
        except Exception as e:
            logger.error("Unknown error while updating the note, %s %s:", note_id, str(e))
            response = {'success': False, 'message': str(e), 'data': []}
            return Response(response, status=404)

    @staticmethod
    @label_coll_validator_put
    def put(request, note_id):
        """
          Summary:
          --------
              Note will be updated by the User.
          Exception:
          ----------
              Keyerror: object
          Returns:
          --------
              response: will return updated note or will return error with smd format
        """
        user = request.user
        try:
            # pdb.set_trace()
            # data is fetched from user
            instance = Notes.objects.get(id=note_id)
            data = request.data
            if len(data) == 0:
                raise KeyError
            collaborator_list = []  # empty coll  list is formed where data is input is converted to id
            try:
                label = data["label"]
                data['label'] = [Label.objects.get(name=name, user_id=request.user.id).id for name in label]
            except KeyError:
                logger.debug('label was not added by the user %s', user)
                pass
            try:
                collaborator = data['collaborators']
                # for loop is used for the getting label input and coll input ids
                for email in collaborator:
                    emails = User.objects.filter(email=email)
                    user_id = emails.values()[0]['id']
                    collaborator_list.append(user_id)
                data['collaborators'] = collaborator_list
            except KeyError:
                logger.debug('collaborators was not added by the user %s', user)
                pass
            serializer = UpdateSerializer(instance, data=data, partial=True)
            # here serialized data checked for validation and saved
            if serializer.is_valid():
                note_create = serializer.save()
                response = {'success': True, 'message': "note updated", 'data': [serializer.data]}
                print(serializer.data)
                # pdb.set_trace()
                if serializer.data['is_archive']:
                    red.hmset(str(user.id) + "is_archive",
                              {note_create.id: str(json.dumps(serializer.data))})
                    logger.info("note was updated with note id :%s for user :%s ", note_id, user)
                    return HttpResponse(json.dumps(response, indent=2), status=200)
                elif serializer.data['is_trashed']:
                    red.hmset(str(user.id) + "is_trashed",
                              {note_create.id: str(json.dumps(serializer.data))})
                    logger.info("note was updated with note id :%s for user :%s ", note_id, user)
                    return HttpResponse(json.dumps(response, indent=2), status=200)
                else:
                    if serializer.data['reminder']:
                        red.hmset("reminder",
                                  {note_create.id: str(json.dumps({"email": user.email, "user": str(user),
                                                                   "note_id": note_create.id,
                                                                   "reminder": serializer.data["reminder"]}))})

                    red.hmset(str(user.id) + "note",
                              {note_create.id: str(json.dumps(serializer.data))})
                    logger.info("note was updated with note id :%s for user :%s ", note_id, user)
                    return HttpResponse(json.dumps(response, indent=2), status=200)
            logger.error("note was updated with note id :%s for user :%s ", note_id, user)
            response = {'success': False, 'message': "note was not created", 'data': []}
            return HttpResponse(json.dumps(response, indent=2), status=400)
        except KeyError as e:
            print(e)
            logger.error("no data was provided from user %s to update", str(e), user)
            response = {'success': False, 'message': "note already upto data ", 'data': []}
            return Response(response, status=400)
        except Exception as e:
            logger.error("got error :%s for user :%s while updating note id :%s", str(e), user, note_id)
            response = {'success': False, 'message': str(e), 'data': []}
            return Response(response, status=404)

    def delete(self, request, note_id, *args, **kwargs):
        """
          Summary:
          --------
              Note will be deleted by the User.
          Exception:
          ----------
              Keyerror: object
          Returns:
          --------
              response: will return SMD format of deleted note or with error message
        """

        smd = {'success': False, 'message': 'not a vaild note id ', 'data': []}
        user = request.user
        try:
            # pdb.set_trace()
            note = Notes.objects.get(id=note_id)
            note.is_trashed = True  # is_deleted, is_removed, is_trashed
            note.save()
            note_data = Notes.objects.filter(id=note_id)
            serialized_data = NotesSerializer(note_data, many=True)

            red.hmset(str(user.id) + "is_trashed",
                      {note.id: str(json.dumps(serialized_data.data))})
            red.hdel(str(user.id) + "note", note_id)
            logger.info("note with node_id :%s was trashed for user :%s", note_id, request.user)
            smd = {'success': True, 'message': 'note is deleted ', 'data': []}
            return HttpResponse(json.dumps(smd, indent=2), status=status.HTTP_201_CREATED)
        except KeyError:
            logger.info("note with node_id :%s was already deleted for user :%s", note_id, request.user)
            return HttpResponse(json.dumps(smd, indent=2), status=404)
        except Exception as e:
            logger.info("note with node_id :%s was already deleted for user :%s", note_id, request.user)
            response = {'success': False, 'message': str(e), 'data': []}
            return HttpResponse(json.dumps(response, indent=2), status=404)
