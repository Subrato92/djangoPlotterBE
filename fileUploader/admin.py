from django.contrib import admin

# Register your models here.
from .models import File
from .models import Data

admin.site.register(File)
admin.site.register(Data)