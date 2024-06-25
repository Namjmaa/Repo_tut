import pytest
from django.utils import timezone
from .models import Todo  
from .forms import TodoForm  

@pytest.fixture
def todo():
    todo = Todo.objects.create(
        title='Test todo',
        task_content='task content test',
        created_date=timezone.now(),
        complete=False,
    )
    yield todo
    todo.delete()

@pytest.mark.django_db
def test_todo_creation(todo):
    assert todo.title == 'Test todo'
    assert todo.task_content == 'task content test'
    assert not todo.complete
    assert todo.created_date is not None

@pytest.mark.django_db
def test_todo_form_valid(todo):
    form_data = {
        'title': todo.title,
        'task_content': todo.task_content
    }
    form = TodoForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_todo_form_invalid(todo):
    form_data = {
        'title': '',
        'task_content': todo.task_content
    }
    form = TodoForm(data=form_data)
    assert not form.is_valid()
    


