from django.contrib import admin
from .models import Catalog
from .models import Reg
from .models import Login

admin.site.register(Catalog)
admin.site.register(Reg)
admin.site.register(Login)