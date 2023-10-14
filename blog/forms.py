from django import forms
from .models import Comment
# Write Code here
class CommentForm(forms.ModelForm):
    class Mete:
        model = Comment
        fields = '__all__'