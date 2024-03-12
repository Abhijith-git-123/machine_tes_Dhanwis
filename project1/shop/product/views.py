from django.shortcuts import render
from .models import *
from .forms import regForm 


# def form1(request):
#     doc = {
#         'reg' : register.objects.all()
#     }
#     return render(request,'forms.html',doc)

def register1(request):
    dop = {
        'rr' : register.objects.all()
    }
    return render(request,'register.html',dop)



def register1(request):
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            
            form.save()
            return render(request, 'register.html')
    else:
        form = regForm()

    return render(request, 'register.html', {'form': form})




