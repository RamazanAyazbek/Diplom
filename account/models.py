from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)
    def __str__(self):
        return self.title +"\n" +  self.description + "\n" + self.version
    def get_absolute_url(self):
        return reverse('project_view', kwargs={"pk": self.pk})
    def save(self, *args, **kwargs):
        # check if the name already exists
        if self.pk is None and Post.objects.filter(title=self.title).exists():
            # if creating a new record and name already exists, raise an error
            raise ValidationError("Title must be unique")
        elif self.pk is not None:
            # if updating an existing record, save a new version
            original = Post.objects.get(pk=self.pk)
            if original.title != self.title or original.description != self.description:
                self.pk = None
                self.version = original.version + 1 
        super(Post, self).save(*args, **kwargs)



