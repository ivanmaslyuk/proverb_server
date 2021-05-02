from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('port', type=int)

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('runserver', options['port'])
