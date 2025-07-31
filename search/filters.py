from issues.models import Issue
import django_filters

class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['issue_name', 'contributor', 'is_issue_solved', 'tag', 'status']
        
        
'''
Author: Daly, J. (2019).
Title: "issue-tracker".
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''