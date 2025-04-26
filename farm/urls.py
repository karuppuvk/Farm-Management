from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
# from .views import view_data

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', login_required(dashboard), name='dashboard'),
    path('view-data/',view_data, name='view_data'),
    path('logout/', logout_view, name='logout'),  # Add this line
]