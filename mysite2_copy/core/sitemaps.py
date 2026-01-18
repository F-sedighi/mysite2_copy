from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['core:index', 'core:about', 'core:contact']
    
    def location(self, item):
        return reverse(item)