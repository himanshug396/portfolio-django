import os
from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from portfolio.settings import STATIC_ROOT
from django.templatetags.static import static

# Create your views here.

def website(request):
	navigation_items = NavigationItem.objects.filter(show=True).order_by('rank')
	social_items = SocialMedia.objects.filter(show=True)
	resume_path = Resume.objects.filter(use=True)[0].name.url
	context = {
		"navigation_items": navigation_items,
		"social_items": social_items,
		"resume_path": resume_path
	}
	return render(request, 'hitman/index.html', context)

@xframe_options_exempt
def home(request):
	social_items = SocialMedia.objects.filter(show=True)
	aboutme = AboutmeText.objects.filter(use=True)[0]
	context = {
		"aboutme": aboutme.text,
		"social_items": social_items
	}
	return render(request, 'hitman/navigation/page-home.html', context)

def projects(request):
	projects = Project.objects.filter(show=True).order_by('rank')
	skills = Skill.objects.all()
	context = {
		"projects": projects,
		"skills": skills
	}
	return render(request, 'hitman/navigation/page-work.html', context)

def gallery(request):
	context = {}
	return render(request, 'hitman/navigation/page-gallery.html', context)

def contact(request):
	social_items = SocialMedia.objects.filter(show=True)
	context = {
		"social_items": social_items
	}
	return render(request, 'hitman/navigation/page-contact.html', context)

@xframe_options_exempt
def resume(request):
	resume_path = Resume.objects.filter(use=True)[0].name.url
	context = {
		"resume_path": resume_path
	}
	return render(request, 'hitman/navigation/page-resume.html', context)

def contact_form(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		question = request.POST.get("question")
		instance = Query.objects.create(
			name=name, email=email, phone=phone, question=question)
		instance.save()
	return HttpResponse(status=204)
