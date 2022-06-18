from django.shortcuts import render

# Create your views here.
def empresas_lista(request):
    return render(request, "empresas/empresas_lista.html")   

