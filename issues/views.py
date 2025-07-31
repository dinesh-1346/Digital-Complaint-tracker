from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Issue, Comment
from .forms import IssueForm, CommentForm

# Create your views here.
def landing_page(request):
    """
    Create a view that will render the landing page to the user.
    """
    all_issues = Issue.objects.all().order_by('-date_issue_created')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(all_issues, 2)
    
    try:
        issues = paginator.page(page)
        
    except PageNotAnInteger:
        
        issues = paginator.page(1)
        
    except EmptyPage:
        
        issues = paginator.page(paginator.num_pages)
    
    return render(request, "landing_page.html", {'issues': issues})
    
def about_page(request):
    """
    This view will render the about page to the user.
    """
    return render(request, "about_page.html")
    
@login_required()
def create_issue(request):
    """
    Implement the view that allows a user to report a new bug or suggest a new feature.
    """
    if request.method == "POST":
        create_issue_form = IssueForm(request.POST, request.FILES)
        if create_issue_form.is_valid():
            
            create_issue_form.instance.contributor = request.user
            if create_issue_form.instance.issue_type == 'FEATURE':
                create_issue_form.instance.price = 75
            else:
                create_issue_form.instance.price = 0
            issue = create_issue_form.save()
            messages.success(request, 'You have successfully contributed a new issue to the site.')
            
            return redirect(view_issue, issue.pk)
    else:
        create_issue_form = IssueForm()
    return render(request, 'create_issue_form.html', {'create_issue_form': create_issue_form})
    
    
@login_required()
def view_issue(request, pk):
    """
    This view allows the user to view a single issue.
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.save()
    comments = Comment.objects.filter(issue=pk)
    len_of_comments = len(comments)

    return render(request, "view_issue.html", {'issue': issue, 'comments': comments, 'len_of_comments': len_of_comments})
    

@login_required()
def edit_issue(request, pk):
    """
    This view allows the contributor or staff member to edit a single issue.
    """
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    user = request.user
    
    if request.method == "POST":
        edit_issue_form = IssueForm(request.POST, request.FILES, instance=issue)
        if edit_issue_form.is_valid():

            edit_issue_form.instance.contributor = request.user
            if edit_issue_form.instance.issue_type == 'FEATURE':
                edit_issue_form.instance.price = 75
            else:
                edit_issue_form.instance.price = 0
            issue = edit_issue_form.save()
            messages.success(request, 'You have successfully made changes to this issue.')

            return redirect(view_issue, issue.pk)
    else:
        edit_issue_form = IssueForm(instance=issue)
        

    return render(request, "edit_issue.html", {'issue': issue, 'edit_issue_form': edit_issue_form})    
    

@login_required()
def upvote_issue(request, pk):
    """
    This view allows the user to upvote an issue of their choice.
    """
    issue = Issue.objects.get(pk=pk)
    issue.issue_upvotes += 1
    issue.save()
    messages.success(request, 'You have successfully upvoted this issue !!')
    return redirect('view_issue', pk)
    
@login_required()
def delete_issue(request, pk):
    """
    This view allows a staff member to delete a issue
    """
    issue_for_deletion = Issue.objects.get(pk=pk)
    issue_for_deletion.delete()
    messages.success(request, "You have successfully deleted this issue.")
    return redirect('index')
    
@login_required()
def create_comment(request, pk):
    """
    This view allows a user to comment on an issue.
    """
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.contributor = request.user
            comment_form.instance.issue = issue
            comment_form.save()
            messages.success(request, 'You have successfully commented on this issue.')
            return redirect(view_issue, pk)
    else:
        comment_form = CommentForm()
    return render(request, 'comment_form.html', {'comment_form': comment_form})
    
@login_required()
def edit_comment(request, pk):
    """
    This view allows the user that submitted the original comment or a staff member to edit a comment.
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment_issue = comment.issue
    issue_pk = comment_issue.id
    if request.method == "POST":
        comment_edit_form = CommentForm(request.POST, request.FILES, instance=comment)
        if comment_edit_form.is_valid():
            comment_edit_form.instance.contributor = request.user
            comment_edit_form.instance.issue = comment_issue
            comment_edit_form.save()
            messages.success(request, 'You have successfully made changes to the comment.')
            return redirect(view_issue, issue_pk)
    else:
        comment_edit_form = CommentForm(instance=comment)
    return render(request, 'comment_edit_form.html', {'comment_edit_form': comment_edit_form})
    
@login_required()
def delete_comment(request, pk):
    """
    This view allows the user who submitted the original comment or a staff member to delete a comment. 
    """
    comment_for_deletion = Comment.objects.get(pk=pk)
    comment_for_deletion_issue = comment_for_deletion.issue
    issue_pk = comment_for_deletion_issue.id
    comment_for_deletion.delete()
    messages.success(request, "You have successfully deleted this comment.")
    return redirect('view_issue', issue_pk)


@login_required()
def my_contributions(request):
    """
    This view will render the My Contributions page.
    """
    user = request.user
    my_issues = Issue.objects.filter(contributor=user)
    my_comments = Comment.objects.filter(contributor=user)
    
    return render(request, "my_contributions.html", {'my_issues': my_issues, 'my_comments': my_comments})
    
    
''' Reference:
Author: Daly, J. (2019).
Title: "issue-tracker"
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/jordandaly/issue_tracker
'''