from django import forms

from .models import Comments


class CommentsForm(forms.ModelForm):
    """
    Comments form to be submitted
    """
    class Meta:
        """
        Fields needed
        """
        model = Comments
        fields = ['comments_article']

    comments_article = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control',
            'placeholder': 'Please add your comment here.'
        })
    )
