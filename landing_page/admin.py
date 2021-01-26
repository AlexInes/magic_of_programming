from django.contrib import admin
from landing_page.models import Work, Education, Skill, SiteConfiguration
from solo.admin import SingletonModelAdmin
# Register your models here.
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Skill)

admin.site.register(SiteConfiguration, SingletonModelAdmin)
