from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from .forms import MinistryForm, GovtSignUpForm, GovtSignUpUpdateForm, StudentSignUpUpdateForm, TeacherSignUpUpdateForm
from .models import Ministry
from django.shortcuts import render
from accounts.forms import UserUpdateForm, ChangeEmailForm
from django.views.generic import View, FormView
from django.conf import settings
from django.utils.crypto import get_random_string
from accounts.models import Activation
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from accounts.utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from .filters import GovtUserFilter
from django.contrib.auth import get_user_model
User = get_user_model()


def SuperAdminHome(request):
    student_count = User.objects.all()
    student = student_count.filter(is_student=True, ).count()
    teacher = student_count.filter(is_trainer=True).count()
    government_employee = student_count.filter(is_governmentEmployee=True).count()
    context = {
        'student': student,
        'teacher': teacher,
        'government_employee': government_employee,

    }
    return render(request,'SuperAdmin/Home.html',context)


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
    return render(request, 'SuperAdmin/Profile/SuperAdminProfile.html', context)


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
    template_name = 'SuperAdmin/GovtEmployee/partial_employee_create.html'
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

        return redirect('employee_list')


def employee_list(request):
    employees = User.objects.all()
    MyFilter = GovtUserFilter(request.GET,queryset=employees)
    employees = MyFilter.qs
    context = {
        'employees': employees,
        'MyFilter':MyFilter,
    }
    return render(request, 'SuperAdmin/GovtEmployee/employee_list.html', context)


def employee_update(request,pk):
    course = get_object_or_404(User, pk=pk)
    form = GovtSignUpUpdateForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "User Updated Successfully")
        return redirect("employee_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'SuperAdmin/GovtEmployee/partial_employee_update.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = User.objects.all()
        data['html_employee_list'] = render_to_string('SuperAdmin/GovtEmployee/partial_employee_list.html',
                                                      {'employees': employees })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('SuperAdmin/GovtEmployee/partial_employee_delete.html', context, request=request)
    return JsonResponse(data)


def employee_view(request, pk):
    employee = get_object_or_404(User, pk=pk)
    data = dict()
    context = {'employee': employee}
    data['html_form'] = render_to_string('SuperAdmin/GovtEmployee/partial_employee_view.html', context, request=request)
    return JsonResponse(data)


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'SuperAdmin/Profile/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(self.request, f'To complete the change of email address, click on the link sent to it.')
        else:
            user.email = email
            user.save()

            messages.success(self.request, f'Email successfully changed.')

        return redirect('SuperAdmin_change_email')


class ChangeEmailActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, f'You have successfully changed your email!')

        return redirect('SuperAdmin_change_email    ')


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'SuperAdmin/Profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('log_in')


def student_list(request):
    students = User.objects.all()
    return render(request, 'SuperAdmin/Student/student_list.html', {'students': students})


def student_view(request, pk):
    student = get_object_or_404(User, pk=pk)
    data = dict()
    context = {'student': student}
    data['html_form'] = render_to_string('SuperAdmin/Student/partial_student_view.html', context, request=request)
    return JsonResponse(data)


def student_update(request,pk):
    student = get_object_or_404(User, pk=pk)
    form = StudentSignUpUpdateForm(request.POST or None, request.FILES or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "User Updated Successfully")
        return redirect("super_admin_student_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'SuperAdmin/Student/partial_student_update.html', {'form': form})


def teacher_list(request):
    teachers = User.objects.all()
    return render(request, 'SuperAdmin/Teacher/teacher_list.html', {'teachers': teachers})


def teacher_view(request, pk):
    teacher = get_object_or_404(User, pk=pk)
    data = dict()
    context = {'teacher': teacher}
    data['html_form'] = render_to_string('SuperAdmin/Teacher/partial_teacher_view.html', context, request=request)
    return JsonResponse(data)


def teacher_update(request,pk):
    teacher = get_object_or_404(User, pk=pk)
    form = TeacherSignUpUpdateForm(request.POST or None, request.FILES or None, instance=teacher)
    if form.is_valid():
        form.save()
        messages.success(request, "User Updated Successfully")
        return redirect("super_admin_teacher_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'SuperAdmin/Teacher/partial_teacher_update.html', {'form': form})
