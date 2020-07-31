from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model
from ckeditor.widgets import CKEditorWidget

from api.models import Post


User = get_user_model()


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


# Register your models here.
admin.site.register(User)
admin.site.register(Post, PostAdmin)
