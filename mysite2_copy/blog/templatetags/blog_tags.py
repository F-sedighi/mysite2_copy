from django import template
from  blog.models import Post, Category, Comment


register = template.Library()

@register.simple_tag
def hello():
    return 'hello'

@register.simple_tag
def function(a=5):
    return a + 2

@register.simple_tag(name = 'totalposts')
def func1():
    posts = Post.objects.filter(status = 1).order_by('published_date').count()
    return posts

@register.simple_tag(name = 'posts')
def func2():
    posts = Post.objects.filter(status = 1).order_by('published_date')
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id, approved=True).count()


@register.filter
def snippet(value, arg = 20):
    return value[:arg] + '...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status = 1).order_by('published_date')[:4]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1).order_by('published_date')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}


