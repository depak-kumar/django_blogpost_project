#pub_date']  # Include pub_date here
from django import forms
from .models import PostModel
from django import forms
# from .models import YourPostModel

# class YourPostForm(forms.ModelForm):
#     class Meta:
#         model = YourPostModel
#         fields = ['title', 'content']

#     def __init__(self, *args, **kwargs):
#         super(YourPostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs['class'] = 'form-control'
#         self.fields['content'].widget.attrs['class'] = 'form-control'

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'pub_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
# blog/forms.py

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
# # blog/forms.py

# from django import forms
# from .models import BlogPost

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'content', 'pub_date']
