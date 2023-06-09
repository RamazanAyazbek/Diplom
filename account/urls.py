from django.urls import path
from .views import LoginView, LogoutView,HomeView,DeletePostView
from .views import create_post, projects, update_post,view_post, user
from . import views

from .feeds import LatestPostsFeed
# app_name='account'
urlpatterns = [
    path('login/', LoginView.as_view(),name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('', HomeView.as_view(),name='home'),
    path('create-project/', create_post, name="create_project"),
    path('project/<int:id>', view_post, name='project_view'),
    path('projects/', projects, name="projects"),
    path('users/', user, name="users"),
    path('update_post/<int:id>', update_post, name='update_post'),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name='delete_project'),
    path('feed/', LatestPostsFeed(), name="rss_feed"),
]
