from django.shortcuts import render, reverse
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from leads.models import Agent
from .forms import AgentModelForm

# Create your views here.
class AgentListView(ListView):
    queryset            = Agent.objects.all()
    context_object_name = "agents"
    template_name       = 'agents/agent_list.html'


class AgentCreateView(CreateView):
    form_class    = AgentModelForm
    template_name = 'agents/agent_create.html'

    def get_success_url(self):
        return reverse('agents:list')


class AgentDetailView(DetailView):
    queryset            = Agent.objects.all()
    context_object_name = "agent"
    template_name       = 'agents/agent_detail.html'


class AgentUpdateView(UpdateView):
    form_class    = AgentModelForm
    queryset      = Agent.objects.all()
    template_name = 'agents/agent_update.html'

    def get_success_url(self):
        return reverse('agents:list')


class AgentDeleteView(DeleteView):
    queryset      = Agent.objects.all()
    template_name = 'agents/agent_delete.html'

    def get_success_url(self):
        return reverse('agents:list')