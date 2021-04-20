from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template.loader import render_to_string

from UploadLecture.forms import UploadLectureForm
from UploadLecture.models import UploadLecture


def lecture_list(request):
    lectures = UploadLecture.objects.all()
    return render(request, 'UploadLecture/lecture_list.html', {'lectures': lectures})


def lecture_create(request):
    if request.method == 'POST':
        form = UploadLectureForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Lecture Upload Created Successfully")
            return redirect('lecture_list')
        else:
            messages.error(request, "Course Not Created Successfully")
    else:
        form = UploadLectureForm()
    return render(request, 'UploadLecture/partial_lecture_create.html', {'form': form})


def lecture_update(request, pk):
    course = get_object_or_404(UploadLecture, pk=pk)
    form = UploadLectureForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Lecture Updated Successfully")
        return redirect("lecture_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'UploadLecture/partial_lecture_update.html', {'form': form})


def lecture_delete(request, pk):
    lecture = get_object_or_404(UploadLecture, pk=pk)
    data = dict()
    if request.method == 'POST':
        lecture.delete()
        data['form_is_valid'] = True
        lectures = UploadLecture.objects.all()
        data['html_lecture_list'] = render_to_string('UploadLecture/partial_lecture_list.html', {'lectures': lectures})
    else:
        context = {'lecture': lecture}
        data['html_form'] = render_to_string('UploadLecture/partial_lecture_delete.html', context, request=request)
    return JsonResponse(data)

