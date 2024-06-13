# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
# from django.urls import path
# from .views import (
#     index, create_post, post_detail, edit_post, delete_post,
#     logout_view  # Import the logout_view function here
# )

# urlpatterns = [
#     path('', index, name='index'),
#     path('create/', create_post, name='create_post'),
#     path('<int:pk>/', post_detail, name='detail'),
#     path('<int:pk>/edit/', edit_post, name='edit_post'),
#     path('<int:pk>/delete/', delete_post, name='delete_post'),
#     # path('logout/', logout_view, name='logout'),  # Add the logout URL pattern
#     # path('logout/', logout_view, name='logout'),  # Ensure this line is present
# ]