from .chatbot import chatbot
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")


def get_bot_response(request):
    userText = request.GET.get('msg')
    reply = chatbot.get_response(userText)
    return HttpResponse(reply)
