"""Task URL Configuration

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
from django.views.generic import TemplateView

from apollo_task import settings
from user_app import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', TemplateView.as_view(template_name='user/user_login_page.html'),name='user'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('change_pwd/',views.change_pwd,name='change_pwd'),
    path('save_pwd/',views.save_pwd,name='save_pwd'),
    path('viewtask/',views.view_task,name='viewtask'),
    path('task_completed/',views.task_completed,name='task_completed')

]