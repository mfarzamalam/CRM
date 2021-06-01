from django.urls import path
# from .views import lead, lead_detail, create_lead, update_lead, delete_lead
from .views import LeadCreateView, LeadUpdateView, LeadDeleteView, LeadDetailView, LeadListView

app_name = 'leads'

urlpatterns = [
    # path('', lead),
    # path('detail/<int:pk>/', lead_detail),
    # path('create/', create_lead),
    # path('update/<int:pk>', update_lead, name='update'),
    # path('delete/<int:pk>', delete_lead, name='delete'),

    path('list/', LeadListView.as_view(), name='list'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='detail'),
    path('create/', LeadCreateView.as_view(), name='create'),
    path('update/<int:pk>', LeadUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', LeadDeleteView.as_view(), name='delete'),
]