from django.contrib import admin
from .models import UserInfo, Contact, Invitation

admin.site.register(UserInfo)
admin.site.register(Contact)
admin.site.register(Invitation)