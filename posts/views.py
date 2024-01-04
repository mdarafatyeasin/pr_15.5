from django.shortcuts import render,redirect
from . import forms
from . models import Post

# Create your views here.
def addPost (request):
    if request.method == 'POST':
        post_form = forms.add_post(request.POST)
        if post_form.is_valid:
            post_form.save()
            return redirect('homePage')
    else:
        post_form = forms.add_post()
    return render (request, 'add_post.html', {'form':post_form})


def editPost (request, id):
    post = Post.objects.get(pk=id)
    post_form = forms.add_post(instance=post)
    if request.method == 'POST':
        post_form = forms.add_post(request.POST, instance=post)
        if post_form.is_valid:
            post_form.save()
            return redirect('homePage')
    return render (request, 'edit_post.html', {'form':post_form})


def deletePost(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('homePage')
