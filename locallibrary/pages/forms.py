from django import forms

class URLForm(forms.Form):
    url = forms.CharField(max_length=256)

    def get_form_data(self):
        print(self.cleaned_data)