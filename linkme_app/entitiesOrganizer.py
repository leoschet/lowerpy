def get_valid_url(url):
	if (url.startswith('http://')):
		return url[7:]

	elif (url.startswith('https://')):
		return url[8:]

	else:
		return url


