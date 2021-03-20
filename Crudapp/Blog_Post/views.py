from django.shortcuts import get_list_or_404, render,redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import ModelForm
from Blog_Post.models import BlogPost
# Create your views here.

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields =['date','author','post']

def Post_list(request,template_name='Blog_posts/Post_list.html'): 
    post = BlogPost.objects.all()
    data ={} #Empty dictionary
    data['object_list'] = post
    print(post)
    return render(request,template_name,data) 

def Post_delete(request,pk): 
    post = get_object_or_404(BlogPost,pk=pk)      # get_list_or_404 is used for creating list
    if request.method=='POST':
        post.delete()
        return redirect('Post_view')  # Post_view in urls.py
    return render(request, "Blog_posts/Post_delete.html", {'object':post}) 

def Post_form(request): 
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Post_view')
    return render(request, "Blog_posts/Post_form.html",{'form':form}) 



