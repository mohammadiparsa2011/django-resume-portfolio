from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroSection, ServicesSection


def home_view(request):
    """صفحه اصلی سایت"""
    hero_section = HeroSection.objects.first()
    services_section = ServicesSection.objects.all()

    context = {
        'hero_section' : hero_section,
        'services' : services_section,
    }
    return render(request, 'index.html', context)

def contact(request):
    # فعلاً فقط یک پیام ساده نشان می‌دهیم
    # بعداً می‌توانید ایمیل ارسال کنید یا داده‌ها را ذخیره نمایید
    return HttpResponse("فرم تماس با موفقیت ارسال شد! (این یک پاسخ موقت است)")

# سایر ویوها (در صورت نیاز)