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
        verbose_name = 'ماژول اطلاعات شخصی'
        verbose_name_plural = 'اطلاعات شخصی'

class ServicesSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان توانایی')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='SVG کد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ماژول توانایی‌ها'
        verbose_name_plural = "توانایی‌ها"