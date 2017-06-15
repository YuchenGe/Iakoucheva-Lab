# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
	template = get_template('MasterFile/Iakoucheva Lab.html')
	output = template.render()
	return HttpResponse(output)