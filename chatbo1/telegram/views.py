from django.shortcuts import render
from django.http import HttpResponse

from mybot import sendGIF
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

from credentials import API_KEY
URL = 'https://api.telegram.org/bot'
def index(request):
	return HttpResponse("hello")

@csrf_exempt
def hook(request):
	
	data = json.loads(request.body)
	message= data['message']
	msg = message['text']
	chat_id = message['chat']['id']
	sendGIF(str(chat_id),msg)

	return HttpResponse('')