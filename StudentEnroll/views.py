from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

from StudentEnroll.filters import StudentEnrollFilter
from StudentEnroll.forms import StudentEnrollForm
from Teacher.models import Student


def Student_Enroll_list(request):
    studentEnrolls = Student.objects.all()
    MyFileter = StudentEnrollFilter(request.GET, queryset=studentEnrolls)
    studentEnrolls = MyFileter.qs
    context = {
        'studentEnrolls': studentEnrolls,
        'MyFileter': MyFileter,
    }
    return render(request, 'StudentEnroll/student_enroll_list.html', context)


def save_studentEnroll_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner_name = request.user
            form.save()
            data['form_is_valid'] = True
            studentEnrolls = Student.objects.all()
            data['html_studentEnroll_list'] = render_to_string(
                'StudentEnroll/partial_student_enroll_list.html', {'studentEnrolls': studentEnrolls})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def Stuent_Enroll_create(request):
    if request.method == 'POST':
        form = StudentEnrollForm(request.POST)
        # user = request.user
    else:
        form = StudentEnrollForm()
    return save_studentEnroll_form(request, form, 'StudentEnroll/partial_student_enroll_create.html')


def Student_Enroll_Update(request, pk):
    studentEnroll = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentEnrollForm(request.POST, instance=studentEnroll)
    else:
        form = StudentEnrollForm(instance=studentEnroll)
    return save_studentEnroll_form(request, form, 'StudentEnroll/partial_student_enroll_update.html')


def Student_Enroll_delete(request, pk):
    studentEnroll = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        studentEnroll.delete()
        data['form_is_valid'] = True
        studentEnrolls = Student.objects.all()
        data['html_studentEnroll_list'] = render_to_string('StudentEnroll/partial_student_enroll_list.html',
                                                           {'studentEnrolls': studentEnrolls})
    else:
        context = {'studentEnroll': studentEnroll}
        data['html_form'] = render_to_string('StudentEnroll/partial_student_enroll_delete.html', context,
                                             request=request)
    return JsonResponse(data)
