from django.shortcuts import render
from django.views.generic import FormView
from . import forms

class HomePageView(FormView):
    template_name = 'home.html'
    form_class = forms.URLForm
    success_url = '/'

    def form_valid(self, form):
        form.get_form_data()
        return super().form_valid(form)

