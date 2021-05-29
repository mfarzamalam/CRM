from django.urls import path
from .views import lead, lead_detail, create_lead

app_name = 'leads'

urlpatterns = [
    path('', lead),
    path('detail/<int:pk>/', lead_detail),
    path('create/', create_lead),
]
