from django.test import TestCase
from .models import Issue, Comment
from django.contrib.auth.models import User

#Tests for models
class TestModels(TestCase):
    
    def test_constructor_for_issue_model(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75, tag="TEST")
        issue.save()
        self.assertEqual(issue.issue_name, "Test Issue Name")
        self.assertEqual(issue.issue_description, "Test Issue Description")
        self.assertEqual(issue.contributor, user)
        self.assertIsNone(issue.date_issue_solved)
        self.assertEqual(issue.price, 75)
        self.assertEqual(issue.issue_type, "BUG")
        self.assertEqual(issue.status, "TODO")
        self.assertEqual(issue.tag, "TEST")
        self.assertEqual(issue.issue_upvotes, 0)
        self.assertFalse(issue.is_issue_solved)
        
    def test_constructor_for_comment_model(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue Name", issue_description="Test Issue Description", contributor=user, price=75)
        issue.save()
        comment = Comment(comment="Test Comment", contributor=user, issue=issue)
        comment.save()
        self.assertEqual(comment.comment, "Test Comment")
        self.assertEqual(comment.contributor, user)
        self.assertEqual(comment.issue, issue)
        
    def test_issue_as_a_string(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue String Name", issue_description="Test Issue Description", contributor=user, price=75)
        self.assertEqual("Test Issue String Name", str(issue))
        
    def test_comment_as_a_string(self):
        user = User()
        user.save()
        issue = Issue(issue_name="Test Issue String Name", issue_description="Test Issue Description", contributor=user, price=75)
        comment = Comment(comment="Test Comment String", contributor=user, issue=issue)
        self.assertEqual("Test Comment String", str(comment))
        


''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker"
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''
        
        
        
        