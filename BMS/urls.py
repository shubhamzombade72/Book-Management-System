"""
URL configuration for BMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from book import views
from BMS import bookview 
from BMS import loginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),

    
    path('b-list/',bookview.book),
    path('b-view/<id>',bookview.view),
    path('b-edit/<id>',bookview.edit),
    path('b-add/',bookview.Addbook),
    path('b-delete/<id>',bookview.delete),
    path('b-login/',bookview.loginForm),
    path('b-create/',bookview.CreateAcc),


    path('u-login/',loginView.AddReg),

    path('login/', loginView.LoginPage, name='login'),
    path('logout/', loginView.LogoutPage, name='logout'),
    path('home/', loginView.HomePage, name='home'),
   

]
