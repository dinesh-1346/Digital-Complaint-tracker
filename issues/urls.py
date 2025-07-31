from django.conf.urls import url, include
from .views import landing_page, create_issue, view_issue, edit_issue, upvote_issue, delete_issue, create_comment, edit_comment, delete_comment, about_page, my_contributions

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^create_issue/$', create_issue, name='create_issue'),
    url(r'^(?P<pk>\d+)/$', view_issue, name='view_issue'),
    url(r'^(?P<pk>\d+)/edit_issue/$', edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_issue, name='upvote_issue'),
    url(r'^(?P<pk>\d+)/delete/$', delete_issue, name='delete_issue'),
    url(r'^(?P<pk>\d+)/comment/$', create_comment, name='create_comment'),
    url(r'^(?P<pk>\d+)/edit_comment/$', edit_comment, name='edit_comment'),
    url(r'^(?P<pk>\d+)/delete_comment/$', delete_comment, name='delete_comment'),
    url(r'^about/$', about_page, name='about_page'),
    url(r'^my_contributions/$', my_contributions, name='my_contributions'),
]