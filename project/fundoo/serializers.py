from django.contrib.auth.models import User
from rest_framework import serializers
from fundoo.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model: Registration
        fields = '__all__'

    def save(self):
        account = Registration(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password1 = self.validated_data['password'],
        password2 = self.validated_data['confirm_passowrd']
        if password1 != password2:
            raise serializers.ValidationError(
                {'password': 'password must match'})

        account.set_password(password1)
        account.save()
        return account


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: User
#         fieids: ['username', 'password', 'email']


# class LoginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model: User
#         fields: ['username', 'password']


# class ResetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: User
#         fields: '[password]'


# class EmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: User
#         fields:  ['email']
