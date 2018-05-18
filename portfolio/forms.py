from django import forms
from .models import Content, Skill, Skill_Item

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title','text','image')

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('title','text','image')

class Skill_ItemForm(forms.ModelForm):
    class Meta:
        model = Skill_Item
        fields = ('name','perc_value','skill_ref')