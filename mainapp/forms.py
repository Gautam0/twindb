from django import forms

from .models import UserInfo, Invitation

class EmailSubmit(forms.ModelForm):

    class Meta:
        model = UserInfo
        
        widgets = {
            'email_one': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'email_two': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }
        fields = ('email_one', 'email_two',)

class InviteForm(forms.ModelForm):

    class Meta:
        model = Invitation
        
        widgets = {
            'invited_by': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }
        fields = ('invited_by',)

