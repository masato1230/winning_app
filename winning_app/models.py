from django.db import models

class Thread(models.Model):
  thread_title = models.CharField(max_length=100)
  thread_desc = models.TextField(blank=True)
  created_date = models.DateTimeField(auto_now_add=True)
  tags = models.TextField(blank=True)

  def __str__(self):
    return self.thread_title

class Comment(models.Model):
  thread_id = models.IntegerField(null=False)
  comment = models.CharField(max_length=200)
  nick_name = models.CharField(max_length=20, null=True, default='匿名さん')
  created_time = models.DateTimeField(auto_now_add=True)
  goods = models.IntegerField(blank=True, default=0)
  replies = models.IntegerField(blank=True, default=0)

  def __str__(self):
    return self.comment





