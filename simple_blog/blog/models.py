from django.db import models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True, editable=False)
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, editable=False)
    content = models.TextField()
    name = models.CharField(max_length=80)
    email = models.EmailField()
    def __unicode__(self):
        return self.name
    
class CommentForm(forms.Form):
    class Meta:
        model = Comment
