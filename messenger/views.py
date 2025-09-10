from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

# Create your views here.
@login_required
def inbox(request):
    msgs = Message.objects.filter(recipient=request.user)
    return render(request, "messenger/inbox.html", {"messages_list": msgs})

@login_required
def compose(request):
    form = MessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        msg = form.save(commit=False)
        msg.sender = request.user
        msg.save()
        messages.success(request, "Mensaje enviado.")
        return redirect("messenger_inbox")
    return render(request, "messenger/compose.html", {"form": form})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk, recipient=request.user)
    if not msg.read:
        msg.read = True
        msg.save(update_fields=["read"])
    return render(request, "messenger/detail.html", {"msg": msg})
