from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']



class SearchForm(forms.Form):
    query = forms.CharField(label='Qidirish', max_length=100)