from django.test import TestCase
from .models import Issue, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

#Tests for views
class LoggedInTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='user007', password='fake_pass')
        self.client.login(username='user007', password='fake_pass')

class TestViews(LoggedInTestCase):

    def test_get_landing_page_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "landing_page.html")
        
    def test_get_about_page_view(self):
        page = self.client.get("/issues/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about_page.html")
        
    def test_create_issue_form_view(self):
        page = self.client.get("/issues/create_issue/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_issue_form.html")
        
    def test_get_view_issue_page(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()

        page = self.client.get("/issues/{0}/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_issue.html")
        
    def test_get_view_issue_page_for_issue_that_does_not_exist(self):
        page = self.client.get("/issues/1/")
        self.assertEqual(page.status_code, 404)
        
    def test_get_edit_issue_page(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()

        page = self.client.get("/issues/{0}/edit_issue/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_issue.html")
        
    def test_get_edit_issue_page_for_issue_that_does_not_exist(self):
        page = self.client.get("/issues/1/edit_issue/")
        self.assertEqual(page.status_code, 404)
    
    def test_get_comment_form_page(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()
        page = self.client.get("/issues/{0}/comment/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "comment_form.html")

    def test_get_comment_edit_form_page(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()
        comment = Comment(comment="Test Comment", contributor=user, issue=issue)
        comment.save()

        page = self.client.get("/issues/{0}/edit_comment/".format(comment.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "comment_edit_form.html")
        
    def test_get_edit_comment_page_for_comment_that_does_not_exist(self):
        page = self.client.get("/issues/1/edit_comment/")
        self.assertEqual(page.status_code, 404)
        
    def test_get_my_contributions_page_view(self):
        user = User()
        user.save()
        """
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()
        comment = Comment(comment="Test Comment", contributor=user, issue=issue)
        comment.save()
        """
        
        page = self.client.get("/issues/my_contributions/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "my_contributions.html")
        
        
''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker"
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''
        
        