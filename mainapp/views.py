from django.shortcuts import render, HttpResponse
from .forms import EmailSubmit

# Create your views here.
def index(request):
	form = EmailSubmit()
	return render(request, "index.html", {'form': form})

def formpage(request):
	print("hola")
	return render(request, "FormPage.html")

def emailsubmit(request):
	form_data = EmailSubmit(request.POST)
	print(form_data)
	saved_data = form_data.save()
	return HttpResponse(form_data)