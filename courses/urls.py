from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView

app_name = 'courses'

urlpatterns=[
    path('', CourseListView.as_view(), name='list'),
    path('<slug>', CourseDetailView.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson-detail')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)