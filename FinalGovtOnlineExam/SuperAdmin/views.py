from django.shortcuts import render

# Create your views here.


def SuperAdminHome(request):
    return render(request,'SuperAdmin/SuperAdminNavbar.html')
