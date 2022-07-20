from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required