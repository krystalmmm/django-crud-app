from django.urls import path, re_path
from . import views

"""
  我们需要创建5个urls, 对应5个函数视图。这是因为对于Retrieve操作，我们需要编写两个函数视图，
  一个用户获取任务列表，一个用于获取任务详情。对于task_detail, task_update和task_delete
  这个三个视图函数，我们还需要通过urls传递任务id或pk参数，否则它们不知道对哪个对象进行操作。

"""
  
# namespace
app_name = 'tasks'
  
  
urlpatterns = [
    # Create a task
    path('create/', views.task_create, name='task_create'),
    
    # Retrieve task list
    path('', views.task_list, name='task_list'),
    
    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    
    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    
    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]