from django.urls import path
from django.contrib import admin
from Oriana import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),

    path('hosts/', views.hosts, name='hosts'),
    path('shosts/', views.shosts, name='shosts'),
    path('users/', views.users, name='users'),
    path('services/', views.services, name='services'),
    path('tasks/', views.tasks, name='tasks'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('host/<int:host_id>/', views.host, name='host'),
    path('shost/<int:shost_id>/', views.shost, name='shost'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('service/<int:service_id>/', views.service, name='service'),
    path('task/<int:task_id>/', views.task, name='task'),

    path('possible_lm/', views.possible_lm, name='possible_lm'),
    path('possible_lm_detail/<int:possiblelm_id>/', views.possible_lm_detail, name='possible_lm_detail'),
    path('lm_sessions/', views.lm_sessions, name='lm_sessions'),
    path('lmsession/<int:lmsession_id>/', views.lmsession, name='lmsession'),

    path('fa_cmdline/', views.fa_cmdline, name='fa_cmdline'),
    path('fa_cmdline/<int:cmdline_id>/', views.fa_cmdline_detail, name='fa_cmdline_detail'),

    path('suspicious_behavior/', views.suspicious_behavior, name='suspicious_behavior'),
    path('suspicious_behavior/<str:type>/', views.suspicious_behavior_type, name='suspicious_behavior_type'),

    path('suspicious_user_behavior/', views.suspicious_user_behavior, name='suspicious_user_behavior'),
    path('suspicious_user_behavior/<int:user_id>/', views.suspicious_behavior_user, name='suspicious_behavior_user'),
    path('suspicious_user_behavior_detail/<int:s_id>/', views.suspicious_user_behavior_detail, name='suspicious_user_behavior_detail'),

    path('suspicious_source_behavior/', views.suspicious_source_behavior, name='suspicious_source_behavior'),
    path('suspicious_source_behavior/<int:source_id>/', views.suspicious_behavior_source, name='suspicious_behavior_source'),
    path('suspicious_source_behavior_detail/<int:s_id>/', views.suspicious_source_behavior_detail, name='suspicious_source_behavior_detail'),

]
