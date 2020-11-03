from django.shortcuts import render, get_object_or_404
from .models import Thread, Comment
# Create your views here.


def home(request):
  threads = Thread.objects.all()
  return render(request, 'winning_app/home.html', {'threads': threads})


def thread(request, thread_id):
  thread = get_object_or_404(Thread, pk=thread_id)
  return render(request, 'winning_app/thread.html', {'thread': thread})