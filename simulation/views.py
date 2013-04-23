# Create your views here

from django.shortcuts import render_to_response

from models import buildingSim
from models import simResults

def home(request):
	return render_to_response('index.html')

