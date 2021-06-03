import random
from django.shortcuts import render, reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm
from .mixin import OrganisorAndLoginRequiredMixin


# Create your views here.
class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    # queryset            = Agent.objects.all()
    context_object_name = "agents"
    template_name       = 'agents/agent_list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    form_class    = AgentModelForm
    template_name = 'agents/agent_create.html'

    def get_success_url(self):
        return reverse('agents:list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(f"{random.randint(0,10000)}")
        user.is_agent = True
        user.is_organisor = False
        user.save()
        Agent.objects.create(user=user, organisation=self.request.user.userprofile)

        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    queryset            = Agent.objects.all()
    context_object_name = "agent"
    template_name       = 'agents/agent_detail.html'


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    form_class    = AgentModelForm
    queryset      = Agent.objects.all()
    template_name = 'agents/agent_update.html'

    def get_success_url(self):
        return reverse('agents:list')


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    queryset      = Agent.objects.all()
    template_name = 'agents/agent_delete.html'

    def get_success_url(self):
        return reverse('agents:list')