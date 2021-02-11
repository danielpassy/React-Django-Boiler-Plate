from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view

import logging

logger = logging.getLogger(__file__)


def logging(request):
    """
    Logger view
    """
    logger.debug("This logs a debug message.")
    return HttpResponse("this worked")


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    """ Retrieve a CSFR token to be used on FORM in the frontend"""

    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, format=None):
        return Response({"success": "CSRF cookie set"})

