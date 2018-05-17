from django import forms
from .models import Content, Skill

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title','text','image')

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('title','text','image')