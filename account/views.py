
from .forms import UserForm, PostForm,UpdatePostForm
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post
from django.urls import reverse,reverse_lazy

class LoginView(View):

    def get(self,request):
        form = UserForm()
        if "sign-in" in request.GET:
            username = request.GET.get("username")
            password = request.GET.get("pswd")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Login attemp failed.')
                return redirect('account_login')
        return render(request,'./templates/login.html',{'form':form})
    
    def post(self,request):
        if "sign-up" in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                selected_group = request.POST.get("groups")
                group = Group.objects.get(name=selected_group)
                user.groups.add(group)
                messages.success(request,'Account has been created succesfully')
                return redirect('account_login')
            else:
                messages.error(request,form.errors)
                return redirect('account_login')
        return render(request,'./templates/login.html')

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,'Logged out succesfully.')
        return redirect('account_login')


@method_decorator(login_required(login_url='login/'),name="dispatch")
class HomeView(View):
    def get(self,request):
        if self.request.user.groups.filter(name='M').exists():
            return render(request,'./templates/home.html')
        else:
            messages.info(request,'You are not authorized to access this page.')
            return redirect('account_login')
# @method_decorator(login_required(login_url='login/'),name="dispatch")
def create_post(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("home")
    else:
        form =PostForm()

    return render(request, "create_post.html", {"form":form})

def projects(request):
    posts=Post.objects.all()
    return render(request, 'all_projects.html',  {"posts":posts})
class ProjectDetailView(DetailView):
    model=Post
    template_name="project.html"
    form_class=PostForm
    def project(request):
        posts=Post.objects.all()
        if request.method=="POST":
            post_id=request.POST.get("post-id")
            post=Post.objects.filter(id=post_id).first()
            if post and post.author == request.user:
                post.delete()
        return render(request, 'all_projects.html', {"posts":posts})

class UpdatePostView(UpdateView):
    model=Post
    form_class=UpdatePostForm
    template_name="change_project.html"


class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy("home")
def Post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('project_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'change_project.html', {'form': form})
# def commit(request):
#     model=Post
#     post=Post.objects.filter(id=post_id).first()
#     return render(request, "commit.html" , {"post":post})

class commit(DetailView):
    model=Post
    template_name="commit.html"
    form_class=PostForm


