from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()
@register.inclusion_tag('website/latest_from_our_blog.html')
def latest_from_our_blog():
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    return {'posts': posts}