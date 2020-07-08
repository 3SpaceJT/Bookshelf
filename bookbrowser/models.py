from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class IndustryIdentifier(models.Model):
    type = models.CharField(max_length=256)
    identifier = models.CharField(max_length=256)

    def __str__(self):
        return self.identifier


class ImageLink(models.Model):
    small_thumbnail = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256)

    def __str__(self):
        return self.small_thumbnail


class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(to=Author)
    published_date = models.CharField(max_length=10)
    industry_identifiers = models.ForeignKey(to=IndustryIdentifier, on_delete=models.CASCADE)
    page_count = models.IntegerField(blank=True)
    image_links = models.ForeignKey(to=ImageLink, on_delete=models.CASCADE)
    language = models.CharField(max_length=128)

    def __str__(self):
        return self.title
