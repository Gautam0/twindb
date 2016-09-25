from django.shortcuts import render, HttpResponse
from .forms import EmailSubmit
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
	form = EmailSubmit()
	return render(request, "index.html", {'form': form})

def formpage(request):
	print("hola")
	return render(request, "FormPage.html")

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
	return HttpResponse(saved_data)