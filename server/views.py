from django.http import HttpResponse
import django_rq
import time

def printMessage(header, message):
    print(header)
    print(message)

def index(request):
    django_rq.enqueue(printMessage, "This is the header", message="Test message")
    return HttpResponse("Hello, you are at the server index")
