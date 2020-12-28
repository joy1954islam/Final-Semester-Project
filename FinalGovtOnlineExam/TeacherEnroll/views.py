from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template.loader import render_to_string

from TeacherEnroll.filters import CourseAssignFilter
from TeacherEnroll.forms import TeacherEnrollForm,TeacherCourseAssignForm
from TeacherEnroll.models import TeacherEnroll
from django.contrib.auth import get_user_model
User = get_user_model()


def teacherEnroll_list(request):
    teacherEnrolls = TeacherEnroll.objects.all()
    MyFileter = CourseAssignFilter(request.GET, queryset=teacherEnrolls)
    teacherEnrolls = MyFileter.qs
    context = {
        'teacherEnrolls': teacherEnrolls,
        'MyFileter':MyFileter,
    }
    return render(request, 'TeacherEnroll/teacherEnroll_list.html', context)


def save_teacherEnroll_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner_name = request.user
            form.save()
            data['form_is_valid'] = True
            teacherEnrolls = TeacherEnroll.objects.all()
            data['html_teacherEnroll_list'] = render_to_string(
                'TeacherEnroll/partial_teacherEnroll_list.html',{'teacherEnrolls': teacherEnrolls})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def teacherEnroll_create(request):
    if request.method == 'POST':
        form = TeacherEnrollForm(request.POST)
        # user = request.user
    else:
        form = TeacherEnrollForm()
    return save_teacherEnroll_form(request, form, 'teacherEnroll/partial_teacherEnroll_create.html')


def teacherEnroll_update(request, pk):
    teacherEnroll = get_object_or_404(TeacherEnroll, pk=pk)
    if request.method == 'POST':
        form = TeacherEnrollForm(request.POST,instance=teacherEnroll)
    else:
        form = TeacherEnrollForm(instance=teacherEnroll)
    return save_teacherEnroll_form(request, form, 'TeacherEnroll/partial_teacherEnroll_update.html')


def teacherEnroll_delete(request, pk):
    teacherEnroll = get_object_or_404(TeacherEnroll, pk=pk)
    data = dict()
    if request.method == 'POST':
        teacherEnroll.delete()
        data['form_is_valid'] = True
        teacherEnrolls = TeacherEnroll.objects.all()
        data['html_teacherEnroll_list'] = render_to_string('TeacherEnroll/partial_teacherEnroll_list.html',
                                                           {'teacherEnrolls': teacherEnrolls})
    else:
        context = {'teacherEnroll': teacherEnroll}
        data['html_form'] = render_to_string('TeacherEnroll/partial_teacherEnroll_delete.html', context,
                                             request=request)
    return JsonResponse(data)


def teacher_course_assign_list(request):
    teacherEnrolls = TeacherEnroll.objects.all()
    MyFileter = CourseAssignFilter(request.GET, queryset=teacherEnrolls)
    teacherEnrolls = MyFileter.qs
    context = {
        'teacherEnrolls': teacherEnrolls,
        'MyFileter':MyFileter,
    }
    return render(request, 'TeacherEnroll/list.html', context)


def teacher_course_assign_create(request):
    form = TeacherCourseAssignForm()
    if request.is_ajax():
        term = request.GET.get('term')
        languages = User.objects.all().filter(username__icontains=term)
        return JsonResponse(list(languages.values()), safe=False)
    if request.method == 'POST':
        form = TeacherCourseAssignForm(request.POST)
        if form.is_valid():
            form.instance.owner_name = request.user
            form.save()
            return redirect('teacher_course_assign_list')
    return render(request, 'TeacherEnroll/home.html', {'form': form})


def teacher_course_assign_update(request,pk):
    teacherEnrolls = get_object_or_404(TeacherEnroll, pk=pk)
    form = TeacherCourseAssignForm(request.POST or None, request.FILES or None, instance=teacherEnrolls)
    if request.is_ajax():
        term = request.GET.get('term')
        languages = User.objects.all().filter(username__icontains=term)
        return JsonResponse(list(languages.values()), safe=False)
    if form.is_valid():
        form.save()
        messages.success(request, "Teacher course Assign Updated Successfully")
        return redirect("teacher_course_assign_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'TeacherEnroll/home.html', {'form': form})


def teacher_course_assign_delete(request,pk):
    teacherEnrolls = get_object_or_404(TeacherEnroll, pk=pk)
    teacherEnrolls.delete()
    return redirect("teacher_course_assign_list")