#!/usr/bin/env python3
"""
GitHub deployment script for MOCKITech Django project
This script helps set up GitHub deployment for cPanel
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

def check_git_status():
    """Check if we're in a git repository"""
    if not os.path.exists('.git'):
        print("❌ Error: Not a git repository. Please initialize git first.")
        return False
    return True

def main():
    print("🚀 Setting up GitHub deployment for MOCKITech...")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from your project root.")
        sys.exit(1)
    
    # Check git status
    if not check_git_status():
        print("\n📋 To initialize git repository:")
        print("1. git init")
        print("2. git add .")
        print("3. git commit -m 'Initial commit'")
        print("4. Create a repository on GitHub")
        print("5. git remote add origin https://github.com/username/repository.git")
        print("6. git push -u origin main")
        sys.exit(1)
    
    # Step 1: Add all files to git
    if not run_command("git add .", "Adding files to git"):
        sys.exit(1)
    
    # Step 2: Commit changes
    commit_message = input("Enter commit message (or press Enter for default): ").strip()
    if not commit_message:
        commit_message = "Update for production deployment"
    
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        print("⚠️  No changes to commit or commit failed")
    
    # Step 3: Push to GitHub
    print("\n📋 Next steps for GitHub deployment:")
    print("1. Push to GitHub: git push origin main")
    print("2. In cPanel, use 'Git Version Control' to clone your repository")
    print("3. Set up the Python app pointing to the cloned directory")
    print("4. Install dependencies: pip install -r requirements.txt")
    print("5. Run migrations: python manage.py migrate")
    print("6. Collect static files: python manage.py collectstatic --noinput")
    print("7. Restart the Python app")
    
    print("\n🔧 cPanel Git Setup:")
    print("1. In cPanel, go to 'Git Version Control'")
    print("2. Click 'Create'")
    print("3. Enter your GitHub repository URL")
    print("4. Set the deployment path (e.g., /home/username/mockitech)")
    print("5. Choose the branch (usually 'main' or 'master')")
    print("6. Click 'Create'")
    
    print("\n⚠️  Important reminders:")
    print("- Update ALLOWED_HOSTS in production.py with your domain")
    print("- Set SECRET_KEY environment variable in cPanel")
    print("- Ensure .gitignore excludes sensitive files")
    print("- Test locally before pushing to production")

if __name__ == "__main__":
    main() 