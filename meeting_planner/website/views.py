from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})


def about(request):
    return HttpResponse("I'm  Reindert and I make courses for Pluralsight")