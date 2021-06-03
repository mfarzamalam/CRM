from django import forms
from .models import Lead, User, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    age        = forms.IntegerField()



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model         = User
        fields        = ('username',)
        field_classes = {'username': UsernameField}



class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        # super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = Agent.objects.filter(organisation=request.user.userprofile)