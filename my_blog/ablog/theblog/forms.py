from django import forms
from .models import Post, Category, Comment


    
choices = Category.objects.all().values_list('name','name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'author','category',
            'tags',
            'content','is_featured',
            'is_featured_header',
            'trending',
            'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),            
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content', 'is_featured', 'is_featured_header', 'trending')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('content',)

