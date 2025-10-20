from django.contrib import admin
from django.urls import path

# Import all views from taskmanager
from taskmanager.views import (
    # Dashboard
    HomePageView,

    # List pages
    TaskListView,
    SubTaskListView,
    CategoryListView,
    PriorityListView,
    NoteListView,

    # CRUD (Create, Update, Delete)
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    PriorityCreateView,
    PriorityUpdateView,
    PriorityDeleteView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    SubTaskCreateView,
    SubTaskUpdateView,
    SubTaskDeleteView,
)

urlpatterns = [
    # 🧭 Admin Panel
    path("admin/", admin.site.urls),

    # 🏠 Dashboard
    path("", HomePageView.as_view(), name="home"),

    # ✅ Tasks
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/add/", TaskCreateView.as_view(), name="task_add"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    # ✅ SubTasks
    path("subtasks/", SubTaskListView.as_view(), name="subtasks"),
    path("subtasks/add/", SubTaskCreateView.as_view(), name="subtask_add"),
    path("subtasks/<int:pk>/edit/", SubTaskUpdateView.as_view(), name="subtask_edit"),
    path("subtasks/<int:pk>/delete/", SubTaskDeleteView.as_view(), name="subtask_delete"),

    # ✅ Categories
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("categories/add/", CategoryCreateView.as_view(), name="category_add"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),

    # ✅ Priorities
    path("priorities/", PriorityListView.as_view(), name="priorities"),
    path("priorities/add/", PriorityCreateView.as_view(), name="priority_add"),
    path("priorities/<int:pk>/edit/", PriorityUpdateView.as_view(), name="priority_edit"),
    path("priorities/<int:pk>/delete/", PriorityDeleteView.as_view(), name="priority_delete"),

    # ✅ Notes
    path("notes/", NoteListView.as_view(), name="notes"),
    path("notes/add/", NoteCreateView.as_view(), name="note_add"),
    path("notes/<int:pk>/edit/", NoteUpdateView.as_view(), name="note_edit"),
    path("notes/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]
