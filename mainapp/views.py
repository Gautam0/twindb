from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import EmailSubmit, InviteForm
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
	form = EmailSubmit()
	form_two = InviteForm()
	return render(request, "index.html", {'form': form, 'form_two': form_two})

def google_form(request):
	print("hola")
	return render(request, "googleform.html")

def emailsubmit(request):
	form_data = EmailSubmit(request.POST)
	
	saved_data = form_data.save(commit=False)
	e1 = saved_data.email_one
	e2 = saved_data.email_two

	email_sub = 'Twin study form.'
	email_mgs = 'Thank you for sign up. Please click this google form. https://docs.google.com/forms/d/e/1FAIpQLSfeFYikE4_LmlYG9kNF7LW4XoKdpT18euHzfqqUtPYCUdwXrA/viewform'

	sent = send_mail(email_sub, email_mgs, settings.EMAIL_HOST_USER,
         [e1, e2], fail_silently=False)
	print("Email successfully sent to you and your twin. Please go to your mail address.")
	saved_data.save()
	return HttpResponseRedirect('/google_form')

def invite(request):
	form_data = InviteForm(request.POST)
	
	saved_data = form_data.save(commit=False)
	email = saved_data.invited_by

	email_sub = 'Twin study form.'
	email_mgs = 'Thank you for sign up. Please click this google form. https://docs.google.com/forms/d/e/1FAIpQLSfeFYikE4_LmlYG9kNF7LW4XoKdpT18euHzfqqUtPYCUdwXrA/viewform'

	sent = send_mail(email_sub, email_mgs, settings.EMAIL_HOST_USER,
         [email], fail_silently=False)
	print("Email successfully sent to you and your twin. Please go to your mail address.")
	saved_data.save()
	return HttpResponseRedirect('/thank_page', {'success': success})

def thank_page(request):
	return render(request, 'thank_you.html')