from django.contrib import admin
from .models import Content, Skill, Skill_Item

# Register your models here.
admin.site.register(Content)
admin.site.register(Skill)
admin.site.register(Skill_Item)