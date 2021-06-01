from django.urls import path
from .views import lead_list, lead_detail, create_lead, update_lead, delete_lead

app_name = 'leads'

urlpatterns = [
    path('list/', lead_list, name='list'),
    path('create/', create_lead, name='create'),
    path('detail/<int:pk>/', lead_detail, name='detail'),
    path('update/<int:pk>', update_lead, name='update'),
    path('delete/<int:pk>', delete_lead, name='delete'),
]