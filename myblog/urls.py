"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.contrib import admin
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)), # Redirect root URL to /blog/
]

# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blog/', include('blog.urls')),
#     # path('login/', auth_views.LoginView.as_view(), name='login'),
#     # # path('', RedirectView.as_view(url='/blog/', permanent=True)),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('accounts/', include('django.contrib.auth.urls')), 
#     # path('login/', auth_views.LoginView.as_view(), name='login'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('logout/', logout_view, name='logout'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]# Add this line

# # myblog/urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blog/', include('blog.urls')),  # Include the blog app's URLs
# ]

