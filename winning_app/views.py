from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Comment
from .forms import CreateThreadForm, CreateCommentForm



def home(request):
  threads = Thread.objects.all()
  return render(request, 'winning_app/home.html', {'threads': threads})


def thread(request, thread_id):
  thread = get_object_or_404(Thread, pk=thread_id)
  comments = Comment.objects.all().filter(thread_id=thread_id)
  context = {
    'thread': thread,
    'comments': comments,
  }
  # コメントが投稿された時の処理
  if request.method == "POST":
    comment = request.POST['comment']
    nick_name = request.POST['nick_name']
    new_comment = Comment(thread_id=thread_id, comment=comment, nick_name=nick_name)
    thread.comment_number += 1
    print(thread.comment_number)
    new_comment.save()
    thread.save()
    

  return render(request, 'winning_app/thread.html', context)

def new_thread(request):
  error_message = ""
  context = {}
  if request.method == "POST":
    thread_title = request.POST['thread_title']
    thread_desc = request.POST['thread_desc']
    tags = request.POST['tags']
    new_thread = Thread(thread_title=thread_title, thread_desc=thread_desc)
    new_thread.save()
    created_thread = Thread.objects.latest('created_date')
    thread_id = created_thread.id
    return redirect('thread', thread_id=thread_id)
  return render(request, 'winning_app/new_thread.html', context)