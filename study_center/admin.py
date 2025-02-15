from django.contrib import admin
from .models import StudyCenter, CustomUser, Course, Certificate, SocialStatus

# Register your models here.
class locationAdmin(admin.ModelAdmin):
    readonly_fields=('address', 'latitude', 'longitude')

admin.site.register(StudyCenter, locationAdmin)
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(SocialStatus)
