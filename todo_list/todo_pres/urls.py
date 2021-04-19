from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin
from . import views

# urlpatterns = [
#     url('', views.AllTasksView.as_view(), name="all_tasks"),
#     url('detail/')
#     # url('category/', category, name="category"),
# ]

urlpatterns = [
    path('', views.AllTasksView.as_view(), name='all_task'),
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('detail_task/<int:pk>', views.DetailTaskView.as_view(), name='detail_task'),
    path('edit_task/<int:pk>', views.EditTaskView.as_view(), name='edit_task'),
    path('category/', views.CategoryView.as_view(), name='tasks_category')
]