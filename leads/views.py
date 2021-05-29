from django.shortcuts import render, HttpResponse, redirect
from .models import Lead, Agent, User
from .forms import LeadForm

# Create your views here.
def lead(request):
    leads = Lead.objects.all()

    context = {'leads':leads}
    return render(request, 'leads/lead.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.filter(pk=pk)

    context = {'lead':lead}
    return render(request, 'leads/lead_details.html', context)


def create_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
            return redirect('/leads/')
    else:
        form = LeadForm()

    context = {'form':form}
    return render(request, 'leads/create_lead.html', context)