from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed


app_name = 'blog'

# create of pathes or urls
urlpatterns=[
    path('', blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('author/',blog_view,name='author'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('author/<str:author_username>', blog_view, name = 'author'),
    #path('category/<str:cat_name>',blog_category,name='category'),
    path('search/', blog_search, name = 'search'),
    path('tag/<str:tag_name>', blog_view, name = 'tag'),
    path("rss/feed/", LatestEntriesFeed()),
    path('test',  test, name = 'test'),
]