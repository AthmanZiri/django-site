from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Project


def project_list(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request):
	try:
		detail = Project.objects.get(pk=post_id)
	except Project.DoesNotExist:
		raise Http404
	return render(request, 'portfolio/portfolio_detail.html', {'detail': detail})