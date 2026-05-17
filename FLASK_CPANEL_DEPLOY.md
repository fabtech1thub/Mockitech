# MockiTech Flask - cPanel Deployment Guide

## 🚀 Deploy to cPanel with Custom Domain (mocktech.com)

### Prerequisites
- cPanel access (username & password)
- Domain mocktech.com pointing to your cPanel nameservers
- SSH access enabled on cPanel account

---

## Step 1: Point Your Domain to cPanel

1. **Update Domain Nameservers** (at your domain registrar):
   - Set nameservers to your hosting provider's nameservers
   - Wait 24-48 hours for DNS propagation

2. **Add Domain in cPanel**:
   - Log in to cPanel
   - Go to **Addon Domains** or **Domains**
   - Click "Add a Domain"
   - Enter: `mocktech.com`
   - Document Directory: `/home/username/mocktech.com/public_html`
   - Click "Add Domain"

---

## Step 2: Upload Project Files

1. **Via SSH** (Recommended):
   ```bash
   ssh username@mocktech.com
   cd ~
   git clone https://github.com/YOUR_REPO/mockitech-website.git mockitech
   cd mockitech
   ```

2. **OR Via File Manager**:
   - Log in to cPanel → File Manager
   - Navigate to `/home/username/mockitech.com/public_html`
   - Upload & extract project zip file

---

## Step 3: Setup Python Application in cPanel

1. **Go to: cPanel → Setup Python App**
   (Under "Software" or "Developer" section)

2. **Create Application** with settings:
   - **Python version**: 3.9 or higher
   - **Application root**: `/home/username/mockitech` (or your project path)
   - **Application URL**: `mocktech.com`
   - **Application startup file**: `app.py`
   - **Application Entry point**: `application`
   - **Application name**: `mockitech`

3. **Click "Create"** - cPanel will create:
   - Virtual environment
   - Passenger configuration
   - `.htaccess` file

---

## Step 4: Install Dependencies

1. **SSH into your account**:
   ```bash
   ssh username@mocktech.com
   cd /home/username/mockitech
   ```

2. **Activate the virtual environment** (created by cPanel):
   ```bash
   source /home/username/mockitech/public_html/venv/bin/activate
   ```

3. **Install Flask and requirements**:
   ```bash
   pip install Flask==3.0.0
   pip install -r requirements.txt
   ```

---

## Step 5: Create WSGI Wrapper

cPanel's Passenger needs a WSGI interface. Create `passenger_wsgi.py`:

```python
#!/usr/bin/env python
import sys
import os

# Add your project to path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

# Create Flask app instance
app = create_app()

# Ensure environment is set
os.environ['FLASK_ENV'] = 'production'

# Export for Passenger
application = app
```

Save this in your project root (`/home/username/mockitech/passenger_wsgi.py`)

---

## Step 6: Modify app.py for Production

Update your `app.py` to work with Passenger:

```python
from flask import Flask, render_template
from datetime import datetime

def create_app():
    """Create Flask application"""
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')

    def format_currency(value):
        """Format number as currency (KES)"""
        return f"KES {value:,.0f}"

    app.jinja_env.filters['format_currency'] = format_currency

    # ... rest of your routes ...
    
    # Set to production
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    
    return app

# This is important for cPanel Passenger
if __name__ == '__main__':
    app = create_app()
    # Use host 0.0.0.0 for local testing
    app.run(debug=False, host='127.0.0.1', port=5001)
else:
    # For Passenger/cPanel
    app = create_app()
```

---

## Step 7: Configure .htaccess

Create/Update `.htaccess` in your `/public_html`:

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Don't rewrite if it's a real file or directory
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    
    # Forward to Passenger
    RewriteRule ^(.*)$ / [QSA,L]
</IfModule>
```

---

## Step 8: Setup SSL Certificate (Free)

1. **In cPanel**: Go to **AutoSSL** or **Let's Encrypt SSL**
2. **Select domain**: mocktech.com
3. **Click "Issue"** - Certificate installed automatically
4. **Force HTTPS** (.htaccess):

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Force HTTPS
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    
    # Other rewrites...
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ / [QSA,L]
</IfModule>
```

---

## Step 9: Test Your Deployment

1. **Check if files are in place**:
   ```bash
   ssh username@mocktech.com
   ls -la /home/username/mockitech/
   ```

2. **Visit your domain**:
   ```
   https://mocktech.com
   ```

3. **Check error logs** if issues:
   - cPanel → **Error Log** or
   - SSH: `tail -f /home/username/logs/access_log`

---

## Step 10: Restart Application

If you make changes:

```bash
ssh username@mocktech.com
cd /home/username/mockitech
touch tmp/restart.txt  # Triggers Passenger restart
```

Or restart via cPanel:
- **Setup Python App** → Select your app → **Restart**

---

## 🔧 Troubleshooting

### 502 Bad Gateway
- Check error logs in cPanel
- Ensure virtual environment is activated
- Verify `passenger_wsgi.py` exists
- Restart application

### Module Not Found Error
```bash
ssh username@mocktech.com
cd /home/username/mockitech
source venv/bin/activate
pip install -r requirements.txt
```

### Images/CSS Not Loading
- Ensure `static/` folder exists
- Check `.htaccess` rewrite rules
- Verify paths in templates use `{{ url_for('static', ...) }}`

### Domain Not Resolving
- Check DNS propagation (24-48 hours)
- Verify nameservers at registrar
- Confirm domain added in cPanel Addon Domains

---

## 📊 Directory Structure Expected

```
/home/username/mockitech/
├── app.py
├── passenger_wsgi.py        ← Important!
├── requirements.txt
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   └── mocki/
├── venv/                     ← Created by cPanel
└── public_html/             ← Symlink to above
    └── .htaccess
```

---

## ✅ Final Checklist

- [ ] Domain pointing to cPanel nameservers
- [ ] Domain added as Addon Domain in cPanel
- [ ] Files uploaded to `/home/username/mockitech`
- [ ] Python App created in cPanel
- [ ] `passenger_wsgi.py` created in project root
- [ ] `requirements.txt` installed via pip
- [ ] `.htaccess` configured for rewrites
- [ ] SSL certificate issued
- [ ] Application restarted
- [ ] Domain accessible at https://mocktech.com

---

## 📞 Support

If issues persist:
1. Check error logs in cPanel
2. Verify all files uploaded correctly
3. Ensure Python version compatibility
4. Check that `app.py` exports `create_app()` function
