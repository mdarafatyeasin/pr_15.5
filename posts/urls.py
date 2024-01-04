from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addPost, name='add_post'),
    path('edit/<int:id>', views.editPost, name='edit_post'),
    path('delete/<int:id>', views.deletePost, name='delete_post'),
]