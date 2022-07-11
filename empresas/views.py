from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http.response import JsonResponse
from empresas.models import Empresa

@login_required
def empresas_lista(request):
    return render(request, "empresas/empresas_lista.html")