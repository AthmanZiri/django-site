# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    try:
        detail = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'blog/post_detail.html', {'detail': detail})