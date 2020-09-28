from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You are at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking ar question %s," % question_id)


def results(request, question_id):
    response = "you're looking at the results of question %s," % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)