from django.shortcuts import render
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from .utility import check_sequence
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
