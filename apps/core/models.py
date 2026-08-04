from django.db import models

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

class ServicesSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان توانایی')
    description = models.TextField(verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='SVG کد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توانایی'
        verbose_name_plural = "توانایی‌ها"

class About(models.Model):
    quote = models.CharField(max_length=100, verbose_name="نقل قول")
    description = models.TextField(verbose_name='توضیحات')
    job_title = models.CharField(max_length=100, verbose_name='عنوان شغلی')
    name = models.CharField(max_length=100, verbose_name='نام کامل')
    signature = models.ImageField(upload_to='about/', verbose_name='امضا')
    main_image = models.ImageField(upload_to='about/', verbose_name='عکس اصلی')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'

class SocialLink(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='social_links', verbose_name='درباره')
    name = models.CharField(max_length=50, verbose_name='نام شبکه اجتماعی')
    icon = models.ImageField(upload_to='about/social/')
    url = models.URLField(verbose_name='لینک شبکه اجتماعی')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه‌های اجتماعی'

class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills', verbose_name='درباره')
    title = models.CharField(max_length=100, verbose_name='عنوان مهارت')
    description = models.TextField(verbose_name='توضیحات')
    percentage = models.PositiveIntegerField(verbose_name='درصد تسلط(0 تا 100)')
    bg_color = models.CharField(max_length=20, verbose_name='رنگ پس زمینه')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت‌ها'

class SkillIcon(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='icons', verbose_name='توانایی')
    icon_image = models.ImageField(upload_to='about/skill_icons/', verbose_name='تصویر آیکون')
    url = models.URLField(blank=True, null=True, verbose_name='لینک(اختیاری)')

    def __str__(self):
        return f"Icon for {self.skill.title}"

    class Meta():
        verbose_name = 'آیکون مهارت'
        verbose_name_plural = 'آیکون‌های مهارت'