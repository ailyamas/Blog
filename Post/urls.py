from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index" ),
    path('detail/<int:pk>',views.detail, name="detail" ) ,
    path('addPost',views.createPost, name="add-Post" ),
    path('Update_post/<int:pk>',views.UpdatePost, name="update-Post" ) ,
    path('Delete_post/<int:pk>',views.deletePost, name="delete-Post" ) ,
]