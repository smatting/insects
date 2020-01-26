from django.core.management.base import BaseCommand, CommandError

from insects_backend.schema import schema

class Command(BaseCommand):
    help = 'Print the graphql schema'

    def handle(self, *args, **options):
        print(str(schema))
