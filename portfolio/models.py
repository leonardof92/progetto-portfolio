from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Skill_Item(models.Model):
    name = models.CharField(max_length=200)
    perc_value = models.PositiveSmallIntegerField(default=50, validators=[MaxValueValidator(100)])
    skill_ref = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return self.name