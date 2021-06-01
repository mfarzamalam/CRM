from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Lead, Agent, User
from .forms import LeadModelForm
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView, CreateView

# Create your views here.
################################
# def lead(request):
#     leads = Lead.objects.all()

#     context = {'leads':leads}
#     return render(request, 'leads/lead.html', context)

class LandingPageView(TemplateView):
    template_name   = 'leads/home.html'


class LeadListView(ListView):
    queryset            = Lead.objects.all()
    context_object_name = "leads"
    template_name       = 'leads/lead_list.html'

    
################################
# def lead_detail(request, pk):
#     lead = Lead.objects.filter(pk=pk)

#     context = {'lead':lead}
#     return render(request, 'leads/lead_details.html', context)

class LeadDetailView(DetailView):
    template_name       =  'leads/lead_details.html'
    queryset            =   Lead.objects.all()
    context_object_name =   "lead"



###############################
# def create_lead(request):
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
#             return redirect('/leads/')
#     else:
#         form = LeadForm()

#     context = {'form':form}
#     return render(request, 'leads/create_lead.html', context)

class LeadCreateView(CreateView):
    template_name = 'leads/create_lead.html'
    form_class    = LeadModelForm

    def get_success_url(self):
        return reverse('leads:list')



##################################
# def update_lead(request, pk):
#     # lead = Lead.objects.get(pk=pk)
#     lead = Lead.objects.filter(pk=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             # lead.first_name = first_name
#             # lead.last_name  = last_name
#             # lead.age        = age
#             # lead.save()

#             lead = Lead.objects.filter(pk=pk).update(first_name=first_name,last_name=last_name,age=age)
#             return redirect('/leads/')
#     else:
#         form = LeadForm()

#     context = {'form':form}
#     return render(request, 'leads/update_lead.html', context)

class LeadUpdateView(UpdateView):
    template_name = 'leads/update_lead.html'
    form_class    = LeadModelForm
    queryset      = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:list')    



#####################################
# def delete_lead(request,pk):
#     lead = Lead.objects.filter(pk=pk)
#     lead.delete()

#     return redirect('/leads')


class LeadDeleteView(DeleteView):
    template_name   = 'leads/delete_lead.html'
    queryset        = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:list')