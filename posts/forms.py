from django import forms
from .models import Post

class add_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'