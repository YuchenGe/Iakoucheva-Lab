# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
	template = get_template('index.html')
	output = template.render()
	return HttpResponse(output)

def table1(request):
	template = get_template('table1.html')
	output = template.render()
	return HttpResponse(output)

def table2(request):
	template = get_template('table2.html')
	output = template.render()
	return HttpResponse(output)

def table3(request):
	template = get_template('table3.html')
	output = template.render()
	return HttpResponse(output)

def table4(request):
	template = get_template('table4.html')
	output = template.render()
	return HttpResponse(output)