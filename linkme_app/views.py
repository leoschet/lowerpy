from django.views.generic.base import RedirectView
from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from models import *
from entitiesOrganizer import *
from linkme_app.forms import *

def index(request):
	print('index')
	msg = 'welcome'
	form = LinkForm()
	return render(request, "index.html", locals())

def register(request):
	print('register')
	if request.method == 'POST' and request.POST.__contains__('source') and request.POST.__contains__('target'):
		print('register if')
		source = request.POST.get('source')
		targetUrl = request.POST.get('target')
		targetUrl = get_valid_url(targetUrl)
		print(targetUrl)
		try:
			print('register if try')
			target = get_object_or_404(Target, url=targetUrl)
			#target ja criado

		except Http404:
			print('register if try-except')
			target = Target()
			target.url = targetUrl
			target.save()

		try:
			print('register if try2')
			link = get_object_or_404(Link, source=source)
			return backToIndex_Erro(request)
			

		except Http404:
			print('register if try-except2')
			link = Link()
			link.source = source
			link.target = target
			link.save()

		return backToIndex(request, source)

	else:
		print('register else')
		return backToIndex_NoField(request)

def backToIndex(request, source):
	msg = "true"
	source = source
	form = LinkForm()
	return render(request, "index.html", locals())

def backToIndex_Erro(request):
	msg = "false"
	form = LinkForm()
	return render(request, "index.html", locals())
	
def backToIndex_NoField(request):
	msg = "noField"
	form = LinkForm()
	return render(request, "index.html", locals())

def backToIndex_Unregistered(request):
	msg = 'urlNotRegistered'
	form = LinkForm()
	return render(request, "index.html", locals())

def redirectTo(request, source):
	print('redirectTo')
	try:
		link = get_object_or_404(Link, source=source)
		return redirect('http://'+link.target.url)

	except Http404:
		print('nao achou')
		return backToIndex_Unregistered(request)