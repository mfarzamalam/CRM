from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Lead, User, Agent
from .forms import LeadForm, CustomUserCreationForm, AssignAgentForm
from django.views.generic import TemplateView, CreateView, FormView
from agents.mixin import OrganisorAndLoginRequiredMixin
################################
def lead_list(request):
    if request.user.is_organisor:
        leads = Lead.objects.filter(organisation=request.user.userprofile, agent__isnull=False)
        unassigned_leads = Lead.objects.filter(organisation=request.user.userprofile, agent__isnull=True)
        # print(unassigned_leads.count())
        context = {'leads':leads, 'unassigned_leads':unassigned_leads}
    else:
        leads = Lead.objects.filter(organisation=request.user.agent.organisation, agent__isnull=False)
        context = {'leads':leads}

    return render(request, 'leads/lead_list.html', context)



class LandingPageView(TemplateView):
    template_name   = 'leads/home.html'

    
################################
def lead_detail(request, pk):
    lead = Lead.objects.filter(pk=pk)

    context = {'leads':lead}
    return render(request, 'leads/lead_details.html', context)


###############################
def create_lead(request):
    if request.user.is_organisor:
        if request.method == "POST":
            form = LeadForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                age = form.cleaned_data['age']

                organisation = request.user.userprofile
                
                Lead.objects.create(first_name=first_name, last_name=last_name, age=age, organisation=organisation)
                return redirect('leads:list')
        else:
            form = LeadForm()

        context = {'form':form}
        return render(request, 'leads/create_lead.html', context)
    else:
        return redirect('leads:list')

##################################
def update_lead(request, pk):
    # lead = Lead.objects.get(pk=pk)
    lead = Lead.objects.filter(pk=pk)
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']

            # lead.first_name = first_name
            # lead.last_name  = last_name
            # lead.age        = age
            # lead.save()

            lead = Lead.objects.filter(pk=pk).update(first_name=first_name,last_name=last_name,age=age)
            return redirect('leads:list')
    else:
        form = LeadForm()

    context = {'form':form}
    return render(request, 'leads/update_lead.html', context)


#####################################
def delete_lead(request,pk):
    lead = Lead.objects.filter(pk=pk)
    lead.delete()

    return redirect('leads:list')


#######################################
class SignupView(CreateView):
    template_name = 'leads/registration/signup.html'
    form_class    = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class AssignAgentView(OrganisorAndLoginRequiredMixin, FormView):
    template_name = 'leads/lead_assign.html'
    form_class    = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({
            'request':self.request
        })
        return kwargs

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead  = Lead.objects.get(id=self.kwargs['pk'])
        print(lead, agent)
        lead.agent = agent
        lead.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('leads:list')