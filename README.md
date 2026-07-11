# django-resume-portfolio

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-5.2-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)

---

This is my personal portfolio and resume website that I built with Django 5.2 LTS. I wanted a clean, modern, and fully responsive design to showcase my skills, projects, and blog posts. It’s ready to deploy and easy to customize.

I’ve tried to keep the code clean and the structure modular so that adding new features later won’t be a headache.

## ✨ What’s inside?

- **Modern UI** – responsive and works on all devices
- **Blog** – you can write, edit, and delete posts
- **Project Showcase** – filter projects by category
- **Testimonials** – manage client feedback easily
- **Environment variables** – secure settings with `.env`
- **Ready for deployment** – comes with Gunicorn and WhiteNoise

## 🛠️ Tech Stack

- **Backend:** Django 5.2 LTS, Python 3.10+
- **Frontend:** Tailwind CSS, HTML5, JavaScript
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Deployment:** Gunicorn, WhiteNoise, Docker-ready
- **Utilities:** python-decouple, Pillow

## 🚀 How to run it locally

1. Clone the repo:
   ```bash
   git clone https://github.com/mohammadiparsa2011/django-resume-portfolio.git
   cd django-resume-portfolio
   ```

2. Set up a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your `SECRET_KEY` and `DEBUG` settings (I’ve provided a sample in the repo).

5. Run migrations and start the server:
   ```bash
   python manage.py migrate --settings=config.settings.local
   python manage.py runserver --settings=config.settings.local
   ```

6. Open your browser and go to `http://127.0.0.1:8000`

## 📁 Project Structure

I’ve organized the project so that all the main logic stays in the `core` app, while other apps (like `portfolio`, `blog`, `testimonials`) are ready for future development. The templates are in the root `templates/` folder for easy access.

```
django-resume-portfolio/
├── config/           # Settings (separated for dev/prod)
├── apps/             # All Django apps
│   ├── core/         # Main app (views, urls)
│   ├── portfolio/    # Models only (for future)
│   ├── blog/         # Models only (for future)
│   └── testimonials/ # Models only (for future)
├── templates/        # HTML templates (base, index, includes)
├── static/           # CSS, JS, images
└── media/            # User-uploaded files
```

## 🤝 Contribute

If you find a bug or have a suggestion, feel free to open an issue or submit a pull request. I’m always open to improving this project.

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 👤 About Me

I’m **Parsa Mohammadi**, a developer who enjoys building clean and functional web applications. You can find me on:

- GitHub: [@mohammadiparsa2011](https://github.com/mohammadiparsa2011)
- LinkedIn: [my LinkedIn profile](https://linkedin.com/in/your-profile)
- Website: [my personal site](https://your-site.com)

---

⭐ If this project helps you or you like it, please give it a star! It means a lot.

---

## 🇮🇷 نسخه‌ی فارسی

# نمونه‌کار شخصی با جنگو

[![نسخه پایتون](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![نسخه جنگو](https://img.shields.io/badge/django-5.2-green.svg)](https://djangoproject.com)
[![مجوز](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)

---

این وب‌سایت نمونه‌کار و رزومه‌ی شخصی‌ام است که با جنگو ۵.۲ LTS ساختم. هدفم این بود که یک طراحی مدرن، تمیز و کاملاً واکنش‌گرا داشته باشم تا مهارت‌ها، پروژه‌ها و نوشته‌های وبلاگم را به‌خوبی نمایش دهد. پروژه آماده‌ی انتشار است و به‌راحتی قابل شخصی‌سازی می‌باشد.

سعی کردم کدها تمیز و ساختار ماژولار باشد تا اضافه کردن ویژگی‌های جدید در آینده دردسر نشود.

## ✨ چه چیزهایی داخلش هست؟

- **ظاهر مدرن** – واکنش‌گرا و سازگار با همه‌ی دستگاه‌ها
- **وبلاگ** – می‌توانید پست بنویسید، ویرایش و حذف کنید
- **نمایش پروژه‌ها** – فیلتر پروژه‌ها بر اساس دسته‌بندی
- **نظرات مشتریان** – مدیریت آسان بازخوردها
- **متغیرهای محیطی** – تنظیمات امن با `.env`
- **آماده برای انتشار** – همراه با Gunicorn و WhiteNoise

## 🛠️ تکنولوژی‌ها

- **بک‌اند:** جنگو ۵.۲ LTS، پایتون ۳.۱۰+
- **فرانت‌اند:** Tailwind CSS، HTML5، جاوااسکریپت
- **دیتابیس:** SQLite (توسعه) / PostgreSQL (تولید)
- **انتشار:** Gunicorn، WhiteNoise، آماده‌ی Docker
- **ابزارها:** python-decouple، Pillow

## 🚀 چطور اجرا کنم؟

1. کلون کردن مخزن:
   ```bash
   git clone https://github.com/mohammadiparsa2011/django-resume-portfolio.git
   cd django-resume-portfolio
   ```

2. ساخت و فعال‌سازی محیط مجازی:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # در ویندوز: .venv\Scripts\activate
   ```

3. نصب وابستگی‌ها:
   ```bash
   pip install -r requirements.txt
   ```

4. ساخت فایل `.env` و اضافه کردن `SECRET_KEY` و `DEBUG` (نمونه‌اش در مخزن هست).

5. اجرای مهاجرت‌ها و سرور:
   ```bash
   python manage.py migrate --settings=config.settings.local
   python manage.py runserver --settings=config.settings.local
   ```

6. مرورگر را باز کنید و بروید به `http://127.0.0.1:8000`

## 📁 ساختار پروژه

پروژه را طوری سازماندهی کردم که تمام منطق اصلی در اپ `core` قرار دارد و اپ‌های دیگر (مانند `portfolio`، `blog`، `testimonials`) برای توسعه‌ی آینده آماده هستند. قالب‌ها هم در پوشه‌ی ریشه `templates/` قرار دارند تا دسترسی آسان‌تر باشد.

```
django-resume-portfolio/
├── config/           # تنظیمات (جدا برای توسعه/تولید)
├── apps/             # همه‌ی اپ‌های جنگو
│   ├── core/         # اپ اصلی (ویوها، URLها)
│   ├── portfolio/    # فقط مدل‌ها (برای آینده)
│   ├── blog/         # فقط مدل‌ها (برای آینده)
│   └── testimonials/ # فقط مدل‌ها (برای آینده)
├── templates/        # قالب‌های HTML
├── static/           # فایل‌های CSS، JS، تصاویر
└── media/            # فایل‌های آپلودی کاربران
```

## 🤝 مشارکت

اگر باگی پیدا کردید یا پیشنهادی دارید، خوشحال می‌شوم یک Issue باز کنید یا Pull Request بفرستید. همیشه برای بهبود این پروژه باز هستم.

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است – برای جزئیات بیشتر فایل [LICENSE](LICENSE) را ببینید.

---

## 👤 درباره‌ی من

من **پارسا محمدی** هستم، یک توسعه‌دهنده که از ساختن اپلیکیشن‌های وب تمیز و کاربردی لذت می‌برد. می‌توانید من را در:

- گیت‌هاب: [@mohammadiparsa2011](https://github.com/mohammadiparsa2011)
- لینکدین: [پروفایل لینکدین من](https://linkedin.com/in/your-profile)
- وب‌سایت: [سایت شخصی من](https://your-site.com)

---

⭐ اگر این پروژه به شما کمک کرد یا از آن خوشتان آمد، لطفاً به آن ستاره دهید! خیلی ارزش دارد.
