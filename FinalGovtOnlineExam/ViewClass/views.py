from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from CourseMaterial.models import CourseMaterial
from UploadLecture.models import UploadLecture
from accounts.decorators import student_required


@login_required
@student_required
def home(request,pk):
    course = CourseMaterial.objects.filter(CourseName=pk)
    # lecture = UploadLecture.objects.filter(MaterialName=pk)
    context = {
        'course': course,
        # 'lecture': lecture,

    }
    return render(request,'ViewClass/Video.html',context)


# def lectureviewclass(request,course_pk,lecture_pk):
#     course = get_object_or_404(CourseMaterial, pk=course_pk)
#     lecture = get_object_or_404(UploadLecture, pk=lecture_pk, MaterialName=course)
#     context = {
#         'course': course,
#         'lecture': lecture,
#     }
#     return render(request, 'ViewClass/ViewClass.html', context)

def lectureviewclass(request,lecture_pk):
    # course = get_object_or_404(CourseMaterial, pk=course_pk)
    lecture = UploadLecture.objects.filter(MaterialName=lecture_pk)
    context = {
        # 'course': course,
        'lecture': lecture,
    }
    return render(request, 'ViewClass/ViewClass.html', context)