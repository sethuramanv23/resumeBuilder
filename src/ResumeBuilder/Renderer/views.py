from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json

# Create your views here.
def index(request):
	user_name = request.GET['user']
	print user_name
	url_user = 'http://localhost:8000/api/v1/user/1/?format=json';
	response = urllib2.urlopen(url_user).read()
	user_json = json.loads(response)
	print user_json

	url = 'http://localhost:8000/api/v1/template/1/?format=json';
	response = urllib2.urlopen(url).read()
	template_json = json.loads(response)
	return HttpResponse(template_json['template_body'])
