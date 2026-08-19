from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroSection, ServicesSection, About, WorkExperience, EducationExperience, PortfolioItem, PortfolioCategory


def home_view(request):
    """صفحه اصلی سایت"""
    hero_section = HeroSection.objects.first()
    services_section = ServicesSection.objects.all()
    about = About.objects.first()
    work_experiences = WorkExperience.objects.all()
    education_experiences = EducationExperience.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    portfo_categories = PortfolioCategory.objects.all()

    context = {
        'hero_section' : hero_section,
        'services' : services_section,
        'about' : about,
        'work_experiences' : work_experiences,
        'education_experiences' : education_experiences,
        'portfolio_items': portfolio_items,
        'categories': portfo_categories,
    }
    return render(request, 'index.html', context)

def contact(request):
    # فعلاً فقط یک پیام ساده نشان می‌دهیم
    # بعداً می‌توانید ایمیل ارسال کنید یا داده‌ها را ذخیره نمایید
    return HttpResponse("فرم تماس با موفقیت ارسال شد! (این یک پاسخ موقت است)")

# سایر ویوها (در صورت نیاز)