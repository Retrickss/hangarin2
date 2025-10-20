from datetime import date
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .forms import TaskForm, SubTaskForm, CategoryForm, PriorityForm, NoteForm
from .models import Task, SubTask, Note, Category, Priority


class HomePageView(View):
    template_name = "home.html"

    def get(self, request):
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(status="Completed").count()
        in_progress_tasks = Task.objects.filter(status="In Progress").count()
        pending_tasks = Task.objects.filter(status="Pending").count()
        recent_tasks = Task.objects.order_by("-updated_at")[:5]

        context = {
            "today": date.today(),
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "in_progress_tasks": in_progress_tasks,
            "pending_tasks": pending_tasks,
            "recent_tasks": recent_tasks,
        }
        return render(request, self.template_name, context)


# --- TASKS ---
class TaskListView(View):
    template_name = "tasks.html"

    def get(self, request):
        query = request.GET.get("q", "")
        tasks = Task.objects.select_related("category", "priority").order_by("-created_at")
        if query:
            tasks = tasks.filter(title__icontains=query)

        paginator = Paginator(tasks, 5)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, self.template_name, {"page_obj": page_obj, "query": query})


# --- SUBTASKS ---
class SubTaskListView(View):
    template_name = "subtasks.html"

    def get(self, request):
        query = request.GET.get("q", "")
        subtasks = SubTask.objects.select_related("parent_task").order_by("-created_at")
        if query:
            subtasks = subtasks.filter(title__icontains=query)

        paginator = Paginator(subtasks, 5)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, self.template_name, {"page_obj": page_obj, "query": query})


# --- CATEGORIES ---
class CategoryListView(View):
    template_name = "categories.html"

    def get(self, request):
        query = request.GET.get("q", "")
        categories = Category.objects.all().order_by("name")
        if query:
            categories = categories.filter(name__icontains=query)

        paginator = Paginator(categories, 5)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, self.template_name, {"page_obj": page_obj, "query": query})


# --- PRIORITIES ---
class PriorityListView(View):
    template_name = "priorities.html"

    def get(self, request):
        query = request.GET.get("q", "")
        priorities = Priority.objects.all().order_by("name")
        if query:
            priorities = priorities.filter(name__icontains=query)

        paginator = Paginator(priorities, 5)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, self.template_name, {"page_obj": page_obj, "query": query})


# --- NOTES ---
class NoteListView(View):
    template_name = "notes.html"

    def get(self, request):
        query = request.GET.get("q", "")
        notes = Note.objects.select_related("task").order_by("-created_at")
        if query:
            notes = notes.filter(content__icontains=query)

        paginator = Paginator(notes, 5)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, self.template_name, {"page_obj": page_obj, "query": query})

# --- 🟦 Task CRUD ---
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "edit_task.html"
    success_url = reverse_lazy("tasks")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "edit_task.html"
    success_url = reverse_lazy("tasks")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete_task.html"
    success_url = reverse_lazy("tasks")


# --- 🟪 Category CRUD ---
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "edit_category.html"
    success_url = reverse_lazy("categories")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "edit_category.html"
    success_url = reverse_lazy("categories")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "delete_category.html"
    success_url = reverse_lazy("categories")


# --- 🟨 Priority CRUD ---
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "edit_priority.html"
    success_url = reverse_lazy("priorities")


class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "edit_priority.html"
    success_url = reverse_lazy("priorities")


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "delete_priority.html"
    success_url = reverse_lazy("priorities")


# --- 🟩 Notes CRUD ---
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "edit_note.html"
    success_url = reverse_lazy("notes")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "edit_note.html"
    success_url = reverse_lazy("notes")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "delete_note.html"
    success_url = reverse_lazy("notes")


# --- 🟥 SubTask CRUD ---
class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "edit_subtask.html"
    success_url = reverse_lazy("subtasks")


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "edit_subtask.html"
    success_url = reverse_lazy("subtasks")


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "delete_subtask.html"
    success_url = reverse_lazy("subtasks")
