from django import forms
from userprofile.models import Profile
from django.contrib.auth.models import User

class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('student_id','photo')
