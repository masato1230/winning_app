from django.shortcuts import render, get_object_or_404
from .models import Thread, Comment
from .forms import CreateThreadForm



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
  return render(request, 'winning_app/thread.html', context)

def new_thread(request):
  error_message = ""
  context = {}
  form = CreateThreadForm(request.POST or None)
  if request.POST.get('thread_title'):
    obj = form.save()
    form = CreateThreadForm()
  context['form'] = form
  return render(request, 'winning_app/new_thread.html', context)