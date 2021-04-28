from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)

    
    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'아이디를 입력하시오',
             'id': 'id'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '비밀번호를 입력하시오',
            'id': 'password',
        }
    ))


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'아이디를 입력하시오',
             'id': 'id'}
    ))
    password = forms.CharField(label='password',widget=forms.PasswordInput(
        attrs={
            'id': 'password1',
        }
    ))
    password2 = forms.CharField(label='Repeate Password',widget=forms.PasswordInput(
        attrs={
            'id': 'password2',
        }
    ))

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        help_texts ={
            'username':None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')
        return cd['password2']

