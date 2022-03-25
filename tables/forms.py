from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """" doc string """
    class Meta:
        """" doc string """
        model = Comment
        fields = ('body',)
