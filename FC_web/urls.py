"""FC_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ASTA_web import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_request),
    path('register/', views.register_request),
    path('user<int:uid>/', views.user_request),
    path('user<int:uid>/notice/', views.notice_request),
    path('user<int:uid>/upload/', views.upload_request),
    path('user<int:uid>/writeblog/', views.writeblog_request),
    path('user<int:uid>/visit<int:vid>/', views.visit_request),
    path('user<int:uid>/delete/<int:id>/<str:type>/', views.delete_request),
    path('download/<int:id>/', views.download_request)
]

# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
