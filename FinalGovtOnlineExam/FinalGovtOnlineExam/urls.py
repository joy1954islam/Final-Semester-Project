"""FinalGovtOnlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts import views as account_views

from django.conf import settings
from django.conf.urls.static import static
from GovernmentEmployee import views as user_views, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', account_views.home, name='home'),
    # path('', IndexPageView.as_view(), name='index'),
    path('', views.index, name='index'),

    path('i18n/', include('django.conf.urls.i18n')),


    path('accounts/', include('accounts.urls')),
    path('SuperAdmin/',include('SuperAdmin.urls')),
    path('GovernmentEmployee/',include('GovernmentEmployee.urls')),
    path('Teacher/',include('Teacher.urls')),
    path('Student/', include('Student.urls')),

    path('courses/', user_views.Home_Course_View, name='Home_Course_View'),
    path('courses/details/<int:pk>/', user_views.CourseDetails, name='Home_Course_Details'),
    path('teacher/', user_views.Home_Teacher_View, name='Home_Teacher_View'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
