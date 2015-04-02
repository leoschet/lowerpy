from django.shortcuts import render


def index(request):
	return render(request, "index.html", locals())

def register(request):
	if request.method == 'POST' and request.POST.__contains__('source') and request.POST.__contains__('target')
		sourceUrl = request.POST.get('source')
		target = request.POST.get('target')

		# pega todos os links
		# links = Link.objects.all()

		source = Source()

		source.url = sourceUrl

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

def redirect(request, id):
	# get all links
	links = Link.objects.all()
	# get source options
	options = Source.objects.all()
	# current url
	currentUrl = request.get_full_path()

	# redirect
	for link in links:
		if link.source.url == currentUrl
			return render(request, link.urlTarget, locals())

	return redirect()