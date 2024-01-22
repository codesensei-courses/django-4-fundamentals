from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


# Please add: an about page that shows some text about yourself

def about(request):
    return HttpResponse("I'm Reindert and I make courses for Pluralsight")