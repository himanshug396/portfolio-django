from django.contrib import admin
from .models import *

admin.site.register(AboutmeText, admin.ModelAdmin)
admin.site.register(NavigationItem, admin.ModelAdmin)
admin.site.register(Quote, admin.ModelAdmin)
admin.site.register(QuoteMe, admin.ModelAdmin)
admin.site.register(ProjectCoverContainerType, admin.ModelAdmin)
admin.site.register(Project, admin.ModelAdmin)
admin.site.register(Skill, admin.ModelAdmin)
admin.site.register(SocialMedia, admin.ModelAdmin)
admin.site.register(Query, admin.ModelAdmin)
admin.site.register(Resume, admin.ModelAdmin)