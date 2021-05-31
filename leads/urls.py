from django.urls import path
from .views import lead, lead_detail, create_lead, update_lead, delete_lead

app_name = 'leads'

urlpatterns = [
    path('', lead),
    path('detail/<int:pk>/', lead_detail),
    path('create/', create_lead),
    path('update/<int:pk>', update_lead, name='update'),
    path('delete/<int:pk>', delete_lead, name='delete'),


    
]
