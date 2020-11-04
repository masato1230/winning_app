from django import forms
from .models import Thread, Comment


class CreateThreadForm(forms.ModelForm):
  class Meta:
    model = Thread
    fields = ['thread_title', 'thread_desc', 'tags']
    labels = {
      'thread_title': 'スレッドタイトル',
      'thread_desc': '(任意)スレッドの説明を書いてください',
      'tags': '(任意)タグを設定してください',
    }


class CreateCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['thread_id', 'comment', 'nick_name']
