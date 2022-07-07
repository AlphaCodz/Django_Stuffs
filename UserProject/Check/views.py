from django.shortcuts import render


# Create your views here.
def KYC(request):
    
    return render(request, 'KYC.html')

# def pending(request):
#     return render(request, 'Pending.html')