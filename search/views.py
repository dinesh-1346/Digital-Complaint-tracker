from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from issues.models import Issue
from django.db.models import Count, Q
from .filters import IssueFilter

# Create your views here.
@login_required()
def search(request):
    """
    This view will take the user to the search page. It will also pass a filter
    object to the search page.
    """
    f = IssueFilter(request.GET, queryset=Issue.objects.all())
    return render(request, "search.html", {'filter': f})




'''
Author: Daly, J. (2019).
Title: "issue-tracker".
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''