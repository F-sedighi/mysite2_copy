from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings


User = get_user_model()

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
        
class Post(models.Model):
   
    image = models.ImageField(upload_to = 'blog/', default = 'blog/default.jpg')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # title

    title = models.CharField(max_length = 255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default = 0) # default = 0
    status = models.BooleanField(default = False)
    login_require = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    
    class Meta:
        
        ordering = ['created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = "پست ها"

    def __str__(self):
        return "{} - {}".format(self.title,self.id)
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    approved = models.BooleanField(default = False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name
    
     