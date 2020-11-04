from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Comment
from .forms import CreateThreadForm, CreateCommentForm



def home(request):
  threads = Thread.objects.all()
  return render(request, 'winning_app/home.html', {'threads': threads})


def thread(request, thread_id):
  thread = get_object_or_404(Thread, pk=thread_id)
  comments = Comment.objects.all().filter(thread_id=thread_id)
  form = CreateCommentForm(request.POST or None)
  context = {
    'thread': thread,
    'comments': comments,
  }
  # コメントが投稿された時の処理
  if request.method == "POST":
    comment = request.POST['comment']
    nick_name = request.POST['nick_name']
    new_comment = Comment(thread_id=thread_id, comment=comment, nick_name=nick_name)
    new_comment.save()

  return render(request, 'winning_app/thread.html', context)

def new_thread(request):
  error_message = ""
  context = {}
  form = CreateThreadForm(request.POST or None)
  if request.POST.get('thread_title'):
    obj = form.save()
    form = CreateThreadForm()
    new_thread = Thread.objects.latest('created_date')
    thread_id = new_thread.id
    return redirect('thread', thread_id=thread_id)
  context['form'] = form
  return render(request, 'winning_app/new_thread.html', context)