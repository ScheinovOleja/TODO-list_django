from django.db.models import *
from django.utils import timezone


# Create your models here.


class Category(Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoList(Model):

    class Meta:
        ordering = ["-creation_date"]

    title = CharField(max_length=250, verbose_name='Задача')
    content = TextField(max_length=1000, blank=True, verbose_name='Описание задачи')
    creation_date = DateField(auto_now_add=True, verbose_name='Дата создания')
    deadline = DateField(default=timezone.now().date(), verbose_name='Дедлайн выполнения (гггг-мм-дд)')
    category = ForeignKey(Category, default="Главные", on_delete=PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title
