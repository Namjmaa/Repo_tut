from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .forms import NoteForm
from .models import Todo
from .models import Note


def home(request):
    context = {"todos": Todo.objects.all().order_by("-created_date")}
    return render(request, "home.html", context)


def create_todo(request):
    if request.method == "POST":
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Амжилттай үүсгэлээ!")
            return redirect("home")
    else:
        forms = TodoForm()

    context = {"form": forms}
    return render(request, "create.html", context)


def edit_todo(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(id=pk)
        forms = TodoForm(request.POST)
        if forms.is_valid():
            todo.title = forms.instance.title
            todo.task_content = forms.instance.task_content
            todo.save()
            messages.success(request, "Амжилттай шинэчиллээ!")
            return redirect("home")
    else:
        todo = Todo.objects.get(id=pk)
        forms = TodoForm(instance=todo)
    return render(request, "edit.html", {"form": forms})


def complete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    context = {"todos": Todo.objects.all()}
    return render(request, "home.html", context)


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    context = {"todos": Todo.objects.all()}
    return render(request, "home.html", context)


def completed(request):
    todo = Todo.objects.all().filter(complete=True)
    context = {"todos": todo}
    return render(request, "completed.html", context)


def note(request):
    if request.method == "POST":
        forms = NoteForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Амжилттай үүсгэлээ!")
            return redirect("notes")
    else:
        forms = NoteForm()

    context = {"notes": Note.objects.all().order_by("-created_date"), "form": forms}
    return render(request, "note.html", context)
