from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def empresas_lista(request):
    return render(request, "empresas/empresas_lista.html")   

