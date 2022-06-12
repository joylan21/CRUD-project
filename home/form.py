from socket import fromshare
from django import forms
from .models import user

class userform(forms.ModelForm):
    class Meta:
        model = user
        fields=['name','email','password']
        # lables={'name':'Username','email':'Email address','password':'password'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control','id':'exampleInputEmail0','placeholder':'Username'}),
        'email':forms.EmailInput(attrs={'class':'form-control','id':'exampleInputEmail1','placeholder':'Email'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','id':'exampleInputpassword1','placeholder':'password'}),}