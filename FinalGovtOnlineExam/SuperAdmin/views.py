from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from .forms import MinistryForm
from .models import Ministry


def SuperAdminHome(request):
    return render(request,'SuperAdmin/SuperAdminNavbar.html')


def ministry_list(request):
    ministrys = Ministry.objects.all()
    return render(request, 'SuperAdmin/Ministry/ministry_list.html', {'ministrys': ministrys})


def save_ministry_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            ministrys = Ministry.objects.all()
            data['html_ministry_list'] = render_to_string('SuperAdmin/Ministry/partial_ministry_list.html', {'ministrys': ministrys })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def ministry_create(request):
    if request.method == 'POST':
        form = MinistryForm(request.POST)
    else:
        form = MinistryForm()
    return save_ministry_form(request, form, 'SuperAdmin/Ministry/partial_ministry_create.html')


def ministry_update(request, pk):
    ministry = get_object_or_404(Ministry, pk=pk)
    if request.method == 'POST':
        form = MinistryForm(request.POST, instance=ministry)
    else:
        form = MinistryForm(instance=ministry)
    return save_ministry_form(request, form, 'SuperAdmin/Ministry/partial_ministry_update.html')


def ministry_delete(request, pk):
    ministry = get_object_or_404(Ministry, pk=pk)
    data = dict()
    if request.method == 'POST':
        ministry.delete()
        data['form_is_valid'] = True
        ministrys = Ministry.objects.all()
        data['html_ministry_list'] = render_to_string('SuperAdmin/Ministry/partial_ministry_list.html', {'ministrys': ministrys })
    else:
        context = {'ministry': ministry}
        data['html_form'] = render_to_string('SuperAdmin/Ministry/partial_ministry_delete.html', context, request=request)
    return JsonResponse(data)


from django.shortcuts import render

# def AddMinistry(request, template_name='SuperAdmin/datatable_button_example.html'):
#     contact_list = Ministry.objects.all()
#     form = MinistryForm(request.POST or None)
#     if form.is_valid():
#         form.instance.username = request.user
#         form.save()
#         messages.success(request, f'Your Ministry has been Created Successfully')
#         return redirect('Ministry')
#     context = {
#         'form': form,
#         'contact_list': contact_list
#     }
#     return render(request, template_name, context)
#
#
# def updateMinistry(request, pk, template_name='SuperAdmin/MinistryEdit.html'):
#     ministry = get_object_or_404(Ministry, pk=pk)
#     form = MinistryForm(request.POST or None, instance=ministry)
#     if form.is_valid():
#         form.save()
#         messages.success(request, f'Your Ministry Account Successfully Update')
#         return redirect('Ministry')
#     # else:
#     #     messages.warning(request, f'Your Ministry Account Not Successfully Update')
#     return render(request, template_name, {'edit_form': form})
#
#
# def deleteMinistry(request, pk, template_name='SuperAdmin/datatable_button_example.html'):
#     ministry = get_object_or_404(Ministry, pk=pk)
#     if request.method == 'POST':
#         ministry.delete()
#         messages.success(request, f'Your Ministry has been Deleted Successfully')
#         return redirect('Ministry')
#     return render(request, template_name, {'object': ministry})


