from django.shortcuts import render, get_object_or_404
from .models import Content, Skill, Skill_Item
from django.utils import timezone
from .forms import ContentForm, SkillForm, Skill_ItemForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def content_list(request):
    contents = Content.objects.filter(published_date__lte=timezone.now()).order_by('title')
    skills = Skill.objects.filter(published_date__lte=timezone.now()).order_by('title')
    #skill_items = Skill_Item.objects.order_by('-perc_value')
    return render(request, 'portfolio/content_list.html', {'contents':contents, 'skills':skills })

def content_detail(request,pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'portfolio/content_detail.html', {'content':content} )

def skill_detail(request,pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill_items = Skill_Item.objects.filter(skill_ref=skill).order_by('-perc_value')
    return render(request, 'portfolio/skill_detail.html', {'skill':skill, 'skill_items':skill_items } )


@login_required
def content_new(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            
            return redirect('content_detail', pk=content.pk)
    else:
        form = ContentForm()
    return render(request,'portfolio/content_edit.html',{'form':form})

@login_required
def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            content = form.save()
           
            return redirect('content_detail', pk=content.pk)
    else:
        form = ContentForm(instance=content)
    return render(request,'portfolio/content_edit.html',{'form':form})

@login_required
def content_lista_bozze(request):
    contents = Content.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'portfolio/content_lista_bozze.html', {'contents':contents})

@login_required
def content_publish(request, pk):
    content = get_object_or_404(Content, pk=pk)
    content.publish()
    return redirect('content_detail', pk=pk)

@login_required
def content_remove(request, pk):
    content = get_object_or_404(Content, pk=pk)
    content.delete()
    return redirect('content_list')

@login_required
def skill_new(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = SkillForm()
    return render(request,'portfolio/skill_edit.html',{'form':form})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill = form.save()
            
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = SkillForm(instance=skill)
    return render(request,'portfolio/skill_edit.html',{'form':form})

@login_required
def skill_lista_bozze(request):
    skills = Skill.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'portfolio/skill_lista_bozze.html', {'skills':skills})

@login_required
def skill_publish(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.publish()
    return redirect('skill_detail', pk=pk)

@login_required
def skill_remove(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('content_list')

@login_required
def skill_item_new(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = Skill_ItemForm(request.POST)
        if form.is_valid():
            '''
            post	=	form.save(commit=False)
            post.author	=	request.user
            post.published_date	=	timezone.now()
            post.save()
            '''
            skill_item = form.save(commit=False)
            skill_item.skill_ref = skill
            skill_item.save()
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = Skill_ItemForm()
    return render(request,'portfolio/skill_item_edit.html',{'form':form})

@login_required
def skill_item_edit(request, pk, pk_item):
    skill = get_object_or_404(Skill, pk=pk)
    skill_item = get_object_or_404(Skill_Item, pk=pk_item)
    if request.method == "POST":
        form = Skill_ItemForm(request.POST, instance=skill_item)
        if form.is_valid():
            skill_item = form.save()
            return redirect('skill_detail', pk=pk)
    else:
        form = Skill_ItemForm(instance=skill_item)
    return render(request,'portfolio/skill_item_edit.html',{'form':form})

@login_required
def skill_item_remove(request, pk, pk_item):
    skill_item = get_object_or_404(Skill_Item, pk=pk_item)
    skill = get_object_or_404(Skill, pk=pk)
    skill_item.delete()
    return redirect('skill_detail', pk=pk)
