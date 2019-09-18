from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("###### You are in the index file. ######")

def hello(request):
    return HttpResponse("::::: This is another message :::::")

def list_Clients(request):
    return HttpResponse("Here you must list the clients in DB.")
