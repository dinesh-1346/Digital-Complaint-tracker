from django.conf.urls import url
from .views import progress_panel, get_issue_type_json, get_issue_status_json, get_bug_upvotes_json, get_feature_upvotes_json

urlpatterns = [
    url(r'^progress_panel/$', progress_panel, name='progress_panel'),
    url(r'^progress_panel/get_issue_type_json/$', get_issue_type_json, name='get_issue_type_json'),
    url(r'^progress_panel/get_issue_status_json/$', get_issue_status_json, name='get_issue_status_json'),
    url(r'^progress_panel/get_bug_upvotes_json/$', get_bug_upvotes_json, name='get_bug_upvotes_json'),
    url(r'^progress_panel/get_feature_upvotes_json/$', get_feature_upvotes_json, name='get_feature_upvotes_json'),
]