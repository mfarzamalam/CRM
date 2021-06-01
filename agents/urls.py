from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = "agents"

urlpatterns = [
    path('list/', AgentListView, name='list'),
]