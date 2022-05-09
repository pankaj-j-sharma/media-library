from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from importlib_metadata import files

from media.forms import MediaItemForm,CategoryForm
from .models import MediaItem
from pprint import pprint
from .sql_wrapper import get_data_from_db
import os


@login_required(login_url="/login/")
def index(request):
    all_medias = get_data_from_db('all_media')
    pprint(list(all_medias))
    return render(request, "media/index.html", {'all_media': all_medias})


def create(request):
    if request.method == "POST":
        print('files', request.FILES)
        # os.path.getsize('Your file path')
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/media/")
    else:
        form = MediaItemForm()

    return render(request, "media/edit.html", {"form": form, })


def update(request, id):
    media_item = get_object_or_404(MediaItem, pk=id)
    if request.method == 'POST':
        print('files', request.FILES)
        form = MediaItemForm(instance=media_item,
                             data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/media/")
    else:
        form = MediaItemForm(instance=media_item)
    return render(request, "media/edit.html", {"form": form, "object": media_item})


def detail(request, id):
    media_item = get_data_from_db('all_media', {'id': id})
    return render(request, "media/detail.html", {'all_media': media_item})


def delete(request, id):
    media_item = get_object_or_404(MediaItem, pk=id)
    media_item.delete()
    return redirect("/media/")


def categories(request):
    all_categories = get_data_from_db('all_category')
    pprint(list(all_categories))
    return render(request, "categories/index.html", {'all_categories': all_categories})


def add_category(request):
    if request.method == "POST":
        print('files', request.FILES)
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/media/")
    else:
        form = CategoryForm()

    return render(request, "categories/edit.html", {"form": form, })
