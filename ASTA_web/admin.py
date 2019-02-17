from django.contrib import admin
from .models import User
from .models import Message
from .models import Blog
from .models import UploadFile
from .models import Rank

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(UploadFile)
admin.site.register(Rank)
