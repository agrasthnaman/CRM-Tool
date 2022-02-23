from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

# Create your views here.
def lead_list(request):
    # return HttpResponse("Hello World!")
    leads = Lead.objects.all()
    context = {
        "name" : "Agrasth Naman",
        "leads" : leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request,pk):
    # print(pk)
    leads = Lead.objects.get(id=pk)
    context = {
        "lead" : leads
    }
    # print(leads)
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    context = {
        "form" : LeadForm()
    }
    return render(request, 'leads/lead_create.html', context)