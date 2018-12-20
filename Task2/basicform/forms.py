from django import forms

from .models import Applicant

class PostForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = ('name', 'phone','email','whyme','ideas')