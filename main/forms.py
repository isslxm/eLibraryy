from django import forms
from .models import Tag
class BookSearchForm(forms.Form):
    search = forms.CharField(max_length=50,
                             required=False,
                             label='Search',
                             widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'tag-checkbox'}),
        required=False
    )

class VideoSearchForm(forms.Form):
    search = forms.CharField(max_length=50,
                             required=False,
                             label='Search',
                             widget=forms.TextInput(attrs={'autocomplete': 'off'}))