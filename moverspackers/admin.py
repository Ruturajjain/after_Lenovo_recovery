from django.contrib import admin

from moverspackers.models import *

# Register your models here.

admin.site.register([SiteUser, Services, Contact])