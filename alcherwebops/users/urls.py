from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),



]
'''
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth.views import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name="register")
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]   


'''