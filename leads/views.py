from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Lead, User, Agent
from .forms import LeadForm, CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
################################
def lead_list(request):
    leads = Lead.objects.all()

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
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
            return redirect('leads:list')
    else:
        form = LeadForm()

    context = {'form':form}
    return render(request, 'leads/create_lead.html', context)


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