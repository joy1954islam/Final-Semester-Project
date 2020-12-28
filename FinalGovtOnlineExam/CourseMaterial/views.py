from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from CourseMaterial.forms import CourseMaterialForm
from CourseMaterial.models import CourseMaterial


def material_list(request):
    topics = CourseMaterial.objects.all()
    return render(request, 'CourseMaterial/content_list.html', {'topics': topics})


def save_material_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            data['form_is_valid'] = True
            topics = CourseMaterial.objects.all()
            messages.success(request, "Course Material Successfully")
            data['html_topic_list'] = render_to_string('CourseMaterial/partial_content_list.html', {'topics': topics })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def material_create(request):
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST)
    else:
        form = CourseMaterialForm()
    return save_material_form(request, form, 'CourseMaterial/partial_content_create.html')


def material_update(request, pk):
    topic = get_object_or_404(CourseMaterial, pk=pk)
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST, instance=topic)
    else:
        form = CourseMaterialForm(instance=topic)
    return save_material_form(request, form, 'CourseMaterial/partial_content_update.html')


def material_delete(request, pk):
    topic = get_object_or_404(CourseMaterial, pk=pk)
    data = dict()
    if request.method == 'POST':
        topic.delete()
        data['form_is_valid'] = True
        topics = CourseMaterial.objects.all()
        data['html_topic_list'] = render_to_string('CourseMaterial/partial_content_list.html', {'topics': topics })
    else:
        context = {'topic': topic}
        data['html_form'] = render_to_string('CourseMaterial/partial_content_delete.html', context, request=request)
    return JsonResponse(data)