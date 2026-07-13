from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    """صفحه اصلی سایت"""
    return render(request, 'index.html')

def contact(request):
    # فعلاً فقط یک پیام ساده نشان می‌دهیم
    # بعداً می‌توانید ایمیل ارسال کنید یا داده‌ها را ذخیره نمایید
    return HttpResponse("فرم تماس با موفقیت ارسال شد! (این یک پاسخ موقت است)")

# سایر ویوها (در صورت نیاز)