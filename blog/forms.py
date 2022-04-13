from django import forms

from .models import Comments, Post


class PostForm(forms.ModelForm):
    """
    Comments form to be submitted
    """
    class Meta:
        """
        Fields needed
        """
        model = Post
        fields = ['slug', 'title', 'intro', 'post_article']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'slug': 'Post-number -> Post-1',
            'title': '100 characteres',
            'intro': '100 characteres',
            'post_article': 'Text Body',
        }

        for field in self.fields:
            if field:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-purple \
                 rounded-4 profile-form-input'


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
