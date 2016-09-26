from django import forms
from .models import UserInfo, Invitation, Contact

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

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact

		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message', 'type': 'textarea'}),
		}
		fields = ('name','mail','phone','message',)