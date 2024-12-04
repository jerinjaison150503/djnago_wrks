from django.urls import path
from . import views

urlpatterns=[
    path('userlogin',views.userlogin),
    path('userhome',views.userhome),
    path('userreg',views.userreg),
    path('admlogin',views.admlogin),
    path('admhome',views.admhome),
    
    
]