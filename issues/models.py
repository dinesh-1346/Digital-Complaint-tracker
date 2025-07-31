from django.db import models
from django.utils import timezone
from .utils import ChoiceEnum
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    """
    The model for a single issue.
    """
    issue_name = models.CharField(max_length=120)
    issue_description = models.TextField()
    date_issue_created = models.DateTimeField(auto_now_add=True)
    contributor = models.ForeignKey(User,related_name='contributor', on_delete=models.CASCADE)
    date_issue_updated = models.DateTimeField(auto_now=True)
    is_issue_solved = models.BooleanField(default=False)
    date_issue_solved = models.DateTimeField(blank=True, null=True)
    issue_upvotes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    issue_image = models.ImageField(upload_to='issue_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Issue_Types(ChoiceEnum):
        BUG = 'bug'
        FEATURE = 'feature'

    class Statuses(ChoiceEnum):
        TODO = 'To Do'
        IN_PROGRESS = 'In Progress'
        DONE = 'Done'

    issue_type = models.CharField(max_length=9, choices=Issue_Types.choices(), default='BUG')
    status = models.CharField(max_length=12, choices=Statuses.choices(), default='TODO')
    


    def __unicode__(self):
        return self.issue_name

    def __str__(self):
        return self.issue_name
        


class Comment(models.Model):
        """
        The class model for a single Comment
        """
        comment = models.CharField(max_length=200)
        date_comment_created = models.DateTimeField(auto_now_add=True)
        date_comment_updated = models.DateTimeField(auto_now=True)
        contributor = models.ForeignKey(User, related_name='comment_contributor', on_delete=models.CASCADE)
        issue = models.ForeignKey(Issue, related_name='comment_issue', on_delete=models.CASCADE)

        def __unicode__(self):
            return self.comment

        def __str__(self):
            return self.comment
            

''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker".
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''