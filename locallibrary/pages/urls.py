from django.urls import path
from .views import HomePageView

from django.views.generic import TemplateView
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('css/small.css', TemplateView.as_view(
    #     template_name='small.css',
    #     content_type='text/css')
    # )
]

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
# ]