# Django Resume Portfolio

> A production-ready personal portfolio & resume website built with Django 5.2 LTS, featuring a modular architecture, dynamic admin panel, and bilingual documentation.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/django-5.2%20LTS-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📖 Overview

A fully-featured, modular portfolio website designed with production-grade practices. Every section is **dynamically managed** through Django's admin panel, so no code changes are required to update your content.

### Why this project stands out

- **Modular architecture** — business logic separated into `config/` and `apps/`, following Django best practices for scalability.
- **Environment isolation** — split settings for development and production (`local.py` / `production.py`).
- **Secure by default** — `.env`-based configuration, CSRF protection, and no hard-coded secrets.
- **Optimized ORM** — `prefetch_related()` and `select_related()` to eliminate N+1 queries.
- **Professional admin panel** — image previews, inline editors, singleton enforcement, and read-only request logs.
- **Ready for deployment** — Gunicorn + WhiteNoise + PostgreSQL support out of the box.

---

## ✨ Features

| Section | Description |
| :--- | :--- |
| **Hero** | Dynamic avatar, name, job title, and resume download button |
| **About** | Quote, bio, signature, social links, and skill progress circles |
| **Achievement** | Combined timeline of work & education, sorted chronologically |
| **Services** | Custom SVG icons with configurable background colors |
| **Projects** | Filterable gallery with multi-category support (ManyToMany) |
| **Hire** | Call-to-action section with custom background image |
| **Testimonials** | Customer feedback carousel with photo & activity |
| **Blog** | Post carousel with auto-truncated descriptions |
| **Footer** | Configurable site name, copyright, and social links |
| **Contact Modal** | Dual-form (Freelance / Job) with CSRF protection and validation |

---

## 🛠️ Tech Stack

**Backend**
- Django 5.2 LTS
- Python 3.10+
- SQLite (dev) / PostgreSQL (production)
- Gunicorn (WSGI server)
- WhiteNoise (static file serving)

**Frontend**
- Tailwind CSS 3.4 (via CDN)
- Vanilla JavaScript (jQuery for legacy components)
- Owl Carousel, AOS, Fancybox, MixItUp

**DevOps & Utilities**
- `python-decouple` — environment variable management
- `Pillow` — image handling
- `psycopg2-binary` — PostgreSQL adapter

---

## 🏗️ Architecture

This project follows a **domain-oriented structure** where all Django apps live under an `apps/` package, and configuration is isolated in `config/`.

```
django-resume-portfolio/
├── config/                      # Project configuration
│   ├── settings/
│   │   ├── base.py              # Shared settings
│   │   ├── local.py             # Development (DEBUG=True)
│   │   └── production.py        # Production (PostgreSQL, DEBUG=False)
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
│
├── apps/                        # All Django applications
│   ├── core/                    # Main app (all models, views, admin)
│   │   ├── models.py            # 14 domain models
│   │   ├── views.py             # Home + Contact views
│   │   ├── admin.py             # Professional admin configuration
│   │   ├── urls.py              # App-level routes
│   │   └── apps.py              # CoreConfig
│   ├── portfolio/               # Reserved for future (Model-only)
│   ├── blog/                    # Reserved for future (Model-only)
│   └── testimonials/            # Reserved for future (Model-only)
│
├── templates/                   # Global template root
│   ├── base.html                # Layout with named blocks
│   ├── index.html               # Homepage composition
│   └── includes/                # 15 partial templates
│       ├── head.html
│       ├── header.html
│       ├── mobile_menu.html
│       ├── hero.html
│       ├── about.html
│       ├── achievement.html
│       ├── services.html
│       ├── projects.html
│       ├── hire.html
│       ├── testimonials.html
│       ├── blog.html
│       ├── footer.html
│       ├── modal_hire.html
│       └── scripts.html
│
├── static/                      # Static assets (CSS/JS/IMG)
├── media/                       # User-uploaded files (git-ignored)
├── .env                         # Environment variables (git-ignored)
├── manage.py
└── requirements.txt
```

### Why `apps/` instead of the project root?

- **Cleaner imports** — `from apps.core.models import About` clearly signals a project-local app.
- **Scalability** — adding a new app never clutters the project root.
- **Familiar pattern** — matches the structure used by many large Django codebases.

---

## 🚀 Quick Start

### Prerequisites

- Python **3.10+**
- pip
- Git
- (Optional) PostgreSQL 13+ for production

### 1. Clone the repository

```bash
git clone https://github.com/mohammadiparsa2011/django-resume-portfolio.git
cd django-resume-portfolio
```

### 2. Create & activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-super-secret-key-change-me
DEBUG=True

# Only required for production (PostgreSQL)
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=strong-password
DB_HOST=localhost
DB_PORT=5432
```

> 💡 **Tip:** Generate a `SECRET_KEY` with:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 5. Apply migrations & create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** for the site and **http://127.0.0.1:8000/admin** for the admin panel.

---

## ⚙️ Settings Strategy

The settings module is **split by environment**:

| File | Purpose | Loaded via |
| :--- | :--- | :--- |
| `config/settings/base.py` | Common configuration | — |
| `config/settings/local.py` | `DEBUG=True`, permissive hosts | `manage.py` (default) |
| `config/settings/production.py` | `DEBUG=False`, PostgreSQL, strict hosts | Gunicorn / WSGI |

`manage.py` defaults to `config.settings.local`, so you can simply run:

```bash
python manage.py runserver
```

For production, override the module:

```bash
DJANGO_SETTINGS_MODULE=config.settings.production gunicorn config.wsgi:application
```

---

## 🚢 Deployment

### Static files

```bash
python manage.py collectstatic --no-input --settings=config.settings.production
```

WhiteNoise will serve them automatically through Gunicorn.

### Gunicorn

```bash
gunicorn config.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=config.settings.production \
    --bind 0.0.0.0:8000 \
    --workers 3
```

### Checklist before going live

- [ ] `SECRET_KEY` is unique and stored in `.env`.
- [ ] `DEBUG=False` in production.
- [ ] `ALLOWED_HOSTS` lists your domain(s).
- [ ] PostgreSQL credentials are set in `.env`.
- [ ] `collectstatic` has been run.
- [ ] `python manage.py check --deploy` passes without warnings.
- [ ] HTTPS is enforced (`SECURE_SSL_REDIRECT = True`).

---

## 🔐 Environment Variables

| Variable | Required | Description |
| :--- | :--- | :--- |
| `SECRET_KEY` | ✅ | Django's cryptographic key |
| `DEBUG` | ✅ | `True` in dev, `False` in prod |
| `DB_NAME` | prod only | PostgreSQL database name |
| `DB_USER` | prod only | PostgreSQL user |
| `DB_PASSWORD` | prod only | PostgreSQL password |
| `DB_HOST` | prod only | Database host (default: `localhost`) |
| `DB_PORT` | prod only | Database port (default: `5432`) |

---

## 🧠 Key Design Decisions

### 1. Why a single `core` app instead of many?

The project is intentionally scoped as a **single-domain portfolio**. Splitting it into `portfolio`, `blog`, `testimonials` apps right away would add ceremony without benefit. The `apps/portfolio`, `apps/blog`, `apps/testimonials` packages exist only as **future placeholders** — if the project grows, migration is a matter of moving models over.

### 2. Why `first()` for singletons?

Models like `HeroSection`, `About`, `Hire`, and `Footer` should have **exactly one record**. Enforcing this at the admin level (`has_add_permission`) and reading via `objects.first()` keeps views simple and prevents accidental duplicates.

### 3. Why `ManyToManyField` for project categories?

A project can belong to **multiple categories** (e.g., both "Web" and "Graphics"). `ManyToManyField` models this naturally and integrates with the frontend filter via slug-based CSS classes.

### 4. Why `prefetch_related()`?

The About section displays social links, skills, and skill icons — three levels of related data. Without `prefetch_related`, Django fires one query per relation per row (**N+1 problem**). With it, everything is fetched in 3-4 queries total.

### 5. Why a custom admin for request logs?

`FreelanceRequest` and `JobRequest` are **user-submitted data** — they should be readable but immutable. `readonly_fields` + `has_change_permission = False` + `has_add_permission = False` guarantee the admin user can only view and delete them.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.  
Please open an issue first to discuss significant changes.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "feat: add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👤 Author

**Parsa Mohammadi**

- GitHub: [@mohammadiparsa2011](https://github.com/mohammadiparsa2011)
- LinkedIn: [mohammadiparsa2011](https://linkedin.com/in/mohammadiparsa2011)
- Website: [parsanova.ir](https://parsanova.ir)

---

## ⭐ Support

If this project helped you, please consider giving it a **star** — it means a lot!

---
---

# 🇮🇷 نسخه‌ی فارسی

> یک وب‌سایت نمونه‌کار و رزومه‌ی شخصی، آماده برای انتشار، ساخته‌شده با **جنگو ۵.۲ LTS**، با معماری ماژولار، پنل ادمین حرفه‌ای و مستندات دوزبانه.

[![نسخه پایتون](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![نسخه جنگو](https://img.shields.io/badge/django-5.2%20LTS-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![مجوز](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![سبک کد](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📖 معرفی

یک وب‌سایت نمونه‌کار و رزومه‌ی شخصی، ساخته‌شده با **جنگو ۵.۲ LTS**، با معماری ماژولار، پنل ادمین حرفه‌ای و مستندات دوزبانه. همه‌ی بخش‌ها از طریق پنل ادمین قابل مدیریت هستن و نیازی به تغییر کد ندارن.

### چرا این پروژه متمایزه؟

- **معماری ماژولار** — منطق پروژه در `config/` و `apps/` جدا شده.
- **جداسازی محیط‌ها** — تنظیمات جداگانه برای توسعه و تولید.
- **امنیت از پایه** — استفاده از `.env` و محافظت CSRF.
- **بهینه‌سازی ORM** — حذف مشکل N+1 با `prefetch_related`.
- **پنل ادمین حرفه‌ای** — پیش‌نمایش تصویر، ویرایشگر درون‌خطی، جلوگیری از رکورد تکراری.
- **آماده برای انتشار** — Gunicorn + WhiteNoise + PostgreSQL.

---

## ✨ ویژگی‌ها

| بخش | توضیح |
| :--- | :--- |
| **هیرو** | آواتار، نام، عنوان شغلی و دکمه‌ی دانلود رزومه |
| **درباره** | نقل قول، بیوگرافی، امضا، شبکه‌های اجتماعی و مهارت‌ها |
| **سوابق** | تایم‌لاین ترکیبی کاری و تحصیلی، مرتب‌شده بر اساس سال |
| **خدمات** | آیکون‌های SVG سفارشی با رنگ پس‌زمینه‌ی قابل تنظیم |
| **پروژه‌ها** | گالری قابل فیلتر با پشتیبانی از چند دسته‌بندی |
| **همکاری** | بخش دعوت به همکاری با تصویر پس‌زمینه‌ی سفارشی |
| **نظرات** | اسلایدر نظرات مشتریان با عکس و حوزه‌ی فعالیت |
| **وبلاگ** | اسلایدر پست‌ها با توضیحات کوتاه‌شده |
| **فوتر** | نام سایت، کپی‌رایت و شبکه‌های اجتماعی قابل تنظیم |
| **مودال تماس** | فرم دوگانه (فریلنسر / شغل) با محافظت CSRF |

---

## 🛠️ تکنولوژی‌ها

**بک‌اند**
- جنگو ۵.۲ LTS
- پایتون ۳.۱۰+
- SQLite (توسعه) / PostgreSQL (تولید)
- Gunicorn (سرور WSGI)
- WhiteNoise (سرو فایل استاتیک)

**فرانت‌اند**
- Tailwind CSS 3.4 (از طریق CDN)
- جاوااسکریپت خالص (jQuery برای کامپوننت‌های قدیمی)
- Owl Carousel, AOS, Fancybox, MixItUp

**ابزارها**
- `python-decouple` — مدیریت متغیرهای محیطی
- `Pillow` — پردازش تصویر
- `psycopg2-binary` — درایور PostgreSQL

---

## 🏗️ معماری

این پروژه از یک **ساختار دامنه‌محور** پیروی می‌کنه که همه‌ی اپ‌های جنگو در پوشه‌ی `apps/` قرار دارن و تنظیمات در `config/` جدا شده.

```
django-resume-portfolio/
├── config/                      # تنظیمات پروژه
│   ├── settings/
│   │   ├── base.py              # تنظیمات مشترک
│   │   ├── local.py             # توسعه (DEBUG=True)
│   │   └── production.py        # تولید (PostgreSQL, DEBUG=False)
│   ├── urls.py                  # روت URLهای اصلی
│   ├── wsgi.py                  # نقطه‌ی ورود WSGI
│   └── asgi.py                  # نقطه‌ی ورود ASGI
│
├── apps/                        # همه‌ی اپ‌های جنگو
│   ├── core/                    # اپ اصلی (همه‌ی مدل‌ها، ویوها، ادمین)
│   │   ├── models.py            # ۱۴ مدل دامنه
│   │   ├── views.py             # ویوهای خانه + تماس
│   │   ├── admin.py             # پیکربندی حرفه‌ای ادمین
│   │   ├── urls.py              # مسیرهای اپ
│   │   └── apps.py              # CoreConfig
│   ├── portfolio/               # رزرو برای آینده (فقط مدل)
│   ├── blog/                    # رزرو برای آینده (فقط مدل)
│   └── testimonials/            # رزرو برای آینده (فقط مدل)
│
├── templates/                   # ریشه‌ی قالب‌ها
│   ├── base.html                # لایه‌ی اصلی با بلاک‌ها
│   ├── index.html               # ترکیب صفحه اصلی
│   └── includes/                # ۱۵ فایل جزئی
│       ├── head.html
│       ├── header.html
│       ├── mobile_menu.html
│       ├── hero.html
│       ├── about.html
│       ├── achievement.html
│       ├── services.html
│       ├── projects.html
│       ├── hire.html
│       ├── testimonials.html
│       ├── blog.html
│       ├── footer.html
│       ├── modal_hire.html
│       └── scripts.html
│
├── static/                      # فایل‌های استاتیک (CSS/JS/IMG)
├── media/                       # فایل‌های آپلودی (در گیت نیست)
├── .env                         # متغیرهای محیطی (در گیت نیست)
├── manage.py
└── requirements.txt
```

### چرا پوشه‌ی `apps/`؟

- **importهای تمیزتر** — `from apps.core.models import About` به‌وضوح نشون می‌ده اپ پروژه‌ایه.
- **توسعه‌پذیری** — اضافه کردن اپ جدید، ریشه‌ی پروژه رو شلوغ نمی‌کنه.
- **الگوی آشنا** — مطابق ساختار بسیاری از پروژه‌های بزرگ جنگو.

---

## 🚀 نصب سریع

### پیش‌نیازها

- پایتون **۳.۱۰+**
- pip
- Git
- (اختیاری) PostgreSQL 13+ برای تولید

### ۱. کلون کردن مخزن

```bash
git clone https://github.com/mohammadiparsa2011/django-resume-portfolio.git
cd django-resume-portfolio
```

### ۲. ساخت و فعال‌سازی محیط مجازی

**ویندوز (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**ویندوز (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**لینوکس / مک:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### ۳. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### ۴. تنظیم متغیرهای محیطی

فایل `.env` در ریشه‌ی پروژه بساز:

```env
SECRET_KEY=your-super-secret-key-change-me
DEBUG=True

# فقط برای تولید (PostgreSQL)
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=strong-password
DB_HOST=localhost
DB_PORT=5432
```

> 💡 **نکته:** برای ساخت `SECRET_KEY` از این دستور استفاده کن:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### ۵. اجرای مهاجرت‌ها و ساخت سوپر‌یوزر

```bash
python manage.py migrate
python manage.py createsuperuser
```

### ۶. اجرای سرور توسعه

```bash
python manage.py runserver
```

آدرس سایت: **http://127.0.0.1:8000**  
آدرس پنل ادمین: **http://127.0.0.1:8000/admin**

---

## ⚙️ استراتژی تنظیمات

ماژول تنظیمات بر اساس محیط **جدا شده**:

| فایل | کاربرد | بارگذاری از طریق |
| :--- | :--- | :--- |
| `config/settings/base.py` | تنظیمات مشترک | — |
| `config/settings/local.py` | `DEBUG=True`، میزبان‌های آزاد | `manage.py` (پیش‌فرض) |
| `config/settings/production.py` | `DEBUG=False`، PostgreSQL، میزبان‌های محدود | Gunicorn / WSGI |

`manage.py` به‌طور پیش‌فرض از `config.settings.local` استفاده می‌کنه:

```bash
python manage.py runserver
```

برای تولید، ماژول رو override کن:

```bash
DJANGO_SETTINGS_MODULE=config.settings.production gunicorn config.wsgi:application
```

---

## 🚢 انتشار

### فایل‌های استاتیک

```bash
python manage.py collectstatic --no-input --settings=config.settings.production
```

WhiteNoise از طریق Gunicorn اون‌ها رو سرو می‌کنه.

### Gunicorn

```bash
gunicorn config.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=config.settings.production \
    --bind 0.0.0.0:8000 \
    --workers 3
```

### چک‌لیست قبل از انتشار

- [ ] `SECRET_KEY` یکتا و در `.env` ذخیره شده.
- [ ] `DEBUG=False` در تولید.
- [ ] `ALLOWED_HOSTS` دامنه‌هات رو لیست کرده.
- [ ] اعتبارنامه‌های PostgreSQL در `.env` تنظیم شده.
- [ ] `collectstatic` اجرا شده.
- [ ] `python manage.py check --deploy` بدون هشدار پاس می‌شه.
- [ ] HTTPS اجباری شده (`SECURE_SSL_REDIRECT = True`).

---

## 🔐 متغیرهای محیطی

| متغیر | ضروری | توضیح |
| :--- | :--- | :--- |
| `SECRET_KEY` | ✅ | کلید رمزنگاری جنگو |
| `DEBUG` | ✅ | `True` در توسعه، `False` در تولید |
| `DB_NAME` | فقط تولید | نام دیتابیس PostgreSQL |
| `DB_USER` | فقط تولید | کاربر PostgreSQL |
| `DB_PASSWORD` | فقط تولید | رمز PostgreSQL |
| `DB_HOST` | فقط تولید | میزبان دیتابیس (پیش‌فرض: `localhost`) |
| `DB_PORT` | فقط تولید | پورت دیتابیس (پیش‌فرض: `5432`) |

---

## 🧠 تصمیم‌های کلیدی طراحی

### ۱. چرا یک اپ `core` به‌جای چند اپ؟

پروژه به‌طور عمدی به‌عنوان یک **نمونه‌کار شخصی تک‌دامنه** طراحی شده. تقسیمش به `portfolio`, `blog`, `testimonials` از همون ابتدا، بدون فایده پیچیدگی اضافه می‌کنه. پکیج‌های `apps/portfolio`, `apps/blog`, `apps/testimonials` فقط به‌عنوان **جایگاه آینده** وجود دارن — اگه پروژه رشد کرد، مهاجرت فقط جابه‌جا کردن مدل‌هاست.

### ۲. چرا `first()` برای Singletonها؟

مدل‌هایی مثل `HeroSection`, `About`, `Hire`, `Footer` باید **فقط یک رکورد** داشته باشن. اجبار در سطح ادمین (`has_add_permission`) و خوندن با `objects.first()`، ویوها رو ساده نگه می‌داره و از رکورد تکراری جلوگیری می‌کنه.

### ۳. چرا `ManyToManyField` برای دسته‌بندی پروژه‌ها؟

یک پروژه می‌تونه به **چند دسته** تعلق داشته باشه (مثلاً هم وب، هم گرافیک). `ManyToManyField` این رو به‌طور طبیعی مدل می‌کنه و با فیلتر فرانت‌اند از طریق کلاس‌های CSS مبتنی بر slug یکپارچه می‌شه.

### ۴. چرا `prefetch_related()`؟

بخش درباره، شبکه‌های اجتماعی، مهارت‌ها و آیکون‌های مهارت‌ها رو نمایش می‌ده — سه سطح داده‌ی مرتبط. بدون `prefetch_related`، جنگو به ازای هر ردیف یه کوئری جدا می‌زنه (**مشکل N+1**). با اون، همه‌چیز در ۳-۴ کوئری لود می‌شه.

### ۵. چرا ادمین سفارشی برای لاگ درخواست‌ها؟

`FreelanceRequest` و `JobRequest` **داده‌ی ارسالی کاربر** هستن — باید خواندنی ولی غیرقابل‌تغییر باشن. ترکیب `readonly_fields` + `has_change_permission = False` + `has_add_permission = False` تضمین می‌کنه که کاربر ادمین فقط می‌تونه ببینه یا حذف کنه.

---

## 🤝 مشارکت

از مشارکت، گزارش باگ و پیشنهاد ویژگی استقبال می‌شود.  
لطفاً قبل از تغییرات مهم، یک Issue باز کنید.

۱. مخزن رو Fork کنید  
۲. برنچ ویژگی بسازید: `git checkout -b feature/amazing-feature`  
۳. کامیت کنید: `git commit -m "feat: add amazing feature"`  
۴. پوش کنید: `git push origin feature/amazing-feature`  
۵. یک Pull Request باز کنید

---

## 📄 مجوز

تحت مجوز **MIT** منتشر شده است. برای جزئیات بیشتر فایل [`LICENSE`](LICENSE) را ببینید.

---

## 👤 نویسنده

**پارسا محمدی**

- گیت‌هاب: [@mohammadiparsa2011](https://github.com/mohammadiparsa2011)
- لینکدین: [mohammadiparsa2011](https://linkedin.com/in/mohammadiparsa2011)
- وب‌سایت: [parsanova.ir](https://parsanova.ir)

---

## ⭐ حمایت

اگر این پروژه بهت کمک کرد، لطفاً بهش **ستاره** بده — خیلی ارزش داره!