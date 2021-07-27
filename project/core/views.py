# Apps Dependency Here
# Python standard Library dependency here
import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from project.core.renderers import ApiRenderer


# Function based views for home page, 404 page, 500 page and other HTTP error code corresponding page


def index(request):
    """returns the template for home page.
    :param request:
    :return:
    """
    return render(template_name='home_page.html', request=request)


def handler404(request, exception):
    """Return json error response with message.
    :param request:
    :param exception:
    :return:
    """
    response_data = ApiRenderer.format_response(status.HTTP_404_NOT_FOUND, status.is_informational(status.HTTP_404_NOT_FOUND))
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def handler500(request):
    """Return json error response with message.
    :param request:
    :return:
    """
    response_data = ApiRenderer.format_response(status.HTTP_500_INTERNAL_SERVER_ERROR, status.is_informational(status.HTTP_500_INTERNAL_SERVER_ERROR))
    return HttpResponse(json.dumps(response_data), content_type="application/json")
