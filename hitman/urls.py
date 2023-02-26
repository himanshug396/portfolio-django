from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import *
from .models import NavigationItem
import string
import random

def generateRandomURL():
	return ''.join(random.choice(string.ascii_lowercase) for i in range(16));


def addTemplateURLs(urlpatterns):
	# navigation_items = NavigationItem.objects.filter(show=True)
	# for item in navigation_items:
	# 	url = generateRandomURL()
	# 	name = item['id']
	# 	template_name = 'hitman/navigation/' + name + '.html'
	# 	if name in []:
	# 		urlpatterns.append()
	# 	elif name in ['page-work']:
	# 		urlpatterns.append(path(url, projects, name=name))
	# 	elif name in ['page-home']:
	# 		urlpatterns.append(path(url, aboutme, name=name))
	# 	else:
	# 		urlpatterns.append(path(url, TemplateView.as_view(template_name=template_name), name=name))
	return urlpatterns

urls = [
	path('', website, name='website'),
	path('query/', contact_form, name='contact_form'),
	path(generateRandomURL(), resume, name='page-resume'),
	path(generateRandomURL(), projects, name='page-work'),
	path(generateRandomURL(), home, name='page-home'),
	path(generateRandomURL(), TemplateView.as_view(template_name='hitman/navigation/page-game.html'), name='page-game'),
	path(generateRandomURL(), gallery, name='page-gallery'),
	path(generateRandomURL(), contact, name='page-contact'),
]

urlpatterns = addTemplateURLs(urls)