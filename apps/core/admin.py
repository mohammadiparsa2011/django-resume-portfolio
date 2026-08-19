from django.contrib import admin
from .models import HeroSection, ServicesSection, About, SocialLink, Skill, SkillIcon, WorkExperience, EducationExperience, PortfolioItem, PortfolioCategory

# Register your models here.

admin.site.register(HeroSection)
admin.site.register(ServicesSection)
admin.site.register(About)
admin.site.register(SocialLink)
admin.site.register(Skill)
admin.site.register(SkillIcon)
admin.site.register(WorkExperience)
admin.site.register(EducationExperience)

@admin.register(PortfolioCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_categories']
    filter_horizontal = ['categories']  # ✅ این باعث میشه انتخاب چند دسته‌بندی توی ادمین راحت باشه

    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])
    display_categories.short_description = 'دسته‌بندی‌ها'
