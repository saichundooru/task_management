"""apollo_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from admin_app import views
from apollo_task import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',views.home_page,name='main'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('user_page/',views.user_page,name='user_page'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('create_user/',views.create_user,name='create_user'),
    path('saving_userdetails/',views.saving_userdetails,name='saving_userdetails'),
    path('view_users/',views.view_users,name='view_users'),
    path('assign_task/',views.assign_task,name='assign_task'),
    path('view_task/',views.view_task,name='view_task'),
    path('save_task/',views.save_task,name='save_task'),
    path('delete/',views.delete,name='delete')


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
