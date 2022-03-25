from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context ={
        "leads":leads
    }
    return render(request,"leads/lead_list.html",context)


def lead_detail(request , pk):
    lead = Lead.objects.get(id=pk)
    context={
        "lead":lead
    }
    print(pk)
    return render(request,"leads/lead_detail.html",context)


def lead_create(request):
    print(request.POST)

    if request.method == "POST":
        print("Recieving Post Data")
        form= LeadForm(request.POST)
        if form.is_valid():
            print("the form is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
    context = {
        "form":form
    }
    return render(request,"leads/lead_create.html",context)