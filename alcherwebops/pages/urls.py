from django.contrib import admin
from django.urls import path
from .views import PostListView,PostCreateView,PostDetailView,MyPostsListView
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page,name='home-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('profile/',PostListView.as_view(),name='profile-page'),
    path('upload/',PostCreateView.as_view(),name='upload-page'),
    path('myposts/',MyPostsListView.as_view(),name='my-posts-page'),
    path('updateprofile',views.update_profile,name="update-profile-page"),
    path('fav/<int:id>/',views.favourite_add,name='favourite_add'),
    path('favourites/',views.favourite_list,name='favourite_list')

]


