# from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from project.apps.user import models as user_models
from project.apps.user.messages import Messages
from project.apps.user import serializers

# Create your views here.

class CustomerEmailRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.EmailAuthSerializer
    model = user_models.Profile

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Messages.CUSTOMER_EMAIL_SIGNUP, status=status.HTTP_200_OK)
