# RADE Analytics Website - Deployment Instructions

## Overview
This is the complete RADE Analytics cannabis testing laboratory website with COA lookup functionality, ready for permanent deployment.

## Features
- ✅ COA Lookup System - Search and view COAs by sample ID
- ✅ Professional Laboratory Design
- ✅ Complete COA Database (30+ test results)
- ✅ Company Information Pages
- ✅ News/Blog Section
- ✅ Franchising Opportunities
- ✅ Mobile Responsive Design
- ✅ QR Code Integration

## Files Structure
```
rade-analytics-final/
├── app.py                 # Main Flask application
├── index.html            # Frontend React application
├── assets/               # CSS and JavaScript files
├── requirements.txt      # Python dependencies
├── *.pdf                # All COA PDF files
└── favicon.ico          # Website icon
```

## Deployment Options

### Option 1: Cloudways.com (Recommended)
1. Create a new PHP/Python application on Cloudways
2. Upload all files to the public_html directory
3. Install Python dependencies: `pip install flask`
4. Run the Flask app: `python3 app.py`
5. Configure your domain to point to the application

### Option 2: Any Web Hosting Service
1. Upload all files to your web server
2. Ensure Python 3.x is available
3. Install Flask: `pip install flask`
4. Run: `python3 app.py`
5. Configure your web server to serve the application

### Option 3: Local Testing
```bash
cd rade-analytics-final
pip install flask
python3 app.py
```
Then visit: http://localhost:5000

## COA Lookup Testing
Test the COA lookup with these sample IDs:
- HP-POT-2024-001 (Wemby strain)
- G41-POT-2024-005 (Gelato 41)
- BD-POT-2024-001 (Blue Dream)
- PH-FULL-2024-001 (Purple Haze - Full Panel)

## Technical Details
- **Backend**: Flask (Python)
- **Frontend**: React with modern UI
- **Database**: In-memory COA data store
- **File Serving**: Direct PDF serving for COAs
- **CORS**: Enabled for cross-origin requests

## Support
The website is fully self-contained and includes all necessary files for deployment. All COA PDFs are included and the lookup system is fully functional.

## URL Structure
- `/` - Main website
- `/tests/{SAMPLE_ID}` - Direct COA PDF access
- `/api/tests/{SAMPLE_ID}` - COA information as JSON
- `/api/tests` - List all available tests

This website will provide 24/7 uptime when deployed to a reliable hosting platform.
