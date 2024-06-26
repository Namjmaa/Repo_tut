import pytest
from django.utils import timezone
from .models import Todo, Note
from .forms import TodoForm


@pytest.fixture
def test_todo():
    todo = Todo.objects.create(
        title="Test todo",
        task_content="task content test",
        created_date=timezone.now(),
        complete=False,
    )
    yield todo
    todo.delete()


@pytest.mark.django_db
def test_todo_creation(test_todo):
    assert test_todo.title == "Test todo"
    assert test_todo.task_content == "task content test"
    assert not test_todo.complete
    assert test_todo.created_date is not None


@pytest.mark.django_db
def test_todo_form_valid(test_todo):
    form_data = {"title": test_todo.title, "task_content": test_todo.task_content}
    form = TodoForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_todo_form_invalid(test_todo):
    form_data = {"title": "", "task_content": test_todo.task_content}
    form = TodoForm(data=form_data)
    assert not form.is_valid()


@pytest.fixture
def test_note():
    note = Note.objects.create(
        name="note test", content="content test", created_date=timezone.now()
    )
    yield note
    note.delete()


@pytest.mark.django_db
def test_note_creation(test_note):
    assert test_note.name == "note test"


@pytest.mark.django_db
def test_note_form_valid(test_note):
    form_data = {"name": test_note.name, "content": test_note.content}
    form = TodoForm(data=form_data)
    assert form.is_valid


@pytest.mark.django_db
def test_note_form_invalid(test_note):
    form_data = {"name": test_note.name, "content": ""}
    form = TodoForm(data=form_data)
    assert not form.is_valid()
