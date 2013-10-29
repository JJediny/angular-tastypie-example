from django.core.management import BaseCommand

from angularexample.todo.models import Todo

class Command(BaseCommand):
    def handle(self, *args, **options):
        todos = [
            'Learn Angular',
            'Learn Restangular',
            'Buy wine',
            'Buy beer',
            'Invite friends',
            'Throw a big party'
        ]

        count = 0
        for todo in todos:
            t, created = Todo.objects.get_or_create(text=todo)
            if created:
                count += 1
        print 'Created %d todos' % count

