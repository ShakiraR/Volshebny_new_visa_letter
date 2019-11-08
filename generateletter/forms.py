from django import forms
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm
from generateletter.models import CustomUserM,Organization,Visaletters

class CustomUserCreationForm(BSModalForm):
    class Meta:
        model = CustomUserM
        fields = ['username','email','user_role']

class CustomUserForm(BSModalForm):
    class Meta:
        model = CustomUserM
        fields = ['username','email']     

class OrganizationForm(BSModalForm):
    class Meta:
        model = Organization
        fields = ['Name_of_Organization','Address']             