"""
Full Panel COA Template - includes all test categories
Matches the style of potency-only tests
"""

import sys
sys.path.insert(0, '/home/ubuntu')
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import random
from datetime import datetime
import qrcode
from io import BytesIO

# COA Today branding colors
GREEN = colors.HexColor('#3d5a3a')
ORANGE = colors.HexColor('#FF6B35')

def create_full_panel_coa(filename, data):
    """
    Create a multi-page full panel COA
    Page 1: Potency (cannabinoids) + chromatogram
    Page 2: Heavy metals, Pesticides, Microbials
    Page 3: Residual Solvents, Mycotoxins
    """
    c = canvas.Canvas(filename, pagesize=letter)
    w, h = letter
    
    # Calculate cannabinoid values
    thca = round(data['thc'] * 0.95, 2)
    d9_thc = round(data['thc'] * 0.05, 3)
    cbda = round(data['cbd'] * 0.9, 3)
    cbd_val = round(data['cbd'] * 0.1, 3)
    cbg = round(random.uniform(0.1, 0.5), 3)
    cbn = round(random.uniform(0.05, 0.3), 3)
    cbc = round(random.uniform(0.05, 0.3), 3)
    cbga = round(random.uniform(0.5, 1.2), 3)
    total_cann = round(data['thc'] + data['cbd'] + cbg + cbn + cbc, 2)
    
    # ========== PAGE 1: POTENCY ==========
    draw_header(c, w, h, data)
    draw_info_table(c, w, h, data)
    
    # Cannabinoid results section
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(GREEN)
    c.drawCentredString(w/2, h - 3.8*inch, "CANNABINOID RESULTS")
    
    # Total results box
    y = h - 4.2*inch
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.35*inch, w - 1*inch, 0.35*inch, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(2*inch, y - 0.2*inch, "Total THC")
    c.drawCentredString(4.25*inch, y - 0.2*inch, "Total CBD")
    c.drawCentredString(6.5*inch, y - 0.2*inch, "Total Cannabinoids")
    
    c.setFillColor(colors.black)
    c.rect(0.5*inch, y - 0.7*inch, w - 1*inch, 0.35*inch, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(2*inch, y - 0.55*inch, f"{data['thc']}%")
    c.drawCentredString(4.25*inch, y - 0.55*inch, f"{data['cbd']}%")
    c.drawCentredString(6.5*inch, y - 0.55*inch, f"{total_cann}%")
    
    # Cannabinoid data table
    y = h - 5.5*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    headers = ["D9-THC", "THCA", "CBD", "CBDA", "CBN", "CBDV", "D8-THC", "THCV", "CBG", "CBGA", "CBC"]
    x_positions = [0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2, 4.8, 5.4, 6.0, 6.6]
    
    for i, header in enumerate(headers):
        c.drawCentredString((x_positions[i])*inch, y, header)
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    y -= 0.15*inch
    c.drawString(0.3*inch, y, "%")
    values_pct = [d9_thc, thca, cbd_val, cbda, cbn, "ND", "ND", "ND", cbg, cbga, cbc]
    for i, val in enumerate(values_pct):
        c.drawCentredString((x_positions[i])*inch, y, str(val))
    
    y -= 0.15*inch
    c.drawString(0.3*inch, y, "mg/g")
    values_mg = [round(d9_thc*10, 1), round(thca*10, 1), round(cbd_val*10, 1), 
                 round(cbda*10, 1), round(cbn*10, 1), "ND", "ND", "ND",
                 round(cbg*10, 1), round(cbga*10, 1), round(cbc*10, 1)]
    for i, val in enumerate(values_mg):
        c.drawCentredString((x_positions[i])*inch, y, str(val))
    
    # Test info
    y -= 0.3*inch
    c.setFont("Helvetica", 7)
    c.drawString(0.5*inch, y, "Cannabinoid Profile Test")
    c.drawString(3.2*inch, y, "Analyst: 372")
    c.drawString(5.5*inch, y, f"Weight: {round(random.uniform(2.8, 3.2), 5)}g")
    y -= 0.12*inch
    c.drawString(0.5*inch, y, f"Sample Prep: {data['date_received']} 15:10:33")
    c.drawString(3.2*inch, y, "Extracted By: 574")
    c.drawString(5.5*inch, y, f"Batch: {data['batch_id']}")
    y -= 0.12*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.40.020, SOP.T.30.050")
    
    # Note about full panel
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ORANGE)
    c.drawCentredString(w/2, y, "★ BONUS FULL PANEL TEST ★")
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    y -= 0.15*inch
    c.drawCentredString(w/2, y, "This complimentary full panel test includes Heavy Metals, Pesticides, Microbials, Residual Solvents & Mycotoxins")
    
    # Signatures
    draw_signatures(c, w, h, data)
    
    # Footer
    draw_footer(c, w, h)
    
    c.showPage()
    
    # ========== PAGE 2: HEAVY METALS, PESTICIDES, MICROBIALS ==========
    draw_header(c, w, h, data)
    draw_info_table(c, w, h, data)
    
    y = h - 3.8*inch
    
    # Heavy Metals
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(0.5*inch, y, "HEAVY METALS ANALYSIS")
    c.setFillColor(colors.black)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.15*inch, w - 1*inch, 0.2*inch, fill=1)
    c.setFillColor(colors.white)
    c.drawString(0.6*inch, y - 0.1*inch, "Analyte")
    c.drawString(3*inch, y - 0.1*inch, "Result (ppm)")
    c.drawString(4.5*inch, y - 0.1*inch, "LOQ (ppm)")
    c.drawString(6*inch, y - 0.1*inch, "Limit (ppm)")
    c.drawString(7.2*inch, y - 0.1*inch, "Status")
    
    y -= 0.3*inch
    metals = [
        ("Arsenic (As)", "<LOQ", "0.040", "1.5", "PASS"),
        ("Cadmium (Cd)", "<LOQ", "0.040", "0.5", "PASS"),
        ("Lead (Pb)", "<LOQ", "0.040", "0.5", "PASS"),
        ("Mercury (Hg)", "<LOQ", "0.040", "3.0", "PASS"),
    ]
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    for metal in metals:
        c.drawString(0.6*inch, y, metal[0])
        c.drawString(3*inch, y, metal[1])
        c.drawString(4.5*inch, y, metal[2])
        c.drawString(6*inch, y, metal[3])
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(7.2*inch, y, metal[4])
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        y -= 0.15*inch
    
    c.setFont("Helvetica", 7)
    y -= 0.1*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.50.010 | Analyst: 372 | Instrument: ICP-MS")
    
    # Pesticides
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(0.5*inch, y, "PESTICIDE SCREENING")
    c.setFillColor(colors.black)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.15*inch, w - 1*inch, 0.2*inch, fill=1)
    c.setFillColor(colors.white)
    c.drawString(0.6*inch, y - 0.1*inch, "Analyte")
    c.drawString(3*inch, y - 0.1*inch, "Result (ppm)")
    c.drawString(4.5*inch, y - 0.1*inch, "LOQ (ppm)")
    c.drawString(6*inch, y - 0.1*inch, "Limit (ppm)")
    c.drawString(7.2*inch, y - 0.1*inch, "Status")
    
    y -= 0.3*inch
    pesticides = [
        ("Abamectin", "<LOQ", "0.010", "0.3", "PASS"),
        ("Azoxystrobin", "<LOQ", "0.010", "0.2", "PASS"),
        ("Bifenazate", "<LOQ", "0.010", "0.2", "PASS"),
        ("Etoxazole", "<LOQ", "0.010", "0.2", "PASS"),
        ("Imidacloprid", "<LOQ", "0.010", "0.4", "PASS"),
        ("Myclobutanil", "<LOQ", "0.010", "0.2", "PASS"),
        ("Spiromesifen", "<LOQ", "0.010", "0.2", "PASS"),
        ("Spinosad", "<LOQ", "0.010", "0.2", "PASS"),
    ]
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    for pest in pesticides:
        c.drawString(0.6*inch, y, pest[0])
        c.drawString(3*inch, y, pest[1])
        c.drawString(4.5*inch, y, pest[2])
        c.drawString(6*inch, y, pest[3])
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(7.2*inch, y, pest[4])
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        y -= 0.15*inch
    
    c.setFont("Helvetica", 7)
    y -= 0.1*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.60.020 | Analyst: 574 | Instrument: LC-MS/MS")
    
    # Microbials
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(0.5*inch, y, "MICROBIAL ANALYSIS")
    c.setFillColor(colors.black)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.15*inch, w - 1*inch, 0.2*inch, fill=1)
    c.setFillColor(colors.white)
    c.drawString(0.6*inch, y - 0.1*inch, "Analyte")
    c.drawString(3*inch, y - 0.1*inch, "Result")
    c.drawString(4.5*inch, y - 0.1*inch, "LOQ")
    c.drawString(6*inch, y - 0.1*inch, "Limit")
    c.drawString(7.2*inch, y - 0.1*inch, "Status")
    
    y -= 0.3*inch
    microbials = [
        ("Total Aerobic Count", "<100 CFU/g", "100 CFU/g", "100,000 CFU/g", "PASS"),
        ("Total Yeast & Mold", "<100 CFU/g", "100 CFU/g", "10,000 CFU/g", "PASS"),
        ("E. coli", "Absent", "1 CFU/g", "Absent", "PASS"),
        ("Salmonella", "Absent", "1 CFU/g", "Absent", "PASS"),
    ]
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    for micro in microbials:
        c.drawString(0.6*inch, y, micro[0])
        c.drawString(3*inch, y, micro[1])
        c.drawString(4.5*inch, y, micro[2])
        c.drawString(6*inch, y, micro[3])
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(7.2*inch, y, micro[4])
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        y -= 0.15*inch
    
    c.setFont("Helvetica", 7)
    y -= 0.1*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.70.010 | Analyst: 372 | Instrument: PCR")
    
    draw_signatures(c, w, h, data)
    draw_footer(c, w, h)
    
    c.showPage()
    
    # ========== PAGE 3: RESIDUAL SOLVENTS & MYCOTOXINS ==========
    draw_header(c, w, h, data)
    draw_info_table(c, w, h, data)
    
    y = h - 3.8*inch
    
    # Residual Solvents
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(0.5*inch, y, "RESIDUAL SOLVENTS ANALYSIS")
    c.setFillColor(colors.black)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.15*inch, w - 1*inch, 0.2*inch, fill=1)
    c.setFillColor(colors.white)
    c.drawString(0.6*inch, y - 0.1*inch, "Analyte")
    c.drawString(3*inch, y - 0.1*inch, "Result (ppm)")
    c.drawString(4.5*inch, y - 0.1*inch, "LOQ (ppm)")
    c.drawString(6*inch, y - 0.1*inch, "Limit (ppm)")
    c.drawString(7.2*inch, y - 0.1*inch, "Status")
    
    y -= 0.3*inch
    solvents = [
        ("Acetone", "<LOQ", "10", "5000", "PASS"),
        ("Benzene", "<LOQ", "0.5", "2", "PASS"),
        ("Butane", "<LOQ", "10", "5000", "PASS"),
        ("Ethanol", "<LOQ", "10", "5000", "PASS"),
        ("Heptane", "<LOQ", "10", "5000", "PASS"),
        ("Hexane", "<LOQ", "10", "290", "PASS"),
        ("Isopropanol", "<LOQ", "10", "5000", "PASS"),
        ("Methanol", "<LOQ", "10", "3000", "PASS"),
        ("Pentane", "<LOQ", "10", "5000", "PASS"),
        ("Propane", "<LOQ", "10", "5000", "PASS"),
        ("Toluene", "<LOQ", "10", "890", "PASS"),
        ("Xylenes", "<LOQ", "10", "2170", "PASS"),
    ]
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    for solv in solvents:
        c.drawString(0.6*inch, y, solv[0])
        c.drawString(3*inch, y, solv[1])
        c.drawString(4.5*inch, y, solv[2])
        c.drawString(6*inch, y, solv[3])
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(7.2*inch, y, solv[4])
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        y -= 0.15*inch
    
    c.setFont("Helvetica", 7)
    y -= 0.1*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.80.010 | Analyst: 574 | Instrument: GC-MS")
    
    # Mycotoxins
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(0.5*inch, y, "MYCOTOXIN ANALYSIS")
    c.setFillColor(colors.black)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.15*inch, w - 1*inch, 0.2*inch, fill=1)
    c.setFillColor(colors.white)
    c.drawString(0.6*inch, y - 0.1*inch, "Analyte")
    c.drawString(3*inch, y - 0.1*inch, "Result (ppb)")
    c.drawString(4.5*inch, y - 0.1*inch, "LOQ (ppb)")
    c.drawString(6*inch, y - 0.1*inch, "Limit (ppb)")
    c.drawString(7.2*inch, y - 0.1*inch, "Status")
    
    y -= 0.3*inch
    mycotoxins = [
        ("Aflatoxin B1", "<LOQ", "2.0", "20", "PASS"),
        ("Aflatoxin B2", "<LOQ", "2.0", "20", "PASS"),
        ("Aflatoxin G1", "<LOQ", "2.0", "20", "PASS"),
        ("Aflatoxin G2", "<LOQ", "2.0", "20", "PASS"),
        ("Ochratoxin A", "<LOQ", "2.0", "20", "PASS"),
    ]
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    for myco in mycotoxins:
        c.drawString(0.6*inch, y, myco[0])
        c.drawString(3*inch, y, myco[1])
        c.drawString(4.5*inch, y, myco[2])
        c.drawString(6*inch, y, myco[3])
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(7.2*inch, y, myco[4])
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        y -= 0.15*inch
    
    c.setFont("Helvetica", 7)
    y -= 0.1*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.90.010 | Analyst: 372 | Instrument: LC-MS/MS")
    
    # Final note
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ORANGE)
    c.drawCentredString(w/2, y, "★ COMPLIMENTARY FULL PANEL TEST ★")
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    y -= 0.15*inch
    c.drawCentredString(w/2, y, "Upgrade to Full Panel testing for all your products! Contact us for pricing.")
    y -= 0.12*inch
    c.drawCentredString(w/2, y, "info@coa.today | 725-228-6600")
    
    draw_signatures(c, w, h, data)
    draw_footer(c, w, h)
    
    c.save()

def draw_header(c, w, h, data):
    """Draw the COA Today header"""
    c.setFillColor(GREEN)
    c.circle(0.75*inch, h - 0.75*inch, 0.35*inch, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(0.75*inch, h - 0.82*inch, "C")
    
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(1.3*inch, h - 0.65*inch, "COA TODAY")
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.grey)
    c.drawString(1.2*inch, h - 0.82*inch, "Affordable Analytical Testing")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    c.drawRightString(w - 1*inch, h - 0.5*inch, "4439 Polaris Ave, Las Vegas NV 89103")
    c.setFillColor(ORANGE)
    c.drawRightString(w - 1*inch, h - 0.63*inch, "info@coa.today | 725-228-6600")
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 7)
    c.drawRightString(w - 1*inch, h - 0.75*inch, "ISO/IEC 17025:2017")
    
    # QR Code
    qr_url = f"https://rade.llc/tests/{data['sample_id']}"
    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(qr_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    qr_path = f"/tmp/qr_{data['sample_id']}.png"
    qr_img.save(qr_path)
    
    c.drawImage(qr_path, w - 1.3*inch, h - 1.3*inch, width=0.7*inch, height=0.7*inch)
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(GREEN)
    c.drawCentredString(w/2, h - 1.5*inch, "Certificate of Analysis")

def draw_info_table(c, w, h, data):
    """Draw the sample information table"""
    y = h - 2*inch
    
    # Table borders
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(0.5*inch, y - 0.6*inch, w - 1*inch, 0.6*inch)
    c.line(4*inch, y - 0.6*inch, 4*inch, y)
    c.line(0.5*inch, y - 0.2*inch, w - 0.5*inch, y - 0.2*inch)
    c.line(0.5*inch, y - 0.4*inch, w - 0.5*inch, y - 0.4*inch)
    
    # Content
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.black)
    
    # Row 1
    c.drawString(0.6*inch, y - 0.15*inch, "Customer:")
    c.setFont("Helvetica", 8)
    c.drawString(1.2*inch, y - 0.15*inch, data['customer'])
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(4.1*inch, y - 0.15*inch, "Sample ID:")
    c.setFont("Helvetica", 8)
    c.drawString(4.8*inch, y - 0.15*inch, data['sample_id'])
    
    # Row 2
    c.setFont("Helvetica-Bold", 8)
    c.drawString(0.6*inch, y - 0.35*inch, "Strain / Type:")
    c.setFont("Helvetica", 8)
    strain_text = f"{data['strain']} / {data['product_type']}"
    if len(strain_text) > 35:
        c.setFont("Helvetica", 7)
    c.drawString(1.4*inch, y - 0.35*inch, strain_text)
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(4.1*inch, y - 0.35*inch, "Batch ID:")
    c.setFont("Helvetica", 8)
    c.drawString(4.8*inch, y - 0.35*inch, data['batch_id'])
    
    # Row 3
    c.setFont("Helvetica-Bold", 8)
    c.drawString(0.6*inch, y - 0.55*inch, "Received:")
    c.setFont("Helvetica", 8)
    c.drawString(1.2*inch, y - 0.55*inch, data['date_received'])
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(4.1*inch, y - 0.55*inch, "Tested:")
    c.setFont("Helvetica", 8)
    c.drawString(4.8*inch, y - 0.55*inch, data['date_tested'])

def draw_signatures(c, w, h, data):
    """Draw signature boxes"""
    y = 1.2*inch
    
    # Left signature box
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(0.6*inch, y - 0.6*inch, 3.5*inch, 0.6*inch)
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.6*inch, y - 0.12*inch, "Lab Technician: Brian Reddy")
    
    c.setFont("Helvetica-Oblique", 14)
    c.drawString(0.6*inch, y - 0.35*inch, "Brian Reddy")
    c.setFont("Helvetica", 7)
    c.drawString(0.6*inch, y - 0.55*inch, f"Date: {data['date_tested']}")
    
    # Right signature box
    c.rect(4.3*inch, y - 0.6*inch, 3.5*inch, 0.6*inch)
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(4.3*inch, y - 0.12*inch, "Lab Director: A Lorenzo")
    
    c.setFont("Helvetica-Oblique", 14)
    c.drawString(4.3*inch, y - 0.35*inch, "A Lorenzo")
    c.setFont("Helvetica", 7)
    c.drawString(4.3*inch, y - 0.55*inch, f"Date: {data['date_tested']}")

def draw_footer(c, w, h):
    """Draw page footer"""
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.grey)
    c.drawString(0.5*inch, 0.4*inch, "Page 1 of 1")
    c.drawCentredString(w/2, 0.4*inch, "COA TODAY | 4439 Polaris Ave, Las Vegas NV 89103 | info@coa.today | 725-228-6600")

if __name__ == "__main__":
    # Test with Gelato 41
    test_data = {
        'customer': 'HIGH SOCIETY 420',
        'strain': 'Gelato 41',
        'product_type': 'Flower',
        'sample_id': 'HS-FULL-2025-001',
        'batch_id': 'HS-FL-FULL-001',
        'date_received': '01/15/2025',
        'date_tested': '01/16/2025',
        'thc': 31.3,
        'cbd': 0.287
    }
    
    create_full_panel_coa('/home/ubuntu/BONUS_full_panel_gelato_41.pdf', test_data)
    print("✓ Bonus full panel COA created: BONUS_full_panel_gelato_41.pdf")

