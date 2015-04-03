from django import forms
from linkme_app.models import *

class LinkForm(forms.Form):
	source = forms.CharField(max_length = 30)
	source.widget.attrs['class'] = 'input-container'
	source.widget.attrs['style'] = 'width: 68px;'
	source.widget.attrs['placeholder'] = '<base_dir>'
	source.widget.attrs['id'] = 'source'

	target = forms.CharField(max_length = 30)
	target.widget.attrs['class'] = 'input-container'
	target.widget.attrs['style'] = 'width: 74px;'
	target.widget.attrs['placeholder'] = '<target_url>'
	target.widget.attrs['id'] = 'target'