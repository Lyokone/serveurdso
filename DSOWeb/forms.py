from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(label="Titre", max_length=50)
    user = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=100)
    calibB = forms.BooleanField(required=False)
    file = forms.FileField()
