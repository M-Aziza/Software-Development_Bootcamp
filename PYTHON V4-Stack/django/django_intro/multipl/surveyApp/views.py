from django.shortcuts import render, HttpResponse , redirect # add redirect to import statement


def root(request):
    return HttpResponse("placeholder to display all the surveys created")

def index(request):
    return HttpResponse("placeholder for users to add a new survey")
