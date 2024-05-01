from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res = HttpResponse("""<html><body bgcolor="yellow"><center><h1>Welcome to shivani it </h1></center></body></html>""")
    return res

# Create your views here.
