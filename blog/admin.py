from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #atributos/exibidos

    list_filter = ('status', 'created', 'publish', 'author') # filtro
    search_fields = ('title', 'body') # pesquisar
    prepopulated_fields = {'slug': ('title',)} # slug automatico
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' # filtrando por ano da publicação.
    ordering = ('status', 'publish') # atalho para publicação.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


