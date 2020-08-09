from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from GovernmentEmployee.forms import CourseForm, CourseContentForm, TeacherSignUpForm
from GovernmentEmployee.models import Course, CourseContent
from accounts.models import Activation
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from accounts.forms import UserUpdateForm, ChangeEmailForm
from django.views.generic import View, FormView
from accounts.utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.contrib.auth import get_user_model
User = get_user_model()


def Home_Course_View(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def Home_Teacher_View(request):
    users = User.objects.all()
    return render(request, 'Teacher.html', {'users': users})


def home(request):
    return render(request, 'GovernmentEmployee/home.html')


def GovernmentEmployeeHome(request):
    return render(request,'GovernmentEmployee/GovernmentEmployeeNavbar.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'GovernmentEmployee/Course/course_list.html', {'courses': courses})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Course Created Successfully")
            return redirect('course_list')
        else:
            messages.error(request, "Course Not Created Successfully")
    else:
        form = CourseForm()
    return render(request, 'GovernmentEmployee/Course/partial_course_create.html', {'form': form})


def course_update(request,pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "course Updated Successfully")
        return redirect("course_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'GovernmentEmployee/Course/partial_course_update.html', {'form': form})


def course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    data = dict()
    context = {'course': course}
    data['html_form'] = render_to_string('GovernmentEmployee/Course/partial_course_view.html', context, request=request)
    return JsonResponse(data)


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    data = dict()
    if request.method == 'POST':
        course.delete()
        data['form_is_valid'] = True
        courses = Course.objects.all()
        data['html_course_list'] = render_to_string('GovernmentEmployee/Course/partial_course_list.html', {'courses': courses })
    else:
        context = {'course': course}
        data['html_form'] = render_to_string('GovernmentEmployee/Course/partial_course_delete.html', context, request=request)
    return JsonResponse(data)


def GovernmentEmployeeProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('GovernmentEmployeeProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'GovernmentEmployee/Profile/GovernmentEmployeeProfile.html', context)


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'GovernmentEmployee/Profile/change_email.html'
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

        return redirect('GovernmentEmployee_change_email')


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

        return redirect('GovernmentEmployee_change_email')


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'GovernmentEmployee/Profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('log_in')


def topic_list(request):
    topics = CourseContent.objects.all()
    return render(request, 'GovernmentEmployee/CourseContent/content_list.html', {'topics': topics})


def save_topic_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Course Content Successfully")
            data['form_is_valid'] = True
            topics = CourseContent.objects.all()
            data['html_topic_list'] = render_to_string('GovernmentEmployee/CourseContent/partial_content_list.html', {'topics': topics })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def topic_create(request):
    if request.method == 'POST':
        form = CourseContentForm(request.POST)
    else:
        form = CourseContentForm()
    return save_topic_form(request, form, 'GovernmentEmployee/CourseContent/partial_content_create.html')


def topic_update(request, pk):
    topic = get_object_or_404(CourseContent, pk=pk)
    if request.method == 'POST':
        form = CourseContentForm(request.POST, instance=topic)
    else:
        form = CourseContentForm(instance=topic)
    return save_topic_form(request, form, 'GovernmentEmployee/CourseContent/partial_content_update.html')


def topic_delete(request, pk):
    topic = get_object_or_404(CourseContent, pk=pk)
    data = dict()
    if request.method == 'POST':
        topic.delete()
        data['form_is_valid'] = True
        topics = CourseContent.objects.all()
        data['html_topic_list'] = render_to_string('GovernmentEmployee/CourseContent/partial_content_list.html', {'topics': topics })
    else:
        context = {'topic': topic}
        data['html_form'] = render_to_string('GovernmentEmployee/CourseContent/partial_content_delete.html', context, request=request)
    return JsonResponse(data)


def teacher_list(request):
    teachers = User.objects.all()
    return render(request, 'GovernmentEmployee/Teacher/teacher_list.html', {'teachers': teachers})


# Teacher SignUp
class TeacherSignUpView(FormView):
    template_name = 'GovernmentEmployee/Teacher/partial_teacher_create.html'
    form_class = TeacherSignUpForm

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

            send_activation_email(request, user.email, code)

            messages.success(request,f'You are signed up. To activate the account, follow the link sent to the mail.')
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,f'You are successfully signed up!')

        return redirect('teacher_list')


def teacher_delete(request, pk):
    teacher = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        teacher.delete()
        data['form_is_valid'] = True
        teachers = User.objects.all()
        data['html_teacher_list'] = render_to_string('GovernmentEmployee/Teacher/partial_teacher_list.html', {'teachers': teachers })
    else:
        context = {'teacher': teacher}
        data['html_form'] = render_to_string('GovernmentEmployee/Teacher/partial_teacher_delete.html', context, request=request)
    return JsonResponse(data)


def teacher_view(request, pk):
    teacher = get_object_or_404(User, pk=pk)
    data = dict()
    context = {'teacher': teacher}
    data['html_form'] = render_to_string('GovernmentEmployee/Teacher/partial_teacher_view.html', context, request=request)
    return JsonResponse(data)

