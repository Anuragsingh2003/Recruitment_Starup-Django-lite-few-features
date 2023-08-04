# forms.py

from django import forms
from .models import CandidateApplication

# recruitment/forms.py


class CandidateApplicationForm(forms.ModelForm):
    class Meta:
        model = CandidateApplication
        fields = ['candidate_name', 'email', 'resume', 'cover_letter']

    def __init__(self, *args, **kwargs):
        super(CandidateApplicationForm, self).__init__(*args, **kwargs)
        self.fields['resume'].widget.attrs.update({'accept': 'image/*, application/pdf, text/plain'})


    # Add any additional form validations or customizations if required



from django.contrib.auth.models import User
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

# forms.py

from django import forms
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location']


class EmpForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
