from django import forms
from .models import Issue, Comment


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('issue_name', 'issue_description', 'issue_image', 'tag', 'issue_type')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)