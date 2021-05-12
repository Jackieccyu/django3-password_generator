"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from generator import views

urlpatterns = [
    # 如果要在此處創建自己的自定義頁面，我們首先必須說path是，在這種情況下是一個空字符串，然後是一個逗號
    path('', views.home, name='home'),
    # 從generatedpassword/ 改成password/
    path('password/', views.password, name='password'),

    path('about/', views.about, name='about'),

]
