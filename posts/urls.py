from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('',views.IndexView.as_view(),name='user_index'),
    path('list/<str:username>/',views.UserPostList.as_view(),name='user_posts'),
    path('list/detail/<int:pk>/',views.UserPostDetail.as_view(),name='user_posts_detail'),
    path('new/',views.UserPostCreate.as_view(),name='user_posts_create'),
    path('list/update/<int:pk>/',views.UserPostUpdate.as_view(),name='user_posts_update'),
    path('list/delete/<int:pk>/',views.UserPostDelete.as_view(),name='user_posts_delete'),
]