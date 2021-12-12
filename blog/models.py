from django.db import models
from django.utils import timezone

STATUS = (
    (0, "Szkic"),
    (1, "Opublikowany")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now(), blank=False, null=False)
    published_date = models.DateTimeField(
        blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
