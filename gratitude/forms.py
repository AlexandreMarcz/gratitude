from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, label='Nome')
    email = forms.EmailField()
    to = forms.EmailField(label = 'Para')
    comments = forms.CharField(required=False, widget=forms.Textarea, label = 'Comentário')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {'name':'Nome', 'email':'Email','body':'Texto'}
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Procure por:')


            

