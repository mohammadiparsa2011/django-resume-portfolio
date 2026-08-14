from django.contrib import admin
from .models import HeroSection, ServicesSection, About, SocialLink, Skill, SkillIcon, WorkExperience, EducationExperience

# Register your models here.

admin.site.register(HeroSection)
admin.site.register(ServicesSection)
admin.site.register(About)
admin.site.register(SocialLink)
admin.site.register(Skill)
admin.site.register(SkillIcon)
admin.site.register(WorkExperience)
admin.site.register(EducationExperience)
