from django import forms
from .models import Comment, Dessert


class CommentForm(forms.ModelForm):
    """" doc string """
    class Meta:
        """" doc string """
        model = Comment
        fields = ('body',)
class DessertForm(forms.ModelForm):
    """ doc string """
    class Meta:
        """" doc string """
        model = Dessert
        fields = ('title',)
