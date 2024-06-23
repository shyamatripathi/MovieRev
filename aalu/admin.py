from django.contrib import admin
from aalu.models import Login
from aalu.models import Signin
from aalu.models import Review1
from aalu.models import UserRev
admin.site.register(Login)
admin.site.register(Review1)
admin.site.register(Signin)
admin.site.register(UserRev)
# Register your models here.
