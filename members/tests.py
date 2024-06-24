from django.test import TestCase
from django.utils import timezone
from .models import Todo, Note
from .forms import TodoForm, NoteForm

class TodoModelTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title='Test todo',
            task_content='This is a test todo',
            created_date= timezone.now(),
            complete = False,
        )

    def test_todo_creation(self):
        #todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(self.todo.title, 'Test todo')
        self.assertEqual(self.todo.task_content, 'This is a test todo')
        self.assertFalse(self.todo.complete)
        self.assertIsNotNone(self.todo.created_date)

    def test_todo_str(self):
        self.assertEqual(str(self.todo), 'Test todo')

class NoteModelTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            name='Test Note',
            content='This is a test note content',
        )

    def test_note_creation(self):
        self.assertEqual(self.note.name, 'Test Note')
        self.assertEqual(self.note.content, 'This is a test note content')
        self.assertIsNotNone(self.note.created_date)

    def test_note_str(self):
        self.assertEqual(str(self.note), 'Test Note')


class TodoFormTest(TestCase):
    def test_todo_form_valid(self):
        form_data = {
            'title': 'test shuu',
            'task_content': 'test task content'
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_form_invalid(self):
        form_data = {
            'title': '', 
            'task_content': 'aldaatai task'
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_note_form_valid(self):
        form_data = {
            'name': 'Test Note',
            'content': 'This is a test note'
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_note_form_invalid(self):
        form_data = {
            'name': '', 
            'content': 'aldaatai note'
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
