from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponse


def map(request):
    return render(request, 'main/map.html')
    
def main(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html',{'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)  
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments},)
    
def new(request) :
    return render(request, 'main/new.html')


def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.price = request.POST['price']
    new_post.pub_date = timezone.now()
    new_post.location = request.POST['location']
    new_post.intention = request.POST['intention']
    new_post.genre = request.POST['genre']
    new_post.summary = request.POST['summary']
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()

    return redirect('main:detail',new_post.id)

def edit(request, id) :
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.intention = request.POST['intention']
    update_post.price = request.POST['price']
    update_post.genre = request.POST['genre']
    update_post.summary = request.POST['summary']
    update_post.location = request.POST['location']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id) :
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:main')



def create_comment(request, post_id):
   new_comment = Comment()
   new_comment.content = request.POST['content']
   new_comment.post = get_object_or_404(Post, pk = post_id)
   new_comment.save() 
   return redirect('main:detail', post_id)

def edit_comment(request, comment_id):
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request, 'main/comment_edit.html', {'comment' : edit_comment})

def update_comment(request, comment_id):
    update_comment = get_object_or_404(Comment, pk = comment_id)
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('main:detail', update_comment.post.id)    

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return detail(request, comment.post.id)