from django.forms import *

from .models import Category, TodoList


class TasksForm(ModelForm):

    class Meta:
        model = TodoList
        fields = "__all__"


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
