from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)

        widgets = {
        'content': forms.Textarea(attrs={'class': 'form-control'})
        }
