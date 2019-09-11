from django import forms
from .models import Projects, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','project_photo','description','url','owner')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
