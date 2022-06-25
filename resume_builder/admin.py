from django.contrib import admin
from .models import (
    Resume,
    Contact,
    Experience,
    Responsibilities,
    Education,
    Certifications,
    Skills,
    Summary
)
# Register your models here.

admin.site.register(Resume)
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Responsibilities)
admin.site.register(Education)
admin.site.register(Certifications)
admin.site.register(Skills)
admin.site.register(Summary)






