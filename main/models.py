from django.db import models
from django.core.validators import FileExtensionValidator

class Tag(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    title = models.CharField('Title',max_length=100)
    description = models.TextField('Desc',max_length=1000)
    image = models.ImageField('Image',upload_to='covers',blank=True)
    pdf = models.FileField('Pdf',upload_to='pdfs',validators=[FileExtensionValidator(['pdf'])],default=' ')
    tags = models.ManyToManyField(Tag)
    author = models.CharField('Author', max_length=40)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        self.author = self.author.lower()
        super().save(*args, **kwargs)

class Video(models.Model):
    title = models.CharField(max_length=1000)
    video_id = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title