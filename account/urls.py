from django.urls import path
from .views import LoginView, LogoutView,HomeView,UpdatePostView,ProjectDetailView,DeletePostView,commit
from .views import create_post, projects, Post_edit
from . import views
urlpatterns = [
    path('login/', LoginView.as_view(),name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('', HomeView.as_view(),name='home'),
    path('create-project/', create_post, name="create_project"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_view'),
    path('projects/', projects, name="projects"),
    path('change_post/<int:pk>', Post_edit, name='change_project'),
    # path('commits_post/<int:pk>', commit.as_view(), name='commit_project'),
    #path('change_post/<int:pk>', UpdatePostView.as_view(), name='change_project'),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name='delete_project')
]
