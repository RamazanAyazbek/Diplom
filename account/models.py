from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post_create(models.Model):
    title=models.CharField(max_length=200)
    # code_window=models.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title +"\n" +  self.description + "\n"
    def get_absolute_url(self):
        # return reverse('project_view', args=[str(self.id)])
        return reverse('update_post', kwargs={"id" : str(self.id)})

class Version(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='versions')
    version_number = models.IntegerField()
    description = models.TextField()
    title = models.CharField(max_length=200, default='Untitled')
    updated_at=models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.post.title} - Version {self.version_number}"




