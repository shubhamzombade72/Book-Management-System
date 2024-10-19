from django.contrib import admin
from django.urls import path
from book import views
from BMS import bookview 
from BMS import loginview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.indexpage),

    path('b-list/', bookview.book),
    path('b-view/<id>', bookview.view),
    path('b-edit/<id>', bookview.edit),
    path('b-add/', bookview.Addbook),
    path('b-delete/<id>', bookview.delete),

    path('', loginview.Signup, name='signup'),
    path('login/', loginview.LoginPage, name='login'),
    # path('home/', loginview.HomePage, name='home'),
    # path('logout/', loginview.LogoutPage, name='logout'),
]
