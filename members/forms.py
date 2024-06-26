from django import forms
from .models import Todo
from .models import Note
from .models import Comment


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "task_content"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["name", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
