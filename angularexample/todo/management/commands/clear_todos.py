from django.core.management import BaseCommand

from angularexample.todo.models import Todo

class Command(BaseCommand):
    def handle(self, *args, **options):
        todos = Todo.objects.all()
        n_todos = todos.count()
        todos.delete()
        print 'Deleted %d todos' % n_todos

