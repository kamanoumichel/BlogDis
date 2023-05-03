from django.contrib import admin
from .models import Post,Comment,Contact,Category
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('titre','slug','body','date_publication','auteur','image')
    prepopulated_fields = {'slug': ('titre',)}
            
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','nom','email','commentaire','date_creation','date_modify')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','sujet','message')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('nom','slug')
    prepopulated_fields = {'slug': ('nom',)}


admin.site.site_title=gettext_lazy("Amaba Discovery Zone")
admin.site.site_header=gettext_lazy("Amaba Discovery Zone")
admin.site.index_title=gettext_lazy("Amaba Discovery Zone")