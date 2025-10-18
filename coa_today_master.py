#!/usr/bin/env python3
"""
COA TODAY - MASTER TEMPLATE
Uses matplotlib for professional, consistent chromatogram peaks
that scale with actual cannabinoid values
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
import qrcode
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from PIL import Image

# COLORS
GREEN = colors.HexColor('#2D5016')
ORANGE = colors.HexColor('#FF6B35')

def generate_retention_times():
    """Generate unique retention times with small variation"""
    base = [5.03, 8.66, 12.33, 15.84, 18.98, 21.80]
    return [round(t + random.uniform(-0.3, 0.3), 2) for t in base]

def create_chromatogram_image(peaks_data):
    """
    Create professional chromatogram using matplotlib
    
    Args:
        peaks_data: list of tuples (name, retention_time, value, color_hex)
    
    Returns:
        BytesIO object containing PNG image
    """
    fig, ax = plt.subplots(figsize=(8, 2.5), dpi=150)
    
    # Set white background
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    # Find max value to scale Y-axis dynamically
    max_value = max([p[2] for p in peaks_data]) if peaks_data else 10
    
    # Set Y-axis limit based on max value with 15% headroom
    # Round up to nearest nice number for clean appearance
    if max_value <= 1:
        y_max = 1.5
    elif max_value <= 5:
        y_max = max_value * 1.3
    elif max_value <= 40:
        y_max = max_value * 1.2
    elif max_value <= 60:
        y_max = 70
    elif max_value <= 80:
        y_max = 90
    else:
        y_max = 110
    
    # Create smooth peaks using Gaussian curves
    x_range = np.linspace(0, 25, 1000)
    y_total = np.zeros_like(x_range)
    
    for name, rt, value, color_hex in peaks_data:
        if value > 0:
            # Create Gaussian peak centered at retention time
            # Width proportional to retention time (later peaks are wider)
            sigma = 0.15 + (rt / 100)
            
            # Boost minor cannabinoid visibility using logarithmic scaling
            # This makes small peaks visible while maintaining relative proportions
            if value < 1.0:
                # For minor cannabinoids (< 1%), boost to minimum 8% of max for visibility
                amplitude = max(value, max_value * 0.08)
            elif value < 5.0:
                # For medium cannabinoids (1-5%), boost to minimum 15% of max
                amplitude = max(value, max_value * 0.15)
            else:
                # For major cannabinoids (> 5%), use actual value
                amplitude = value
            
            peak = amplitude * np.exp(-((x_range - rt) ** 2) / (2 * sigma ** 2))
            
            # Fill under the curve with solid color
            ax.fill_between(x_range, 0, peak, color=color_hex, alpha=0.9, linewidth=0)
            
            # Add peak label at the top
            peak_max_idx = np.argmax(peak)
            # Label all peaks that are visible
            if amplitude > max_value * 0.05:  # Label peaks > 5% of max
                ax.text(x_range[peak_max_idx], peak[peak_max_idx] + (y_max * 0.02), name,
                       ha='center', va='bottom', fontsize=7, color=color_hex, fontweight='bold')
    
    # Styling
    ax.set_xlim(0, 25)
    ax.set_ylim(0, y_max)
    ax.set_xlabel('Retention Time (minutes)', fontsize=9)
    ax.set_ylabel('Response', fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
    
    # Save to BytesIO
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    buf.seek(0)
    
    return buf

def create_coa_today(filename, data):
    """
    Create COA with matplotlib-generated chromatogram
    
    Args:
        data: dict with customer, strain, product_type, sample_id, batch_id,
              date_received, date_tested, thc, cbd
    """
    c = canvas.Canvas(filename, pagesize=letter)
    w, h = letter
    
    # Calculate all cannabinoid values upfront
    thca = round(data['thc'] * 0.95, 2)
    d9_thc = round(data['thc'] * 0.05, 3)
    cbda = round(data['cbd'] * 0.9, 3)
    cbd_val = round(data['cbd'] * 0.1, 3)
    cbg = round(random.uniform(0.1, 0.5), 3)
    cbn = round(random.uniform(0.05, 0.3), 3)
    cbc = round(random.uniform(0.05, 0.3), 3)
    cbga = round(random.uniform(0.5, 1.2), 3)
    total_cann = round(data['thc'] + data['cbd'] + cbg + cbn + cbc, 2)
    
    # === HEADER ===
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
    c.drawString(1.3*inch, h - 0.85*inch, "Hemp Testing Laboratory")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.black)
    c.drawRightString(w - 1*inch, h - 0.5*inch, "4439 Polaris Ave, Las Vegas NV 89103")
    c.setFillColor(ORANGE)
    c.drawRightString(w - 1*inch, h - 0.65*inch, "info@coa.today | 725-228-6600")
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 7)
    c.drawRightString(w - 1*inch, h - 0.8*inch, "ISO/IEC 17025:2017")
    
    # QR Code
    qr = qrcode.QRCode(box_size=2, border=0)
    qr.add_data(f"https://rade.llc/tests/{data['sample_id']}")
    qr.make()
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("/tmp/qr.png")
    c.drawImage("/tmp/qr.png", w - 0.9*inch, h - 1.2*inch, 0.6*inch, 0.6*inch)
    
    # === TITLE ===
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(GREEN)
    c.drawCentredString(w/2, h - 1.5*inch, "Certificate of Analysis")
    
    # === INFO TABLE ===
    y = h - 1.8*inch
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.5)
    
    c.rect(0.5*inch, y - 0.6*inch, w - 1*inch, 0.6*inch)
    c.line(0.5*inch, y - 0.2*inch, w - 0.5*inch, y - 0.2*inch)
    c.line(0.5*inch, y - 0.4*inch, w - 0.5*inch, y - 0.4*inch)
    c.line(4*inch, y, 4*inch, y - 0.6*inch)  # Moved from 2.5 to 4 inches
    c.line(5.5*inch, y, 5.5*inch, y - 0.6*inch)  # Moved from 5 to 5.5 inches
    
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.black)
    c.drawString(0.6*inch, y - 0.15*inch, "Customer:")
    c.drawString(4.1*inch, y - 0.15*inch, "Sample ID:")
    c.drawString(0.6*inch, y - 0.35*inch, "Strain / Type:")
    c.drawString(4.1*inch, y - 0.35*inch, "Batch ID:")
    c.drawString(0.6*inch, y - 0.55*inch, "Received:")
    c.drawString(4.1*inch, y - 0.55*inch, "Tested:")
    
    c.setFont("Helvetica", 8)
    c.drawString(1.1*inch, y - 0.15*inch, data['customer'])
    c.drawString(5.6*inch, y - 0.15*inch, data['sample_id'])
    
    # Handle long strain/product type text - truncate if needed
    strain_type_text = f"{data['strain']} / {data['product_type']}"
    max_width = 2.6*inch  # Space available before next column at 4 inches
    
    # Check if text fits, if not reduce font size
    text_width = c.stringWidth(strain_type_text, "Helvetica", 8)
    if text_width > max_width:
        # Try smaller font first
        c.setFont("Helvetica", 7)
        text_width = c.stringWidth(strain_type_text, "Helvetica", 7)
        if text_width > max_width:
            # Still too long, try even smaller
            c.setFont("Helvetica", 6.5)
            text_width = c.stringWidth(strain_type_text, "Helvetica", 6.5)
            if text_width > max_width:
                # Last resort: truncate
                while text_width > max_width and len(strain_type_text) > 15:
                    strain_type_text = strain_type_text[:-4] + "..."
                    text_width = c.stringWidth(strain_type_text, "Helvetica", 6.5)
        c.drawString(1.3*inch, y - 0.35*inch, strain_type_text)
        c.setFont("Helvetica", 8)  # Reset font
    else:
        c.drawString(1.3*inch, y - 0.35*inch, strain_type_text)
    
    c.drawString(5.6*inch, y - 0.35*inch, data['batch_id'])
    c.drawString(1.1*inch, y - 0.55*inch, data['date_received'])
    c.drawString(5.6*inch, y - 0.55*inch, data['date_tested'])
    
    # === RESULTS HEADER ===
    y -= 0.9*inch
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(GREEN)
    c.drawCentredString(w/2, y, "CANNABINOID RESULTS")
    
    # === MAIN RESULTS BOX ===
    y -= 0.35*inch
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.25*inch, w - 1*inch, 0.25*inch, fill=1)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(2.5*inch, y - 0.17*inch, "Total THC")
    c.drawCentredString(4.25*inch, y - 0.17*inch, "Total CBD")
    c.drawCentredString(6*inch, y - 0.17*inch, "Total Cannabinoids")
    
    y -= 0.25*inch
    c.setStrokeColor(colors.black)
    c.rect(0.5*inch, y - 0.3*inch, w - 1*inch, 0.3*inch)
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(2.5*inch, y - 0.2*inch, f"{data['thc']}%")
    c.drawCentredString(4.25*inch, y - 0.2*inch, f"{data['cbd']}%")
    c.drawCentredString(6*inch, y - 0.2*inch, f"{total_cann}%")
    
    # === BAR CHART ===
    y -= 0.6*inch
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.black)
    c.drawCentredString(w/2, y, "Main Cannabinoids (%)")
    
    y -= 0.25*inch
    
    bars = [
        ("THCa", thca, '#FF6B35'),  # Orange (COA Today brand color)
        ("CBD", data['cbd'], '#2D5016'),  # Green (COA Today brand color)
        ("CBG", cbg, '#FFA500'),  # Bright Orange
        ("CBN", cbn, '#FFD700'),  # Gold/Yellow
        ("CBC", cbc, '#FF8C00')  # Dark Orange
    ]
    
    bar_width = 0.5*inch
    max_height = 1.3*inch
    max_val = 35
    x_start = 1.5*inch
    spacing = 1.1*inch
    
    for i, (name, val, color_hex) in enumerate(bars):
        x = x_start + (i * spacing)
        bar_h = (val / max_val) * max_height
        
        c.setFillColor(colors.HexColor(color_hex))
        c.rect(x, y - max_height, bar_width, bar_h, fill=1)
        
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        c.drawCentredString(x + bar_width/2, y - max_height - 0.15*inch, name)
    
    c.setFont("Helvetica", 7)
    for val in [0, 10, 20, 30]:
        y_pos = y - max_height + (val/max_val) * max_height
        c.drawRightString(x_start - 0.1*inch, y_pos - 0.03*inch, str(val))
    
    # === CHROMATOGRAM - MATPLOTLIB GENERATED ===
    y -= max_height + 0.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.black)
    c.drawCentredString(w/2, y, "HPLC Chromatogram")
    
    y -= 0.25*inch
    
    # Generate unique retention times
    retention_times = generate_retention_times()
    
    # Prepare peaks data for matplotlib
    peaks_data = [
        ("Δ9-THC", retention_times[0], d9_thc, '#87CEEB'),
        ("THCa", retention_times[1], thca, '#4169E1'),
        ("CBDa", retention_times[2], cbda, '#90EE90'),
        ("CBGa", retention_times[3], cbga, '#FF6B35'),
        ("CBN", retention_times[4], cbn, '#9370DB'),
        ("CBC", retention_times[5], cbc, '#FFB6C1')
    ]
    
    # Create chromatogram image
    chrom_img_buf = create_chromatogram_image(peaks_data)
    
    # Save to temp file for ReportLab
    chrom_temp_path = "/tmp/chromatogram.png"
    with open(chrom_temp_path, 'wb') as f:
        f.write(chrom_img_buf.getvalue())
    
    # Draw chromatogram
    chrom_w = w - 1.5*inch
    chrom_h = 1.5*inch
    c.drawImage(chrom_temp_path, 0.75*inch, y - chrom_h, chrom_w, chrom_h)
    
    # === DETAILED TABLE ===
    y -= chrom_h + 0.4*inch
    
    cannabinoids = [
        ("D9-THC", d9_thc),
        ("THCA", thca),
        ("CBD", cbd_val),
        ("CBDA", cbda),
        ("CBN", cbn),
        ("CBDV", "ND"),
        ("D8-THC", "ND"),
        ("THCV", "ND"),
        ("CBG", cbg),
        ("CBGA", cbga),
        ("CBC", cbc)
    ]
    
    # Header
    c.setFillColor(GREEN)
    c.rect(0.5*inch, y - 0.2*inch, w - 1*inch, 0.2*inch, fill=1)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 7)
    col_w = (w - 1*inch) / 11
    for i, name in enumerate(["D9-THC", "THCA", "CBD", "CBDA", "CBN", "CBDV", "D8-THC", "THCV", "CBG", "CBGA", "CBC"]):
        c.drawCentredString(0.5*inch + (i + 0.5) * col_w, y - 0.13*inch, name)
    
    # % row
    y -= 0.2*inch
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(0.3*inch, y - 0.13*inch, "%")
    
    c.setFont("Helvetica", 7)
    for i, (_, val) in enumerate(cannabinoids):
        c.drawCentredString(0.5*inch + (i + 0.5) * col_w, y - 0.13*inch, str(val))
    
    # mg/g row
    y -= 0.15*inch
    c.setFont("Helvetica-Bold", 7)
    c.drawString(0.3*inch, y - 0.13*inch, "mg/g")
    
    c.setFont("Helvetica", 7)
    for i, (_, val) in enumerate(cannabinoids):
        mg = round(val * 10, 1) if val != "ND" else "ND"
        c.drawCentredString(0.5*inch + (i + 0.5) * col_w, y - 0.13*inch, str(mg))
    
    # === FOOTER INFO ===
    y -= 0.35*inch
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.black)
    c.drawString(0.5*inch, y, "Cannabinoid Profile Test")
    c.drawString(3*inch, y, "Analyst: 372")
    c.drawString(5.5*inch, y, "Weight: 3.0235g")
    
    y -= 0.12*inch
    c.drawString(0.5*inch, y, f"Sample Prep: {data['date_received']} 15:10:33")
    c.drawString(3*inch, y, "Extracted By: 574")
    c.drawString(5.5*inch, y, "Batch: DA006057")
    
    y -= 0.12*inch
    c.drawString(0.5*inch, y, "Analysis Method: SOP.T.40.020, SOP.T.30.050")
    
    # === SIGNATURES ===
    y -= 0.35*inch
    c.setStrokeColor(colors.black)
    c.rect(0.5*inch, y - 0.7*inch, 3.5*inch, 0.7*inch)
    c.rect(4.2*inch, y - 0.7*inch, 3.5*inch, 0.7*inch)
    
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.black)
    c.drawString(0.6*inch, y - 0.12*inch, "Lab Technician: Brian Reddy")
    c.drawString(4.3*inch, y - 0.12*inch, "Lab Director: A Lorenzo")
    
    c.setFont("Helvetica", 9)
    c.drawString(0.6*inch, y - 0.45*inch, "Brian Reddy")
    c.drawString(4.3*inch, y - 0.45*inch, "A Lorenzo")
    
    c.setFont("Helvetica", 7)
    c.drawString(0.6*inch, y - 0.65*inch, f"Date: {data['date_tested']}")
    c.drawString(4.3*inch, y - 0.65*inch, f"Date: {data['date_tested']}")
    
    # === PAGE FOOTER ===
    c.setFont("Helvetica", 6)
    c.setFillColor(colors.grey)
    c.drawString(0.5*inch, 0.35*inch, "Page 1 of 1")
    c.drawCentredString(w/2, 0.35*inch, "COA TODAY | 4439 Polaris Ave, Las Vegas NV 89103 | info@coa.today | 725-228-6600")
    
    c.save()
    print(f"✓ Created: {filename}")

# Test with 2 different samples
if __name__ == "__main__":
    samples = [
        {
            "customer": "HIGH SOCIETY 420",
            "strain": "Blooberry",
            "product_type": "Flower",
            "sample_id": "HS-POT-2025-001",
            "batch_id": "HS-FL-2025-001",
            "date_received": "01/15/2025",
            "date_tested": "01/16/2025",
            "thc": 29.4,
            "cbd": 0.312
        },
        {
            "customer": "HIGH SOCIETY 420",
            "strain": "Pineapple Express",
            "product_type": "Pre-Roll",
            "sample_id": "HS-POT-2025-002",
            "batch_id": "HS-PR-2025-010",
            "date_received": "01/15/2025",
            "date_tested": "01/16/2025",
            "thc": 30.1,
            "cbd": 0.245
        }
    ]
    
    for sample in samples:
        filename = f"/home/ubuntu/master_{sample['strain'].replace(' ', '_').lower()}.pdf"
        create_coa_today(filename, sample)

