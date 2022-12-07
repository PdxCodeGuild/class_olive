from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('bob/<str:timeframe>', views.goals_by_timeframe, name='bob'),
]