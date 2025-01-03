from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, Tag
from .forms import TaskForm, TagForm


# Homepage with list of tasks
class TaskListView(ListView):
    model = Task
    template_name = "tasks/home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at")


# Создание новой задачи
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create task"
        return context

    def get_success_url(self):
        return reverse_lazy("tasks:home")


# Modify task
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Modify task"
        return context

    def get_success_url(self):
        return reverse_lazy("tasks:home")


# Delete task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("tasks:home")


# Changing the task status (completed/uncompleted)
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tasks:home")


# Tag list
class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"


# Create tag
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add tag"
        return context

    def get_success_url(self):
        return reverse_lazy("tasks:tag_list")


# Modify tag
class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Modify tag"
        return context

    def get_success_url(self):
        return reverse_lazy("tasks:tag_list")


# Delete tag
class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/confirm_delete_tag.html"

    def get_success_url(self):
        return reverse_lazy("tasks:tag_list")
