from django.core.management.base import BaseCommand
from books.models import Book
import random


class Command(BaseCommand):

    help = "This command adds book's photo"

    def handle(self, *args, **options):
        for book in Book.objects.all():
            book.cover_image = f"book_photos/{random.randint(1, 20)}.jpg"
            book.save()
        self.stdout.write(self.style.SUCCESS("Photo added!"))
