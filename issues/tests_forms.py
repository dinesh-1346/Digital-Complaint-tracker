from django.test import TestCase
from .forms import IssueForm, CommentForm

# Create your tests here.
""" -- Used in Testing.
class TestDjango(TestCase):
    
    def test_is_this_thing_on(self):
        self.assertEqual(1, 0)
"""
class TestForms(TestCase):
    
    def test_issue_form_can_submit_with_required_fields(self):
        form = IssueForm({'issue_name': 'Test Issue', 'issue_description': 'Test Description', 'issue_type': 'BUG'})
        self.assertTrue(form.is_valid())
        
    def test_issue_form_error_message_for_missing_required_fields(self):
        form = IssueForm({'issue_name': ''}, {'issue_description': ''}, {'issue_type': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['issue_name'], [u'This field is required.'])
        self.assertEqual(form.errors['issue_description'], [u'This field is required.'])
        self.assertEqual(form.errors['issue_type'], [u'This field is required.'])
        
    def test_comment_form_can_submit_with_required_field(self):
        form = CommentForm({'comment': 'Test Comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_error_message_for_missing_required_field(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
        
''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker"
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''