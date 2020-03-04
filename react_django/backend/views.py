from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializers
# Create your views here.


class StudentCreateAPIView(APIView):
    serializer_class = StudentSerializers
    # queryset = Student.objects.all()

    def get(self, request):
        queryset = Student.objects.filter(user=request.user)
        serializers_data = StudentSerializers(queryset, many=True)
        return Response(serializers_data.data)

    def post(self, request):
        print(request.user.id)
        serializer = StudentSerializers(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = StudentSerializers

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # def put(self, request):
    #     pass
