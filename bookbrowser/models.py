from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)


class IndustryIdentifier(models.Model):
    type = models.CharField(max_length=256)
    identifier = models.CharField(max_length=256)


class ImageLink(models.Model):
    small_thumbnail = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256)


class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(to=Author)
    published_date = models.CharField(max_length=10)
    industry_identifiers = models.ForeignKey(to=IndustryIdentifier, on_delete=models.CASCADE)
    page_count = models.IntegerField(blank=True)
    image_links = models.ForeignKey(to=ImageLink, on_delete=models.CASCADE)
    language = models.CharField(max_length=128)
