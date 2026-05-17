#!/usr/bin/env python3
"""
Production deployment script for MOCKITech Django project
Run this script to prepare your project for cPanel deployment
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 Starting production deployment preparation...")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from your project root.")
        sys.exit(1)
    
    # Step 1: Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        sys.exit(1)
    
    # Step 2: Make migrations
    if not run_command("python manage.py makemigrations", "Making migrations"):
        sys.exit(1)
    
    # Step 3: Apply migrations
    if not run_command("python manage.py migrate", "Applying migrations"):
        sys.exit(1)
    
    # Step 4: Create superuser if needed
    print("👤 Do you want to create a superuser? (y/n): ", end="")
    create_superuser = input().lower().strip()
    if create_superuser == 'y':
        run_command("python manage.py createsuperuser", "Creating superuser")
    
    print("\n🎉 Production preparation completed!")
    print("\n📋 Next steps for cPanel deployment:")
    print("1. Zip your project folder (excluding .git, .venv, __pycache__)")
    print("2. Upload to cPanel File Manager")
    print("3. Extract in your desired directory")
    print("4. In cPanel Setup Python App:")
    print("   - Set app root to your project folder")
    print("   - Set entry point to 'passenger_wsgi.py'")
    print("   - Add environment variable: DJANGO_SETTINGS_MODULE=mockitech.settings")
    print("5. Install requirements: pip install -r requirements.txt")
    print("6. Restart the Python app")
    print("\n⚠️  Don't forget to:")
    print("- Update ALLOWED_HOSTS in settings.py with your domain")
    print("- Change SECRET_KEY to a strong, unique value")
    print("- Set up SSL if needed")

if __name__ == "__main__":
    main() 