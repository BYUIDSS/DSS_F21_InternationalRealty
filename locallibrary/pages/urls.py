from django.urls import path
from .views import HomePageView
from django.views.generic import TemplateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('css/style.css', TemplateView.as_view(
        template_name='style.css',
        content_type='text/css')
    )
]