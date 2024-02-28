from django.contrib import admin
from blog.models import Article, Person, Category

admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Category)

