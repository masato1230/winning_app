from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('thread/<int:thread_id>', views.thread, name='thread'),
  path('new_thread/', views.new_thread, name='new_thread'),
  path('good/<int:comment_id>/<int:thread_id>', views.goods, name='goods'),
]