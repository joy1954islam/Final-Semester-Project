from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from TeacherEnroll.forms import TeacherEnrollForm
from TeacherEnroll.models import TeacherEnroll


def teacherEnroll_list(request):
    teacherEnrolls = TeacherEnroll.objects.all()
    return render(request, 'TeacherEnroll/teacherEnroll_list.html', {'teacherEnrolls': teacherEnrolls})


def save_teacherEnroll_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
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
    else:
        form = TeacherEnrollForm()
    return save_teacherEnroll_form(request, form, 'teacherEnroll/partial_teacherEnroll_create.html')


def teacherEnroll_update(request, pk):
    teacherEnroll = get_object_or_404(TeacherEnroll, pk=pk)
    if request.method == 'POST':
        form = TeacherEnrollForm(request.POST, instance=teacherEnroll)
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