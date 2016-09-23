from django import forms

from .models import UserInfo

class EmailSubmit(forms.ModelForm):

    class Meta:
        model = UserInfo
        
        widgets = {
            'email_one': forms.TextInput(attrs={'class': 'form-control'}),
            'email_two': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = ('email_one', 'email_two',)