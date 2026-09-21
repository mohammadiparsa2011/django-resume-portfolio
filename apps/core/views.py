from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.db import transaction

from .models import (
    HeroSection, ServicesSection, About, WorkExperience, EducationExperience,
    PortfolioItem, PortfolioCategory, FreelanceRequest, JobRequest, Hire,
    Testimonials, Blog, Footer
)


# ============================================================
# 🎯 توابع کمکی (Helper Functions)
# ============================================================

def _build_experiences():
    """
    سوابق کاری و تحصیلی رو ترکیب می‌کنه و بر اساس سال مرتب می‌کنه.
    خروجی: لیستی از دیکشنری‌ها که هر کدوم شامل نوع، سال و اطلاعات است.
    """
    work_items = [
        {
            'type': 'work',
            'start_year': exp.start_year,
            'end_year': exp.end_year,
            'title': exp.company,
            'subtitle': exp.position,
            'description': exp.description,
        }
        for exp in WorkExperience.objects.all().order_by('start_year')
    ]

    education_items = [
        {
            'type': 'education',
            'start_year': exp.start_year,
            'end_year': exp.end_year,
            'title': exp.university,
            'subtitle': exp.degree,
            'description': exp.description,
        }
        for exp in EducationExperience.objects.all().order_by('start_year')
    ]

    # ترکیب و مرتب‌سازی بر اساس سال (قدیم به جدید)
    combined = work_items + education_items
    combined.sort(key=lambda x: (x['start_year'], x['type']))
    return combined


def _save_freelance_request(request):
    """ذخیره‌ی درخواست فریلنسری از روی داده‌های POST"""
    return FreelanceRequest.objects.create(
        name=request.POST.get('Name', '').strip(),
        email=request.POST.get('Email', '').strip(),
        rate_type=request.POST.get('rate_type', 'fixed'),
        special_offer=request.POST.get('special_offer', '').strip(),
        proposal=request.POST.get('your-comment', '').strip(),
    )


def _save_job_request(request):
    """ذخیره‌ی درخواست شغلی از روی داده‌های POST"""
    return JobRequest.objects.create(
        name=request.POST.get('Name', '').strip(),
        email=request.POST.get('Email', '').strip(),
        job_type=request.POST.get('job_type', 'remote'),
        salary_suggestion=request.POST.get('salary_suggestion', '').strip(),
        proposal=request.POST.get('your-comment', '').strip(),
    )


# ============================================================
# 🎯 ویو صفحه اصلی
# ============================================================

def home_view(request):
    """
    نمایش صفحه اصلی سایت با تمام بخش‌های داینامیک.
    از select_related و prefetch_related برای بهینه‌سازی کوئری‌ها استفاده می‌کنیم.
    """
    # --- بخش Hero ---
    hero_section = HeroSection.objects.first()

    # --- بخش About با روابط (شبکه‌های اجتماعی + مهارت‌ها + آیکون‌ها) ---
    about = (
        About.objects
        .prefetch_related(
            'social_links',
            'skills__icons',
        )
        .first()
    )

    # --- بخش Services ---
    services = ServicesSection.objects.all()

    # --- بخش Achievement (سوابق ترکیبی) ---
    experiences = _build_experiences()
    work_experiences = WorkExperience.objects.all().order_by('start_year')
    education_experiences = EducationExperience.objects.all().order_by('start_year')

    # --- بخش Portfolio ---
    portfolio_items = (
        PortfolioItem.objects
        .prefetch_related('categories')
        .all()
    )
    categories = PortfolioCategory.objects.all()

    # --- بخش Hire ---
    hire = Hire.objects.first()

    # --- بخش Testimonials ---
    testimonials = Testimonials.objects.all()

    # --- بخش Blog ---
    blog = Blog.objects.all().order_by('-created_at')

    # --- بخش Footer با روابط ---
    footer = (
        Footer.objects
        .prefetch_related('social_links')
        .first()
    )

    context = {
        # Hero
        'hero_section': hero_section,
        # About
        'about': about,
        # Services
        'services': services,
        # Achievement
        'experiences': experiences,
        'work_experiences': work_experiences,
        'education_experiences': education_experiences,
        # Portfolio
        'portfolio_items': portfolio_items,
        'categories': categories,
        # Hire
        'hire': hire,
        # Testimonials
        'testimonials': testimonials,
        # Blog
        'blog': blog,
        # Footer
        'footer': footer,
        'current_year': timezone.now().year,
    }
    return render(request, 'index.html', context)


# ============================================================
# 🎯 ویو فرم تماس (Contact)
# ============================================================

@csrf_protect
@require_http_methods(["GET", "POST"])
def contact(request):
    """
    مدیریت ارسال فرم‌های استخدام (فریلنسری و شغلی).
    - GET: ریدایرکت به صفحه اصلی
    - POST: ذخیره‌ی درخواست در دیتابیس و نمایش پیام
    """
    if request.method != 'POST':
        return redirect('core:index')

    # استخراج داده‌های مشترک
    name = request.POST.get('Name', '').strip()
    email = request.POST.get('Email', '').strip()

    # اعتبارسنجی ساده
    if not name or not email:
        messages.error(request, 'لطفاً نام و ایمیل خود را وارد کنید.')
        return redirect('core:index')

    try:
        with transaction.atomic():
            # تشخیص نوع فرم بر اساس فیلدهای منحصربه‌فرد
            if 'rate_type' in request.POST:
                # فرم فریلنسری
                _save_freelance_request(request)
                messages.success(request, '✅ درخواست فریلنسری شما با موفقیت ثبت شد!')

            elif 'job_type' in request.POST:
                # فرم شغلی
                _save_job_request(request)
                messages.success(request, '✅ درخواست شغلی شما با موفقیت ثبت شد!')

            else:
                messages.error(request, '❌ خطا در تشخیص نوع فرم!')

    except Exception as e:
        messages.error(request, f'❌ خطا در ثبت درخواست: {str(e)}')

    return redirect('core:index')