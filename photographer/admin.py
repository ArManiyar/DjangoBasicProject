from django.contrib import admin
from photographer.models import Contacts, Image





# Register your models here.
# admin.site.register(Contacts)
# admin.site.register(Image)
models = (Contacts, Image)
for m in models:
   admin.site.register(m)