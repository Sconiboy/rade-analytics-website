from flask import Flask, send_from_directory, send_file, jsonify
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# CORS headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Store COA data
COA_DATA = {
    'HP-POT-2024-001': {'strain': 'Wemby', 'customer': 'HEMPATHY', 'thc': '28.57%', 'cbd': '1.87%', 'file': 'wemby_potency_HP_POT_2024_001.pdf'},
    'HP-POT-2024-002': {'strain': 'Lemon Biscuits', 'customer': 'HEMPATHY', 'thc': '31.23%', 'cbd': '2.45%', 'file': 'lemon_biscuits_potency_HP_POT_2024_002.pdf'},
    'HP-POT-2024-003': {'strain': 'Flapjacks', 'customer': 'HEMPATHY', 'thc': '29.88%', 'cbd': '3.12%', 'file': 'flapjacks_potency_HP_POT_2024_003.pdf'},
    'HP-POT-2024-004': {'strain': 'Blockberry', 'customer': 'HEMPATHY', 'thc': '26.54%', 'cbd': '4.78%', 'file': 'blockberry_potency_HP_POT_2024_004.pdf'},
    'HP-POT-2024-005': {'strain': 'Sherb Cream Pie', 'customer': 'HEMPATHY', 'thc': '30.12%', 'cbd': '2.34%', 'file': 'sherb_cream_pie_potency_HP_POT_2024_005.pdf'},
    'HP-POT-2024-006': {'strain': 'White Boy Cookies', 'customer': 'HEMPATHY', 'thc': '32.79%', 'cbd': '1.56%', 'file': 'white_boy_cookies_potency_HP_POT_2024_006.pdf'},
    'HP-POT-2024-007': {'strain': 'Space Candy', 'customer': 'HEMPATHY', 'thc': '27.65%', 'cbd': '3.67%', 'file': 'space_candy_potency_HP_POT_2024_007.pdf'},
    'HP-POT-2024-008': {'strain': 'Dog Biscuits', 'customer': 'HEMPATHY', 'thc': '29.35%', 'cbd': '2.89%', 'file': 'dog_biscuits_potency_HP_POT_2024_008.pdf'},
    'HP-POT-2024-009': {'strain': 'Lemon Berry', 'customer': 'HEMPATHY', 'thc': '33.21%', 'cbd': '1.23%', 'file': 'lemon_berry_potency_HP_POT_2024_009.pdf'},
    'HP-POT-2024-010': {'strain': 'Biscotti Wedding', 'customer': 'HEMPATHY', 'thc': '28.90%', 'cbd': '4.23%', 'file': 'biscotti_wedding_potency_HP_POT_2024_010.pdf'},
    'HP-POT-2024-011': {'strain': 'Italian Ice', 'customer': 'HEMPATHY', 'thc': '31.57%', 'cbd': '3.45%', 'file': 'italian_ice_potency_HP_POT_2024_011.pdf'},
    'HP-POT-2024-012': {'strain': '61', 'customer': 'HEMPATHY', 'thc': '30.45%', 'cbd': '2.67%', 'file': '61_potency_HP_POT_2024_012.pdf'},
    'HP-POT-2024-013': {'strain': '41', 'customer': 'HEMPATHY', 'thc': '29.78%', 'cbd': '3.89%', 'file': '41_potency_HP_POT_2024_013.pdf'},
    'TEST-FULL-001': {'strain': 'Test Strain', 'customer': 'HEMPATHY', 'thc': '29.35%', 'cbd': '2.89%', 'file': 'test_strain_full_panel_TEST-FULL-001.pdf'},
    
    # Single Source LLC COAs
    'G41-POT-2024-005': {'strain': 'Gelato 41', 'customer': 'Single Source LLC', 'thc': '32.40%', 'cbd': '0.31%', 'file': 'gelato_41_potency_G41_POT_2024_005.pdf'},
    'G41-POT-2024-006': {'strain': 'Gelato 41', 'customer': 'Single Source LLC', 'thc': '32.40%', 'cbd': '0.31%', 'file': 'gelato_41_potency_G41_POT_2024_006.pdf'},
    'G41-POT-2024-007': {'strain': 'Gelato 41', 'customer': 'Single Source LLC', 'thc': '32.40%', 'cbd': '0.31%', 'file': 'gelato_41_potency_G41_POT_2024_007.pdf'},
    'G41-POT-2024-008': {'strain': 'Gelato 41', 'customer': 'Single Source LLC', 'thc': '32.40%', 'cbd': '0.31%', 'file': 'gelato_41_potency_G41_POT_2024_008.pdf'},
    
    # Secret Garden Dispensary COAs
    'IL-POT-2024-004': {'strain': 'Illuminati', 'customer': 'Secret Garden Dispensary', 'thc': '31.23%', 'cbd': '0.46%', 'file': 'illuminati_potency_IL_POT_2024_004.pdf'},
    
    # Blue Dream COAs
    'BD-POT-2024-001': {'strain': 'Blue Dream', 'customer': 'Test Client', 'thc': '28.46%', 'cbd': '0.19%', 'file': 'blue_dream_potency_BD_POT_2024_001.pdf'},
    
    # Purple Haze Full Panel
    'PH-FULL-2024-001': {'strain': 'Purple Haze', 'customer': 'RADE Analytics Demo', 'thc': '27.89%', 'cbd': '2.34%', 'file': 'purple_haze_full_panel_PH-FULL-2024-001.pdf'},
}

@app.route('/')
def index():
    """Serve the main website"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    """Serve static files"""
    try:
        return send_from_directory('.', path)
    except:
        # If file not found, serve index.html for SPA routing
        return send_from_directory('.', 'index.html')

@app.route('/tests/<sample_id>')
def get_coa(sample_id):
    """Serve the COA PDF for a given sample ID"""
    if sample_id not in COA_DATA:
        return jsonify({"error": "Sample ID not found"}), 404
    
    coa_info = COA_DATA[sample_id]
    pdf_path = os.path.join(os.path.dirname(__file__), coa_info['file'])
    
    if not os.path.exists(pdf_path):
        return jsonify({"error": "COA file not found"}), 404
    
    return send_file(pdf_path, as_attachment=False, mimetype='application/pdf')

@app.route('/api/tests/<sample_id>')
def get_coa_info(sample_id):
    """Get COA information as JSON"""
    if sample_id not in COA_DATA:
        return jsonify({"error": "Sample ID not found"}), 404
    
    return jsonify(COA_DATA[sample_id])

@app.route('/api/tests')
def list_all_tests():
    """List all available tests"""
    return jsonify(COA_DATA)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
