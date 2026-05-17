from flask import Flask, render_template
from datetime import datetime

def format_currency(value):
    """Format number as currency (KES)"""
    return f"KES {value:,.0f}"

def create_app():
    """Create Flask application"""
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    
    # Register custom Jinja2 filter
    app.jinja_env.filters['format_currency'] = format_currency

    @app.context_processor
    def inject_globals():
        return {'year': datetime.now().year}

    # Home page
    @app.route('/')
    def home():
        return render_template('mocki/index.html')

    # About page
    @app.route('/about')
    def about():
        return render_template('mocki/about.html')

    # Services page
    @app.route('/services')
    def services():
        return render_template('mocki/services.html')

    # Contact page
    @app.route('/contact')
    def contact():
        return render_template('mocki/contact.html')

    # Blog page
    @app.route('/blog')
    def blog():
        return render_template('mocki/blog.html')

    # Service detail routes
    @app.route('/pos-systems')
    def pos_systems():
        return render_template('mocki/possystems.html')

    @app.route('/hospital-management')
    def hospital_management():
        return render_template('mocki/hospital_management.html')

    @app.route('/school-management')
    def school_management():
        return render_template('mocki/school_management.html')

    @app.route('/erp-solutions')
    def erp_solutions():
        return render_template('mocki/erp_solutions.html')

    @app.route('/web-design')
    def web_design():
        return render_template('mocki/web_design.html')

    @app.route('/hardware-sourcing')
    def hardware_sourcing():
        return render_template('mocki/hardware_sourcing.html')

    @app.route('/hardware-installation')
    def hardware_installation():
        return render_template('mocki/hardware_installation.html')

    @app.route('/technical-support')
    def technical_support():
        return render_template('mocki/technical_support.html')

    @app.route('/it-support')
    def it_support():
        return render_template('mocki/it_support.html')

    @app.route('/maintenance-services')
    def maintenance_services():
        return render_template('mocki/maintenance_services.html')

    @app.route('/cctv-security')
    def cctv_security():
        return render_template('mocki/cctv_security.html')

    @app.route('/cybersecurity')
    def cybersecurity():
        return render_template('mocki/cybersecurity.html')

    @app.route('/data-management')
    def data_management():
        return render_template('mocki/data-management.html')

    # Error handlers
    @app.errorhandler(404)
    def not_found(_):
        return render_template('mocki/404.html'), 404

    @app.errorhandler(500)
    def server_error(_):
        return render_template('mocki/500.html'), 500

    return app


if __name__ == '__main__':
    app = create_app()
    # Development mode - use debug=True for local testing
    # Production mode (cPanel) uses passenger_wsgi.py instead
    app.run(debug=True, host='0.0.0.0', port=5001)