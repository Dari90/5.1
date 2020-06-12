from django import forms
from p_library.models import Book, Friend
from django.forms import formset_factory 

class FriendForm(forms.ModelForm):
	class Meta:
		model = Friend
		fields = '__all__'	