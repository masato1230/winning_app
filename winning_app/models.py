from django.db import models

class Thread(models.Model):
  thread_title = models.CharField(max_length=100)
  thread_desc = models.TextField(blank=True)
  created_date = models.DateField(auto_now_add=True)
  tags = models.TextField(blank=True)

class Comment(models.Model):
  thread_id = models.IntegerField(null=False)
  comment = models.CharField(max_length=100)
  goods = models.IntegerField(blank=True)
  replies = models.IntegerField(blank=True)





