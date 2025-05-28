# MockiTech - IT Solutions Website

A modern website for an IT company offering various software solutions including Point of Sale, Hospital Management Systems, School Management Systems, CRM, Web Design, and Software Development services.

## Features

- Modern, responsive design using Bootstrap 5
- Interactive UI with smooth animations
- Contact form with validation
- Service showcase
- About page with company information
- Team section
- FAQ section
- Google Maps integration
- Mobile-friendly layout

## Technologies Used

- Python 3.x
- Django 5.1.7
- Bootstrap 5
- Font Awesome
- HTML5/CSS3
- JavaScript

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mockitech.git
cd mockitech
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

## Running the Development Server

1. Make sure your virtual environment is activated

2. Run the development server:
```bash
python manage.py runserver
```

3. Open your browser and visit:
```
http://127.0.0.1:8000/
```

## Project Structure

```
mockitech/
├── mocki/                  # Main app directory
│   ├── templates/         # HTML templates
│   ├── static/           # Static files (CSS, JS, images)
│   └── views.py          # View functions
├── mockitech/            # Project settings
├── static/              # Project-wide static files
├── templates/           # Project-wide templates
├── media/              # User-uploaded files
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries, please contact:
- Email: info@mockitech.com
- Phone: +1 (234) 567-8900 