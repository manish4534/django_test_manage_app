from django.contrib import admin
from .models import Category,Post

# Register your models here.

# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'post_id', 'url',)
    search_fields = ('title', )
    list_filter = ('cat', )
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

