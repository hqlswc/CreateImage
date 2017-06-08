from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    memory = forms.IntegerField()
    cpu = forms.IntegerField()
    disk = forms.CharField(max_length=100)
    cdrom = forms.CharField(max_length=100)
    network = forms.CharField(max_length=100)
