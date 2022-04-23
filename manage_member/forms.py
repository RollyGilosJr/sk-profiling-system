from typing import ClassVar
from django import forms
from manage_member.models import Member

class member_form (forms.ModelForm):
    class Meta:
        model = Member
        fields = ['chairman',
                  'kagawad1',
                  'kagawad2',
                  'kagawad3',
                  'kagawad4',
                  'kagawad5',
                  'kagawad6',
                  'kagawad7',
                  'treasurer',
                  'secretary']
        labels = {
            'chairman' : "",
            'kagawad1' : "",
            'kagawad2' : "",
            'kagawad3' : "",
            'kagawad4' : "",
            'kagawad5' : "",
            'kagawad6' : "",
            'kagawad7' : "",
            'treasurer' : "",
            'secretary' : ""
        }
