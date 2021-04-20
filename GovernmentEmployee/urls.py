from django.contrib import admin
from django.urls import path, include

from GovernmentEmployee import views
from django.conf import settings
from django.conf.urls.static import static
from TeacherEnroll import views as teacherEnroll
from StudentEnroll import views as student_enroll
urlpatterns = [
    path('Home/', views.home, name='govt_home'),

    path('GovernmentEmployeeHome/', views.GovernmentEmployeeHome, name='GovernmentEmployeeHome'),
    path('GovernmentEmployeeProfile/', views.GovernmentEmployeeProfile, name='GovernmentEmployeeProfile'),

    path('change/password/', views.ChangePasswordView.as_view(), name='GovernmentEmployee_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='GovernmentEmployee_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

    path('StudentEnroll/', student_enroll.Student_Enroll_list, name='Student_Enroll_View'),
    path('StudentEnroll/create/', student_enroll.Stuent_Enroll_create, name='Student_Enroll_create'),
    path('<int:pk>/StudentEnroll/delete/', student_enroll.Student_Enroll_delete, name='Student_Enroll_delete'),
    path('<int:pk>/StudentEnroll/Update/', student_enroll.Student_Enroll_Update, name='Student_Enroll_Update'),


    path('course/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('<int:pk>/course/update/', views.course_update, name='course_update'),
    path('<int:pk>/course/view/', views.course_view, name='course_view'),
    path('<int:pk>/course/delete/', views.course_delete, name='course_delete'),

    path('teacherEnroll/', teacherEnroll.teacherEnroll_list, name='teacherEnroll_list'),
    path('teacherEnroll/create/', teacherEnroll.teacherEnroll_create, name='teacherEnroll_create'),
    path('<int:pk>/teacherEnroll/update/', teacherEnroll.teacherEnroll_update, name='teacherEnroll_update'),
    path('<int:pk>/teacherEnroll/delete/', teacherEnroll.teacherEnroll_delete, name='teacherEnroll_delete'),

    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.TeacherSignUpView.as_view(), name='teacher_create'),
    # path('<int:pk>/teacher/update/', views.teacher_update, name='teacher_update'),
    path('<int:pk>/teacher/delete/', views.teacher_delete, name='teacher_delete'),
    path('<int:pk>/teacher/view/', views.teacher_view, name='teacher_view'),

    path('student/', views.student_list, name='student_list'),
    path('student/create/', views.StudentSignUpView.as_view(), name='student_create'),
    # path('<int:pk>/student/update/', views.student_update, name='student_update'),
    path('<int:pk>/student/delete/', views.student_delete, name='student_delete'),
    path('<int:pk>/student/view/', views.student_view, name='student_view'),

    path('material_approved/', views.material_list, name='course_material_approved_list'),
    # path('material/create/', views.material_create, name='material_create'),
    path('<int:pk>/material_approved/update/', views.material_update, name='course_material_approved_update'),
    path('<int:pk>/material_approved/view/', views.material_view, name='course_material_approved_view'),
    path('<int:pk>/material_approved/delete/', views.material_delete, name='course_material_approved_delete'),


    path('teacher/enroll/', teacherEnroll.teacher_course_assign_list, name='teacher_course_assign_list'),
    path('teacher/enroll/create/', teacherEnroll.teacher_course_assign_create, name='teacher_course_assign_create'),
    path('teacher/enroll/<int:pk>/course/update/', teacherEnroll.teacher_course_assign_update,
         name='teacher_course_assign_update'),
    path('teacher/enroll/<int:pk>/course/delete/', teacherEnroll.teacher_course_assign_delete,
         name='teacher_course_assign_delete'),
]
