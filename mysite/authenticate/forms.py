from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
    
class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden',}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password')
    
class SignUpForm(UserCreationForm):
    """SignUp UserCreationForm."""

    # TODO: Define form fields he
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    first_name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}))
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)    
       
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label= ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] ='Enter Password'
        self.fields['password1'].label=''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small> Enter the same password as before, for verification.</small></span>'
        
        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image',) 







