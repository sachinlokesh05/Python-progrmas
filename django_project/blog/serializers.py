from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']


class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class NotesSerializer(serializers.ModelSerializer):
    label = LabelSerializer(many=True, read_only=True)
    collaborators = CollaboratorsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'label', 'url', 'is_archive',
                  'collaborators', 'post_image', 'reminder', 'color']


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'note']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'note', 'label', 'url', 'is_archive', 'collaborators',
                  "is_copied", 'checkbox', 'is_pined', 'is_trashed', 'color', 'reminder']
