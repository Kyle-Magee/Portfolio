from django import forms


class TemplateForm(forms.Form):
    template_file = forms.FileField(
        label='Select a File',
    )
