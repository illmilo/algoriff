from django.db import models
from django.db.models.fields.files import ImageFieldFile

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100)
    short = models.TextField()
    tag = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    image = models.ImageField(upload_to='courses/headers/')
    lessons_count = models.CharField(max_length=20)
    tutor = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class PublicRelations(models.Model):
    title = models.CharField(max_length=100)
    short = models.TextField()
    style = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Public Relation'
        verbose_name_plural = 'Public Relations'