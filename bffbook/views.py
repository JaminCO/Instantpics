from django.http import HttpResponse
from profiles.models import Profile
from posts.models import Post, Like
from django.shortcuts import render
from datetime import  datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.forms import PostModelForm, CommentModelForm
from django.http import JsonResponse

def about(request):
    return render(request, 'main/about.html')

@login_required
def home_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    # initials
    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False

    profile = Profile.objects.get(user=request.user)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = PostModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()


    context = {
        'qs': qs,
        'profile': profile,
        'Profile': profile,
        'p_form': p_form,
        'c_form': c_form,
        'post_added': post_added,
    }	
    
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello World')




# user = request.user
# 	hello = 'Hello '
# 	# welcome =  messages.info(request, "Info: This is the sample info Flash message.")

# 	context = {
# 		'user':user,
# 		'hello' : hello,
# 	}