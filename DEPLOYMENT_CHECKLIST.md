# 🚀 MockiTech Flask cPanel Deployment Checklist

## Pre-Deployment (Before Upload)

- [ ] **Verify app.py structure**
  ```python
  def create_app():
      app = Flask(__name__)
      # ... register routes ...
      return app
  
  if __name__ == '__main__':
      app = create_app()
      app.run(debug=True, host='0.0.0.0', port=5001)
  ```

- [ ] **Ensure passenger_wsgi.py exists** in project root
  - File: `passenger_wsgi.py`
  - Contains: `from app import create_app; application = create_app()`

- [ ] **Verify requirements.txt has all dependencies**:
  ```
  Flask==3.0.0
  # ... other packages ...
  ```

- [ ] **Test locally**:
  ```bash
  python3 app.py
  # Visit http://127.0.0.1:5001
  ```

- [ ] **Check static files path**:
  - CSS: `/static/css/`
  - JS: `/static/js/`
  - Images: `/static/images/`

- [ ] **Verify template paths**:
  - All templates in: `/templates/mocki/`
  - No hardcoded paths in templates

---

## Domain Setup (mocktech.com)

### At Your Domain Registrar

- [ ] **Update nameservers** to your hosting provider
  - Example: `ns1.yourhost.com`, `ns2.yourhost.com`
  - **Allow 24-48 hours for propagation**

- [ ] **Verify DNS propagation**:
  ```bash
  nslookup mocktech.com
  # Should show your hosting provider's nameservers
  ```

### In cPanel

- [ ] **Log in to cPanel** with credentials

- [ ] **Add domain as Addon Domain**:
  - Go to: Addon Domains (or Domains)
  - Domain name: `mocktech.com`
  - Document root: `/home/username/mocktech.com/public_html` (auto-filled)
  - Click "Add Domain"

- [ ] **Create subdirectories** (if not auto-created):
  ```
  mkdir -p /home/username/mocktech.com/public_html
  ```

---

## File Upload & Setup

- [ ] **Upload project files via SSH**:
  ```bash
  ssh username@hostname
  cd /home/username
  git clone YOUR_REPO_URL mockitech
  cd mockitech
  ```

  **OR upload via File Manager**:
  - Extract to `/home/username/mockitech/`

- [ ] **Verify file permissions**:
  ```bash
  chmod 755 /home/username/mockitech/
  chmod 755 /home/username/mockitech/static
  chmod 755 /home/username/mockitech/templates
  chmod 644 /home/username/mockitech/app.py
  chmod 644 /home/username/mockitech/passenger_wsgi.py
  ```

- [ ] **Check files are in place**:
  ```bash
  ls -la /home/username/mockitech/
  # Should see: app.py, passenger_wsgi.py, static/, templates/, requirements.txt
  ```

---

## Python Application Setup in cPanel

- [ ] **In cPanel: Go to Setup Python App**
  (Under Software section or Developer area)

- [ ] **Click "Create Application"** with these settings:
  - **Python version**: 3.9+ (check available versions)
  - **Application root**: `/home/username/mockitech`
  - **Application URL**: `mocktech.com`
  - **Application startup file**: `app.py`
  - **Application Entry point**: `application`
  - **Application name**: `mockitech`

- [ ] **cPanel creates automatically**:
  - Virtual environment at: `~/.pyenv/versions/3.x.x/...`
  - `public_html` symlink
  - Passenger configuration

- [ ] **SSH into the virtual environment**:
  ```bash
  ssh username@hostname
  cd /home/username/mockitech
  ```

---

## Install Dependencies

- [ ] **Activate virtual environment** (cPanel created):
  ```bash
  source /home/username/mockitech/venv/bin/activate
  # Or check cPanel for exact path in Setup Python App
  ```

- [ ] **Install Flask and requirements**:
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  pip install Flask==3.0.0
  ```

- [ ] **Verify installation**:
  ```bash
  python -c "import flask; print(flask.__version__)"
  ```

---

## Configuration Files

- [ ] **Create/Update .htaccess**:
  - Copy from `htaccess_template` to `/home/username/mockitech/public_html/.htaccess`
  - Enables URL rewriting for Passenger

- [ ] **Update config.py** (if using):
  ```python
  os.getenv('FLASK_ENV', 'production')  # Should be 'production' on cPanel
  ```

---

## SSL Certificate (HTTPS)

- [ ] **In cPanel: Go to AutoSSL or Let's Encrypt SSL**

- [ ] **Select domain**: mocktech.com

- [ ] **Click "Issue"** or "Install"
  - Free certificate installed automatically
  - Valid for 90 days (auto-renews)

- [ ] **Verify HTTPS works**:
  ```
  https://mocktech.com
  ```

- [ ] **Update .htaccess** to force HTTPS:
  ```apache
  RewriteCond %{HTTPS} off
  RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
  ```

---

## Testing & Verification

- [ ] **Check application status** in cPanel:
  - Setup Python App → Your application → Check status/restart button

- [ ] **Test homepage**:
  ```
  https://mocktech.com
  ```

- [ ] **Test individual pages**:
  - https://mocktech.com/about
  - https://mocktech.com/services
  - https://mocktech.com/contact

- [ ] **Check static files load**:
  - CSS visible and applied
  - Images display correctly
  - JavaScript animations work

- [ ] **Test forms**:
  - Contact form submits successfully
  - No 404 errors on form submit

- [ ] **Check error pages**:
  - Visit non-existent page: https://mocktech.com/nonexistent
  - Should show custom 404 page

---

## Debugging (If Issues Occur)

### 502 Bad Gateway
```bash
# Check error logs
tail -f /home/username/logs/error_log

# Check if app restarts
touch /home/username/mockitech/tmp/restart.txt

# Or restart in cPanel
# Setup Python App → Select app → Restart
```

### Module Not Found Error
```bash
ssh username@hostname
cd /home/username/mockitech

# Activate venv
source /home/username/.pyenv/versions/3.x.x/envs/mockitech/bin/activate

# Install missing packages
pip install -r requirements.txt
```

### Images/CSS Not Loading
```bash
# Check .htaccess is in public_html
ls -la /home/username/mocktech.com/public_html/.htaccess

# Check static folder exists
ls -la /home/username/mockitech/static/

# Verify symlink
ls -la /home/username/mocktech.com/public_html/
```

### Domain Not Resolving
```bash
# Check DNS
nslookup mocktech.com

# Verify nameservers (should be your host's)
dig mocktech.com NS

# Wait if recently changed (24-48 hours)
```

---

## Post-Deployment Maintenance

### Regular Tasks
- [ ] **Monitor error logs** weekly
- [ ] **Update Flask** quarterly: `pip install --upgrade Flask`
- [ ] **Backup database** (if applicable)
- [ ] **Test all pages** monthly

### On Updates
- [ ] **Upload new files** via SSH/File Manager
- [ ] **Restart application**: 
  ```bash
  touch /home/username/mockitech/tmp/restart.txt
  ```
- [ ] **Test in browser** immediately after

### Performance Tips
- [ ] **Enable gzip compression** in .htaccess (already included)
- [ ] **Set cache headers** for static files (already included)
- [ ] **Optimize images** (already done in static/images/)
- [ ] **Minify CSS/JS** (optional, use `optimize-images.js` script)

---

## Quick Reference: Key Paths

| Item | Path |
|------|------|
| Project root | `/home/username/mockitech/` |
| App entry point | `/home/username/mockitech/app.py` |
| Passenger WSGI | `/home/username/mockitech/passenger_wsgi.py` |
| Virtual environment | Check in cPanel Setup Python App |
| Public HTML | `/home/username/mocktech.com/public_html/` |
| .htaccess | `/home/username/mocktech.com/public_html/.htaccess` |
| Static files | `/home/username/mockitech/static/` |
| Templates | `/home/username/mockitech/templates/mocki/` |
| Error logs | `/home/username/logs/error_log` |
| Application logs | cPanel → Setup Python App → View logs |

---

## Success Indicators ✅

Your deployment is successful when:
- [ ] Domain resolves to `https://mocktech.com` (with HTTPS)
- [ ] Homepage loads with hero section and images
- [ ] All navigation links work
- [ ] Services pages display with images
- [ ] Contact form loads (can submit or redirects)
- [ ] No 404 errors for static files (CSS, images, JS)
- [ ] cPanel shows "Application is Running" status
- [ ] No 502 Bad Gateway errors

---

## Support Commands

```bash
# SSH into account
ssh username@hostname

# Check Python version
python --version

# Check pip packages
pip list

# Check app status (from app directory)
ls -la /home/username/mockitech/

# View real-time error log
tail -f /home/username/logs/error_log

# Restart application
touch /home/username/mockitech/tmp/restart.txt

# Check if port 5001 is listening (should NOT be in production)
netstat -tuln | grep 5001

# Test app locally (development only)
python /home/username/mockitech/app.py
# Then visit: http://localhost:5001
```

---

## Final Checklist Before Going Live

- [ ] All pages load without errors
- [ ] HTTPS certificate installed and auto-redirects from HTTP
- [ ] Contact form works (or redirects properly)
- [ ] All images load correctly
- [ ] CSS and JavaScript applied
- [ ] Mobile responsive (test on phone)
- [ ] No console errors (open DevTools with F12)
- [ ] Business hours: Test one full flow (home → about → services → contact)
- [ ] Error pages work (404, 500)

**Congratulations! 🎉 Your MockiTech website is live at https://mocktech.com**

For questions or issues: Check cPanel error logs or restart the application.
