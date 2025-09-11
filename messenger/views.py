from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def inbox(request):
    # Más adelante podés pasar mensajes reales en el contexto
    return render(request, "messenger/inbox.html")
