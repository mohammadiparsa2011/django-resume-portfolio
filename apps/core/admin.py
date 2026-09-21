from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import (
    HeroSection, ServicesSection, About, SocialLink, Skill, SkillIcon,
    WorkExperience, EducationExperience, PortfolioItem, PortfolioCategory,
    FreelanceRequest, JobRequest, Hire, Testimonials, Blog,
    FooterSocialLink, Footer
)


# ============================================================
# تابع کمکی برای پیش‌نمایش تصویر در پنل ادمین
# ============================================================
def image_preview(obj, field_name, width=60, height=60):
    """نمایش بندانگشتی تصویر در پنل ادمین"""
    field = getattr(obj, field_name, None)
    if field:
        return format_html(
            '<img src="{}" style="width:{}px; height:{}px; border-radius:8px; object-fit:cover;" />',
            field.url, width, height
        )
    return format_html('<span style="color:#999;">—</span>')


# ============================================================
# HeroSection
# ============================================================
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'avatar_preview']
    readonly_fields = ['avatar_preview_field']
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'job_title', 'button_text')
        }),
        ('فایل‌ها', {
            'fields': ('avatar', 'avatar_preview_field', 'resume_file')
        }),
    )

    def avatar_preview(self, obj):
        return image_preview(obj, 'avatar', 50, 50)
    avatar_preview.short_description = 'آواتار'

    def avatar_preview_field(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="max-width:200px; border-radius:10px;" />', obj.avatar.url)
        return '—'
    avatar_preview_field.short_description = 'پیش‌نمایش آواتار'

    def has_add_permission(self, request):
        # فقط یک رکورد مجاز است
        if HeroSection.objects.exists():
            return False
        return True


# ============================================================
#  Inline ها برای About
# ============================================================
class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ['name', 'icon', 'url', 'order']
    ordering = ['order']


class SkillIconInline(admin.TabularInline):
    model = SkillIcon
    extra = 1
    fields = ['icon_image', 'url']


class SkillInline(admin.StackedInline):
    model = Skill 
    extra = 1 
    show_change_link = True 
    fields = ['title', 'description', 'percentage', 'bg_color']


# ============================================================
# About
# ============================================================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'signature_preview']
    inlines = [SocialLinkInline, SkillInline]
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('quote', 'description', 'job_title', 'name')
        }),
        ('تصاویر', {
            'fields': ('signature', 'signature_preview_field', 'main_image', 'main_image_preview')
        }),
    )
    readonly_fields = ['signature_preview_field', 'main_image_preview']

    def signature_preview(self, obj):
        return image_preview(obj, 'signature', 80, 30)
    signature_preview.short_description = 'امضا'

    def signature_preview_field(self, obj):
        if obj.signature:
            return format_html('<img src="{}" style="max-width:200px;" />', obj.signature.url)
        return '—'
    signature_preview_field.short_description = 'پیش‌نمایش امضا'

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="max-width:200px; border-radius:10px;" />', obj.main_image.url)
        return '—'
    main_image_preview.short_description = 'پیش‌نمایش عکس اصلی'

    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return True


# ============================================================
# SocialLink (مستقل)
# ============================================================
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'about', 'url', 'order', 'icon_preview']
    list_editable = ['order']
    list_filter = ['about']
    search_fields = ['name', 'url']
    list_select_related = ['about']
    list_per_page = 20

    def icon_preview(self, obj):
        return image_preview(obj, 'icon', 30, 30)
    icon_preview.short_description = 'آیکون'


# ============================================================
# Skill (مستقل)
# ============================================================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'about', 'percentage', 'color_preview']
    list_editable = ['percentage']
    list_filter = ['about']
    search_fields = ['title', 'description']
    list_select_related = ['about']
    list_per_page = 20

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block; width:20px; height:20px; '
            'background:{}; border-radius:4px; border:1px solid #ccc;"></span>',
            obj.bg_color
        )
    color_preview.short_description = 'رنگ'


# ============================================================
# SkillIcon
# ============================================================
@admin.register(SkillIcon)
class SkillIconAdmin(admin.ModelAdmin):
    list_display = ['skill', 'icon_preview', 'url']
    list_filter = ['skill']
    search_fields = ['skill__title']
    list_select_related = ['skill']
    list_per_page = 20

    def icon_preview(self, obj):
        return image_preview(obj, 'icon_image', 30, 30)
    icon_preview.short_description = 'آیکون'


# ============================================================
# ServicesSection
# ============================================================
@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'bg_color', 'color_preview', 'short_description']
    list_editable = ['bg_color']
    search_fields = ['title', 'description']
    list_per_page = 20
    save_on_top = True

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block; width:25px; height:25px; '
            'background:{}; border-radius:50%; border:1px solid #ccc;"></span>',
            obj.bg_color
        )
    color_preview.short_description = 'پیش‌نمایش رنگ'

    def short_description(self, obj):
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return '—'
    short_description.short_description = 'توضیحات'


# ============================================================
# WorkExperience
# ============================================================
@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_year', 'end_year']
    list_filter = ['start_year', 'company']
    search_fields = ['company', 'position', 'description']
    ordering = ['start_year']
    list_per_page = 20
    save_on_top = True


# ============================================================
# EducationExperience
# ============================================================
@admin.register(EducationExperience)
class EducationExperienceAdmin(admin.ModelAdmin):
    list_display = ['university', 'degree', 'start_year', 'end_year']
    list_filter = ['start_year', 'university']
    search_fields = ['university', 'degree', 'description']
    ordering = ['start_year']
    list_per_page = 20
    save_on_top = True


# ============================================================
# PortfolioCategory
# ============================================================
@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_per_page = 20


# ============================================================
# PortfolioItem
# ============================================================
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail_preview', 'display_categories', 'link']
    list_filter = ['categories']
    search_fields = ['title', 'description']
    filter_horizontal = ['categories']
    list_per_page = 12
    save_on_top = True
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'description', 'categories', 'link')
        }),
        ('تصاویر', {
            'fields': ('thumbnail_picture', 'thumbnail_preview_field',
                       'main_picture', 'main_preview_field')
        }),
    )
    readonly_fields = ['thumbnail_preview_field', 'main_preview_field']

    def thumbnail_preview(self, obj):
        return image_preview(obj, 'thumbnail_picture', 60, 60)
    thumbnail_preview.short_description = 'بندانگشتی'

    def thumbnail_preview_field(self, obj):
        if obj.thumbnail_picture:
            return format_html('<img src="{}" style="max-width:250px; border-radius:10px;" />',
                               obj.thumbnail_picture.url)
        return '—'
    thumbnail_preview_field.short_description = 'پیش‌نمایش تصویر بندانگشتی'

    def main_preview_field(self, obj):
        if obj.main_picture:
            return format_html('<img src="{}" style="max-width:250px; border-radius:10px;" />',
                               obj.main_picture.url)
        return '—'
    main_preview_field.short_description = 'پیش‌نمایش تصویر اصلی'

    def display_categories(self, obj):
        return " | ".join([cat.name for cat in obj.categories.all()])
    display_categories.short_description = 'دسته‌بندی‌ها'


# ============================================================
# FreelanceRequest (فقط خواندنی)
# ============================================================
@admin.register(FreelanceRequest)
class FreelanceRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'rate_type', 'created_at']
    list_filter = ['rate_type', 'created_at']
    search_fields = ['name', 'email', 'proposal']
    readonly_fields = ['name', 'email', 'rate_type', 'special_offer', 'proposal', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 20
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# ============================================================
# JobRequest (فقط خواندنی)
# ============================================================
@admin.register(JobRequest)
class JobRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'job_type', 'salary_suggestion', 'created_at']
    list_filter = ['job_type', 'created_at']
    search_fields = ['name', 'email', 'proposal']
    readonly_fields = ['name', 'email', 'job_type', 'salary_suggestion', 'proposal', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 20
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# ============================================================
# Hire
# ============================================================
@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = ['title', 'rhetorical_question', 'background_preview']
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'rhetorical_question', 'description')
        }),
        ('تصویر', {
            'fields': ('background_image', 'background_preview_field')
        }),
    )
    readonly_fields = ['background_preview_field']

    def background_preview(self, obj):
        return image_preview(obj, 'background_image', 60, 40)
    background_preview.short_description = 'پس‌زمینه'

    def background_preview_field(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" style="max-width:300px; border-radius:10px;" />',
                               obj.background_image.url)
        return '—'
    background_preview_field.short_description = 'پیش‌نمایش تصویر'

    def has_add_permission(self, request):
        if Hire.objects.exists():
            return False
        return True


# ============================================================
# Testimonials
# ============================================================
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'title', 'customer_area_activity', 'photo_preview']
    list_editable = ['title']
    list_filter = ['title', 'customer_area_activity']
    search_fields = ['customer_name', 'description']
    list_per_page = 20
    save_on_top = True

    def photo_preview(self, obj):
        return image_preview(obj, 'customer_photo', 40, 40)
    photo_preview.short_description = 'عکس'

    def save_model(self, request, obj, form, change):
        # وقتی یکی از نظرات ذخیره میشه، عنوان برای همه‌ی نظرات یکسان بشه
        if obj.title:
            Testimonials.objects.exclude(pk=obj.pk).update(title=obj.title)
        super().save_model(request, obj, form, change)


# ============================================================
# Blog
# ============================================================
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'category_title', 'topic', 'photo_preview', 'created_at']
    list_editable = ['category_title']
    list_filter = ['category_title', 'topic', 'created_at']
    search_fields = ['post_title', 'description']
    date_hierarchy = 'created_at'
    list_per_page = 15
    save_on_top = True

    def photo_preview(self, obj):
        return image_preview(obj, 'post_photo', 50, 50)
    photo_preview.short_description = 'عکس'

    def save_model(self, request, obj, form, change):
        # وقتی یکی از پست‌ها ذخیره میشه، عنوان بخش برای همه‌ی پست‌ها یکسان بشه
        if obj.category_title:
            Blog.objects.exclude(pk=obj.pk).update(category_title=obj.category_title)
        super().save_model(request, obj, form, change)


# ============================================================
# FooterSocialLink
# ============================================================
@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order', 'icon_preview']
    list_editable = ['order']
    search_fields = ['name', 'url']
    ordering = ['order']
    list_per_page = 20

    def icon_preview(self, obj):
        return image_preview(obj, 'social_icon', 30, 30)
    icon_preview.short_description = 'آیکون'


# ============================================================
# Footer
# ============================================================
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'copyright_text']
    filter_horizontal = ['social_links']
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('site_name', 'copyright_text')
        }),
        ('شبکه‌های اجتماعی', {
            'fields': ('social_links',)
        }),
    )

    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return True