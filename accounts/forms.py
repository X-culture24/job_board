from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Import the Profile model
import re  # Moved to the top

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User      
        fields = ["username", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):  
    class Meta:
        model = Profile
        fields = ["full_name", "field_of_study", "experience", "location", "phone_number"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Enter your full name", "class": "form-control"}),
            "field_of_study": forms.TextInput(attrs={"placeholder": "Enter your field of study", "class": "form-control"}),
            "experience": forms.NumberInput(attrs={"placeholder": "Years of experience", "class": "form-control"}),
            "location": forms.TextInput(attrs={"placeholder": "Enter your location", "class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Enter your phone number", "class": "form-control"}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        phone_pattern = re.compile(r"^\+?\d{10,15}$")  # Matches +254712345678 or 0712345678

        if phone_number and not phone_pattern.match(phone_number):
            raise forms.ValidationError("Enter a valid phone number in international format (e.g., +254712345678).")

        return phone_number
