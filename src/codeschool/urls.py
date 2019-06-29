"""codeschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

# Own
from pages.views import HomePageView, AboutPageView, ContactPageView, HelptPageView
from users.views import register, ProfilePageView
from courses.views import CoursePageView, CourseChapterRedirectView, CourseChapterPageView, CourseTestPageView, CourseTestRedirectView, CourseCompletedPageView

urlpatterns = [

    # Own
    path('', HomePageView.as_view(), name='home'),

    path('course/', CoursePageView.as_view(), name='course'),
    path('course/chapter/', CourseChapterRedirectView.as_view(), name='chapter-main'),
    path('course/chapter/<int:chapter_id>/', CourseChapterPageView.as_view(), name='chapter'),

    path('course/Questionnaire/', CourseTestRedirectView.as_view(), name='Questionnaire-main'),
    path('course/Questionnaire/<int:id>/', CourseTestPageView.as_view(), name='Questionnaire'),

    path('course/completed/', CourseCompletedPageView.as_view(), name='course-completed'),


    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('register/', register, name='register'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('help/', HelptPageView.as_view(), name='help'),


    # Django included
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

