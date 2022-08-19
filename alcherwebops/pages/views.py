from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView,CreateView,DetailView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from users.models import Profile





class PostListView(ListView):
	model=Post
	template_name='pages/profile_page.html'
	context_object_name='posts'
	ordering=["-date_posted"]
	#<app><model>_<viewtype>.html




class MyPostsListView(ListView):
	model=Post
	template_name='pages/my_posts.html'
	context_object_name='posts'
	ordering=["-date_posted"]
	#<app><model>_<viewtype>.
	def get_queryset(self):
		return Post.objects.filter(username=self.request.user)

class PostDetailView(DetailView):
	model=Post


class PostCreateView(CreateView):
	model=Post
	fields=['caption','picture']
	def form_valid(self,form):
		form.instance.username=self.request.user
		return super().form_valid(form)

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('post-detail',kwargs())






def login_page(request):

	return render(request,'pages/login_page.html')

@login_required
def profile(request):
	context={"posts":Post.objects.all()}
	return render(request,'pages/profile_page.html',context)

@login_required
def upload(request):
	return render(request,'pages/add_post_page.html')

@login_required
def myposts(request):
	if pk:
		post_owner = get_object_or_404(User, pk=pk)
		user_posts=Post.objects.filter(user=request.user)

	else:
		post_owner = request.user
		user_posts=Post.objects.filter(user=request.user)
	return render(request,'pages/my_posts.html',{'post_owner': post_owner, 'user_posts': user_posts})

@login_required
def update_profile(request):
	if request.method=="POST":
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,"Account succesfully updated for {} ".format(request.user.username))
			return redirect('profile-page')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)


	context={
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'pages/edit_profile.html',context)


@login_required
def favourite_add(request,id):
	post=get_object_or_404(Post,id=id)
	if post.favourites.filter(id=request.user.id).exists():
		post.favourites.remove(request.user)

	else:
		post.favourites.add(request.user)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
	new=Post.objects.filter(favourites=request.user)
	return render(request,'pages/favourites.html',{'new':new})

# Create your views here.
