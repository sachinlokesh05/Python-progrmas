from django.shortcuts import render
from rest_framework.decorators import api_view
from fundoo.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def registration_view(request):
    if request.me thod == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response']= "succesfully registred"
            data['email'] = account.email
            data['username'] = account.user_name
        else:
            data =  serializer.errors
        return Response(data)
    
    # # user input is checked
    #     if firstname == "" or username == "" or email == "" or password == "":
    #         messages.info(request, "one of the above field is empty")
    #         return redirect('/registration')

    #     elif
