import os, tempfile, zipfile
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def gchami(request):
#    response = HttpResponse(content_type='application/force-download')
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="onie.bin"'
    response['X-Sendfile'] = smart_str('/home/gchami/onie.bin')
    return response
#    return HttpResponse("Hello, world. You're at gchami")

def onie(request):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    filename = 'onie.bin' # Select your file here.                                
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='application/octet-stream')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="onie-installer"'
    return response
