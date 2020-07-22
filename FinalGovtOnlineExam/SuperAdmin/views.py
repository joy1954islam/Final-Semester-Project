from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from .forms import MinistryForm, GovtSignUpForm
from .models import Ministry
from django.shortcuts import render
from accounts.forms import UserUpdateForm
from django.views.generic import View, FormView
from django.conf import settings
from django.utils.crypto import get_random_string
from accounts.models import Activation
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from accounts.utils import (
    send_activation_email,
)
from django.contrib.auth import get_user_model
User = get_user_model()


def SuperAdminHome(request):
    return render(request,'SuperAdmin/SuperAdminNavbar.html')



def SuperAdminProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('SuperAdminProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'SuperAdmin/SuperAdminProfile.html', context)


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


class GovtSignUpView(FormView):
    template_name = 'SuperAdmin/GovtEmployee/partial_govtemployee_create.html'
    form_class = GovtSignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.DISABLE_USERNAME:
            user.username = f'user_{user.id}'
            user.save()

        if settings.ENABLE_USER_ACTIVATION:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.save()

            send_activation_email(request,user.email, code)

            messages.success(request,f'Account is Created and You are signed up. To activate the account, follow the '
                                     f'link sent to the mail.')
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,f'You are successfully signed up!')

        return redirect('govtemployee_list')


def govtemployee_list(request):
    govtemployees = User.objects.all()
    return render(request, 'SuperAdmin/GovtEmployee/govtemployee_list.html', {'govtemployees': govtemployees})


def govtemployee_delete(request, pk):
    govtemployee = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        govtemployee.delete()
        data['form_is_valid'] = True
        govtemployees = User.objects.all()
        data['html_govtemployee_list'] = render_to_string('SuperAdmin/GovtEmployee/partial_govtemployee_list.html', {'govtemployees': govtemployees })
    else:
        context = {'govtemployee': govtemployee}
        data['html_form'] = render_to_string('SuperAdmin/GovtEmployee/partial_govtemployee_delete.html', context, request=request)
    return JsonResponse(data)






