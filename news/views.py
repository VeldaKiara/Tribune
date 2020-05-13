from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
#A view is a function that takes the request from a user,
#  processes it and returns a response to the user
def welcome(request):
    return HttpResponse('Welcome to the Daily Tribune')