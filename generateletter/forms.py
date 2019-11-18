from django import forms
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm
from generateletter.models import CustomUserM,Organization,Visaletters
from bootstrap_modal_forms.mixins import PopRequestMixin,CreateUpdateAjaxMixin
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(BSModalForm):
    class Meta:
        model = CustomUserM
        fields = ['username','email','user_role']

class CustomUserForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = CustomUserM
        fields = ['username','email','password1','password2']     

class OrganizationForm(BSModalForm):
    class Meta:
        model = Organization
        fields = ['Name_of_Organization','Address']

class PaymentStatusForm(BSModalForm):
    class Meta:
        model = Visaletters
        fields = ['Payment_status']        

class visalettersform(BSModalForm):
    class Meta:
        model = Visaletters
        fields = ['multiplicity','Country','Tourism','entry_from','departure_to','Visa_Letter_Number','Routes_and_Places','hotels','amount']