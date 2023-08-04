# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('jbf', views.job_list, name='job_list'),
    path('create_job/', views.create_job, name='create_job'),
    path('feture', views.featured_candidates, name='featured_candidates'),
    path('emls/', views.emplist, name='emplist'),
    path('eminf/', views.empinfo, name='empinfo'),



]
