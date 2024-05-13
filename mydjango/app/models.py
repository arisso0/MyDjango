from django.db import models
from simple_history.models import HistoricalRecords


class DateCreatedUpdated(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(DateCreatedUpdated):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()


class UserReview(DateCreatedUpdated):
    username = models.CharField(max_length=1000)


class Review(DateCreatedUpdated):
    author = models.CharField(max_length=100)
    user = models.ForeignKey(UserReview, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='user_review')
    is_posted = models.BooleanField(default=True)
    description = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    history = HistoricalRecords(excluded_fields=['book', 'date_created', 'date_updated'])


class Author(DateCreatedUpdated):
    name = models.CharField(max_length=2000)
    books = models.ManyToManyField(Book, related_name='book')
