# from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .tasks import create_random_user_accounts


class OnboardAPIView(generics.ListCreateAPIView):

    def post(self, request, *arg, **kwargs):
        create_random_user_accounts.delay(5)

        return Response({'msg:Get data'}, status=status.HTTP_200_OK)
