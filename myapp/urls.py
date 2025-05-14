"""
URL configuration for maiin project.

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

from django.urls import path
from myapp.views import (
    dashboard, 
    pemainbola_list, 
    pemainbola_add, pemainbola_update,pemainbola_delete, klub_list, klub_add, klub_detail, 
    klub_update, klub_delete)

from myapp.autentikasi import akun_login


urlpatterns =[
    path('', dashboard, name="dashboard"),
    path('pemainbola/list', pemainbola_list, name="pemainbola_list"),
    path('pemainbola/add', pemainbola_add, name="pemainbola_add"),
    path('pemainbola/update/<int:id_pemain>', pemainbola_update, name="pemainbola_update"),
    path('pemainbola/delete/<int:id_pemain>', pemainbola_delete, name="pemainbola_delete"),

    path('klub/list/', klub_list, name="klub_list"),
    path('klub/add/', klub_add, name="klub_add"),
    path('klub/detail/<int:id_klub>', klub_detail, name="klub_detail"),    
    path('klub/update/<int:id_klub>', klub_update, name="klub_update"), 
    path('klub/delete/<int:id_klub>', klub_delete, name="klub_delete"), 

    path('autentikasi/login', akun_login, name="akun_login")
]
