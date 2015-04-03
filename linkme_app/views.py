from django.views.generic.base import RedirectView
from django.http import *
from django.shortcuts import render
from models import *
import urlparse


def index(request):
	return render(request, "index.html", locals())

def register(request):
	if request.method == 'POST' and request.POST.__contains__('source') and request.POST.__contains__('target'):
		source = request.POST.get('source')
		targetUrl = request.POST.get('target')

		# pega todos os links
		# links = Link.objects.all()

		target = Target()

		target.url = Url

		link = Link()

		link.source = source
		link.target = target
		link.save()

		return redirect(backToIndex)
	return redirect(backToIndex_Erro)

def backToIndex(request):
	success = "true"
	return redirect(index)

def backToIndex_Erro(request):
	success = "false"
	return redirect(index)

def redirect(request, source):
	# get link object
	link = Link.objects.get(source = source)

	# get path and generate url
	target = link.target

	# redirect
	return render(request, "redirect.html", locals())