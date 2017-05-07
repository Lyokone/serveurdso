from django import forms


class UploadFile(forms.Form):
    title = forms.CharField(label="Titre", max_length=50)
    user = forms.CharField(max_length=50)
    file = forms.FileField()
