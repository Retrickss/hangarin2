from django import forms
from .models import Task, SubTask, Category, Priority, Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "deadline", "status", "category", "priority"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ["title", "status", "parent_task"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ["name"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["task", "content"]
