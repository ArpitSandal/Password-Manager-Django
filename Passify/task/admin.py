from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Authenticate)
admin.site.register(LoginPass)
admin.site.register(CreditPass)
admin.site.register(NotesPass)