from django.db import models
from django.utils.text import slugify


class HeroSection(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    job_title = models.CharField(max_length=255, verbose_name='عنوان شغل')
    button_text = models.CharField(max_length=100, verbose_name='متن دکمه')
    avatar = models.ImageField(upload_to='hero/', verbose_name='تصویر آواتار(png)')
    resume_file = models.FileField(upload_to='hero/resume/', verbose_name='رزومه(pdf & image)', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اطلاعات شخصی'
        verbose_name_plural = 'اطلاعات شخصی'


class About(models.Model):
    quote = models.CharField(max_length=100, verbose_name="نقل قول")
    description = models.TextField(verbose_name='توضیحات')
    job_title = models.CharField(max_length=100, verbose_name='عنوان شغلی')
    name = models.CharField(max_length=100, verbose_name='نام کامل')
    signature = models.ImageField(upload_to='about/', verbose_name='امضا')
    main_image = models.ImageField(upload_to='about/', verbose_name='عکس اصلی')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'


class SocialLink(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='social_links', verbose_name='درباره')
    name = models.CharField(max_length=50, verbose_name='نام شبکه اجتماعی')
    icon = models.ImageField(upload_to='about/social/', verbose_name='آیکون شبکه اجتماعی')
    url = models.URLField(verbose_name='لینک شبکه اجتماعی')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه‌های اجتماعی'
        ordering = ['order']


class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills', verbose_name='درباره')
    title = models.CharField(max_length=100, verbose_name='عنوان مهارت')
    description = models.TextField(verbose_name='توضیحات')
    percentage = models.PositiveIntegerField(verbose_name='درصد تسلط(0 تا 100)')
    bg_color = models.CharField(max_length=20, verbose_name='رنگ پس زمینه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت‌ها'


class SkillIcon(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='icons', verbose_name='توانایی')
    icon_image = models.ImageField(upload_to='about/skill_icons/', verbose_name='تصویر آیکون')
    url = models.URLField(blank=True, null=True, verbose_name='لینک(اختیاری)')

    def __str__(self):
        return f"Icon for {self.skill.title}"

    class Meta:
        verbose_name = 'آیکون مهارت'
        verbose_name_plural = 'آیکون‌های مهارت'


class ServicesSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان توانایی')
    description = models.TextField(verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='SVG کد')
    bg_color = models.CharField(max_length=20, default='#84a59d', blank=True, null=True, verbose_name='رنگ پس زمینه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توانایی'
        verbose_name_plural = "توانایی‌ها"


class WorkExperience(models.Model):
    position = models.CharField(max_length=100, verbose_name='جایگاه شغلی')
    company = models.CharField(max_length=100, verbose_name='کمپانی')
    start_year = models.IntegerField(verbose_name='سال شروع همکاری')
    end_year = models.CharField(max_length=10, blank=True, null=True, verbose_name='سال پایان همکاری/الان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.position} در {self.company}'

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = "سوابق کاری"
        ordering = ['start_year']


class EducationExperience(models.Model):
    degree = models.CharField(max_length=100, verbose_name='مدرک تحصیلی')
    university = models.CharField(max_length=100, verbose_name='نام دانشگاه')
    start_year = models.IntegerField(verbose_name='سال شروع تحصیل')
    end_year = models.IntegerField(verbose_name='سال پایان تحصیل')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.degree} در {self.university}'

    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = "سوابق تحصیلی"
        ordering = ['start_year']


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name="اسلاگ (برای فیلتر)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    categories = models.ManyToManyField(PortfolioCategory, related_name='portfolio_items', verbose_name='دسته‌بندی‌ها')

    thumbnail_picture = models.ImageField(upload_to='portfolio/thumbnail/', verbose_name='تصویر بندانگشتی')
    main_picture = models.ImageField(upload_to='portfolio/main/', verbose_name='تصویر اصلی')
    link = models.URLField(blank=True, null=True, verbose_name='لینک نمونه کار')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'


class FreelanceRequest(models.Model):
    RATE_CHOICES = [
        ('fixed', 'نرخ ثابت'),
        ('hourly', 'نرخ ساعتی'),
    ]

    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    rate_type = models.CharField(max_length=10, choices=RATE_CHOICES, default='fixed', verbose_name='نوع نرخ')
    special_offer = models.CharField(max_length=255, blank=True, null=True, verbose_name='پیشنهاد ویژه')
    proposal = models.TextField(verbose_name='متن پیشنهاد')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "درخواست فریلنسری"
        verbose_name_plural = "درخواست‌های فریلنسری"
        ordering = ["-created_at"]


class JobRequest(models.Model):
    JOB_TYPE_CHOICES = [
        ('remote', 'شغل مجازی'),
        ('office', 'شغل اداری'),
    ]

    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default='remote', verbose_name='نوع شغل')
    salary_suggestion = models.CharField(max_length=255, blank=True, null=True, verbose_name='حقوق پیشنهادی')
    proposal = models.TextField(verbose_name='متن پیشنهاد')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "درخواست شغلی"
        verbose_name_plural = "درخواست‌های شغلی"
        ordering = ["-created_at"]


class Hire(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    rhetorical_question = models.CharField(max_length=150, verbose_name='سوال غیرمستقیم')
    description = models.TextField(verbose_name='توضیحات')
    background_image = models.ImageField(upload_to='hire/', verbose_name='تصویر پس زمینه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "همکاری"
        verbose_name_plural = "همکاری"


class Testimonials(models.Model):
    TITLE_CHOICES = [
        ('پژواک‌های درخشندگی', 'پژواک‌های درخشندگی'),
        ('نظرات مشتریان', 'نظرات مشتریان'),
        ('تجربه‌های همکاری', 'تجربه‌های همکاری'),
        ('چرا ما؟', 'چرا ما؟'),
    ]

    title = models.CharField(max_length=50, choices=TITLE_CHOICES, default='پژواک‌های درخشندگی', verbose_name='عنوان بخش')
    customer_name = models.CharField(max_length=100, verbose_name='نام مشتری')
    customer_area_activity = models.CharField(max_length=50, verbose_name='حوزه فعالیت مشتری')
    description = models.TextField(verbose_name='توضیحات')
    customer_photo = models.ImageField(upload_to='testimonials/', verbose_name='عکس مشتری', blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.customer_area_activity}"

    class Meta:
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظرات مشتریان"


class Blog(models.Model):
    CATEGORY_TITLE_CHOICES = [
        ('آخرین مطالب', 'آخرین مطالب'),
        ('وبلاگ', 'وبلاگ'),
        ('مجله', 'مجله'),
        ('مقالات', 'مقالات'),
    ]

    category_title = models.CharField(max_length=50, choices=CATEGORY_TITLE_CHOICES, default='آخرین مطالب', verbose_name='عنوان بخش وبلاگ')
    topic = models.CharField(max_length=50, verbose_name='موضوع پست')
    post_title = models.CharField(max_length=255, verbose_name='عنوان پست')
    description = models.TextField(verbose_name='متن پست')
    post_photo = models.ImageField(upload_to='blog/', verbose_name='عکس پست')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ['-created_at']


class FooterSocialLink(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام شبکه')
    url = models.URLField(verbose_name='لینک')
    social_icon = models.ImageField(upload_to='footer/social_link_icons/', blank=True, null=True, verbose_name='آیکون شبکه')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    def save(self, *args, **kwargs):
        if self.order == 0 or self.order is None:
            last_order = FooterSocialLink.objects.aggregate(
                models.Max('order')
            )['order__max']
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شبکه اجتماعی در فوتر'
        verbose_name_plural = 'شبکه‌های اجتماعی در فوتر'
        ordering = ['order']


class Footer(models.Model):
    site_name = models.CharField(max_length=100, default='parsanova', verbose_name='نام سایت')
    copyright_text = models.CharField(
        max_length=255,
        default='تمامی حقوق محفوظ است.',
        verbose_name='متن کپی‌رایت'
    )
    social_links = models.ManyToManyField(FooterSocialLink, blank=True, verbose_name='شبکه‌های اجتماعی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات فوتر'
        verbose_name_plural = 'تنظیمات فوتر'
