from django.urls import path
from . import views
app_name='app'

urlpatterns = [
    path ('',views.get_master, name="master"),
    
]