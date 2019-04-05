from django.contrib import admin

from blog.models import blog
from .models import job
# Register your models here.
admin.site.register(job)
admin.site.register(blog)