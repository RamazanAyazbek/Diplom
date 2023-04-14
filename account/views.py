
from .forms import UserForm, PostForm,UpdatePostForm
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Version
from django.urls import reverse,reverse_lazy
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
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
        return render(request,'./templates/home.html')
    # def get(self,request):
    #     if self.request.user.groups.filter(name='M').exists():
    #         return render(request,'./templates/home.html')
    #     else:
    #         messages.info(request,'You are not authorized to access this page.')
    #         return redirect('account_login')
# @method_decorator(login_required(login_url='login/'),name="dispatch")
def create_post(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        email="ramazan.ayazbek.kz@gmail.com"
        message="Created new post"
        name_user=request.user 
        letter=str(name_user)+" created by"
        send_mail(
        letter,
        message, 
        'settings.EMAIL_HOST_USER',
        [email])
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
    context={
        "posts":posts
    }
    return render(request, 'all_projects.html',  context)
def user(request):
    User=get_user_model()
    users=User.objects.all()
    context={
        "users":users
    }
    return render(request, 'user.html',  context)
# class ProjectDetailView(DetailView):
#     model=Post
#     template_name="project.html"
#     form_class=PostForm
#     def project(request):
#         posts=Post.objects.all()
#         if request.method=="POST":
#             post_id=request.POST.get("post-id")
#             post=Post.objects.filter(id=post_id).first()
#             if post and post.author == request.user:
#                 post.delete()
#         return render(request, 'all_projects.html', {"posts":posts})

def view_post(request, id):
    get_post=Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    versions = post.versions.order_by('-timestamp')
    return render(request, 'project.html', {'post': post, 'versions': versions})



def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        message=request.POST["message"]
        email=request.POST["email"]
        name_user=request.user
        letter=str(name_user) + ' Project changed from Maks'
        # email="ramazan.ayazbek.kz@gmail.com"
        send_mail(
        letter, 
        message, 
        'settings.EMAIL_HOST_USER',
        [email])
        version_number = post.versions.count() + 1
        post_version = Version(post=post,version_number=version_number, description=post.description)
        post_version.save()
        # form_class=Post
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('project_view', id=post.id)
    else:
        form = UpdatePostForm(instance=post)
    versions = post.versions.order_by('-timestamp')
    context = {
        'form': form,
        'versions': versions,
    }
    return render(request, 'update_post.html', context)


class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy("home")


# def send_email(request):
#     if request.method =="POST":
#         message=request.POST["message"]
#         email="ramazan.ayazbek.kz@gmail.com"
        
#         send_mail(
#         'Contact Form', 
#         message, 
#         'settings.EMAIL_HOST_USER',
#         [email]
#         )







# from django.http import JsonResponse
# import smtplib
# from email.mime.text import MIMEText
# import json

# def send_email(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         to_email = data['to_email']
#         from_email = data['from_email']
#         subject = data['subject']
#         body = data['body']

#         msg = MIMEText(body)
#         msg['Subject'] = subject
#         msg['From'] = from_email
#         msg['To'] = to_email

#         try:
#             smtp_server = smtplib.SMTP('maksplank351@gmail.com', 587)
#             smtp_server.starttls()
#             smtp_server.login(from_email, 'Ramazan1901')
#             smtp_server.sendmail(from_email, to_email, msg.as_string())
#             smtp_server.quit()
#             return JsonResponse({'status': 'ok'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})

