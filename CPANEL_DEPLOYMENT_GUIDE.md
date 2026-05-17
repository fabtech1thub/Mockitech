# MOCKITech Django Project - cPanel Deployment Guide

## 🚀 Quick Start

1. **Run the deployment script:**
   ```bash
   python deploy_to_cpanel.py
   ```

2. **Update your domain in settings.py:**
   - Open `mockitech/settings.py`
   - Replace `'yourdomain.com'` with your actual domain

3. **Zip your project:**
   - Exclude: `.git`, `.venv`, `__pycache__`, `*.pyc`
   - Include: All other files and folders

## 📋 cPanel Setup Steps

### Step 1: Upload Files
1. Log in to cPanel
2. Go to **File Manager**
3. Navigate to your desired directory (e.g., `/home/username/`)
4. Upload and extract your project zip file

### Step 2: Setup Python App
1. In cPanel, find **Setup Python App** (under "Software")
2. Click **Create Application**
3. Configure:
   - **Python version**: 3.8+ (match your local version)
   - **Application root**: `/home/username/yourproject/`
   - **Application URL**: Your domain or subdomain
   - **Application startup file**: `passenger_wsgi.py`
   - **Application Entry point**: `passenger_wsgi.py`

### Step 3: Environment Variables
Add these environment variables in the Python App setup:
- `DJANGO_SETTINGS_MODULE`: `mockitech.settings`
- `PYTHONPATH`: `/home/username/yourproject/`

### Step 4: Install Dependencies
1. In cPanel, go to **Terminal** or use **SSH**
2. Navigate to your project directory
3. Activate the virtual environment (if created by cPanel)
4. Run: `pip install -r requirements.txt`

### Step 5: Database Setup
1. Run migrations: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Load data (if you have any): `python manage.py loaddata db.json`

### Step 6: Static Files
1. Ensure `staticfiles/` directory exists and is writable
2. Run: `python manage.py collectstatic --noinput`

### Step 7: Restart Application
1. Go back to **Setup Python App**
2. Click **Restart** on your application

## 🔧 Troubleshooting

### Common Issues:

1. **500 Internal Server Error**
   - Check error logs in cPanel
   - Verify `passenger_wsgi.py` exists and is correct
   - Ensure all dependencies are installed

2. **Static files not loading**
   - Verify `.htaccess` is in place
   - Check file permissions on `staticfiles/` directory
   - Ensure `STATIC_ROOT` is correctly set

3. **Database errors**
   - Check if SQLite file is writable
   - Verify database path in settings.py
   - Run migrations again

4. **Import errors**
   - Check `PYTHONPATH` environment variable
   - Verify all requirements are installed
   - Check virtual environment activation

## 🔒 Security Checklist

- [ ] Changed `SECRET_KEY` to a strong, unique value
- [ ] Set `DEBUG = False`
- [ ] Updated `ALLOWED_HOSTS` with your domain
- [ ] Enabled security headers in `.htaccess`
- [ ] Protected sensitive files (`.py`, `.sqlite3`)
- [ ] Set up SSL certificate (recommended)

## 📞 Support

If you encounter issues:
1. Check cPanel error logs
2. Verify all file paths are correct
3. Ensure Python version compatibility
4. Test locally before deploying

## 🎯 Final Checklist

- [ ] Project files uploaded to cPanel
- [ ] Python app configured correctly
- [ ] Dependencies installed
- [ ] Database migrated
- [ ] Static files collected
- [ ] Application restarted
- [ ] Domain configured
- [ ] SSL certificate installed (optional but recommended)
- [ ] Site tested and working

---

**Your MOCKITech Django website is now ready for production! 🎉** 