from django import forms
from .models import Comment
# Write Code here
class CommentForm(forms.ModelForm):
    class Meta:  # It should be "class Meta", not "class Mete"
        model = Comment
        fields = ('name', 'author', 'comment')
        widgets = {
            'blog': forms.HiddenInput(),
            'author': forms.HiddenInput()
        }
