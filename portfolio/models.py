from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images',height_field=None,width_field=None,max_length=100,null='images/None/no-img.jpg')
    
    #image = models.CharField(max_length=200, null=True)
    #image = models.ImageField(upload_to='images',height_field=None,width_field=None,max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images',height_field=None,width_field=None,max_length=100,null='images/None/no-img.jpg')

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title

class Skill_Item(models.Model):
    name = models.CharField(max_length=200)
    perc_value = models.PositiveSmallIntegerField(default=50, validators=[MaxValueValidator(100)])
    skill_ref = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return self.name