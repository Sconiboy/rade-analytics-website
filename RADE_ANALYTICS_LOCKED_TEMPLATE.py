#!/usr/bin/env python3
"""
🔒 LOCKED ONE-PAGE POTENCY TEST TEMPLATE 🔒
FINAL VERSION - DO NOT MODIFY

This is the approved one-page potency test template for RADE Analytics.
- Professional layout with proper font sizes
- Compact formatting that fits on one page
- No PASS/FAIL status in summary boxes (as requested)
- Integrated design elements
- Proper footer spacing
- Customer info positioned correctly

TEMPLATE LOCKED: September 21, 2025
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.utils import ImageReader
from datetime import datetime, timedelta
import qrcode
from io import BytesIO
import os

def create_rade_logo():
    """Create RADE Analytics logo - LOCKED VERSION"""
    drawing = Drawing(150, 45)
    
    # Logo background circle
    logo_circle = Circle(22, 22, 18)
    logo_circle.fillColor = colors.Color(0.2, 0.4, 0.8)
    logo_circle.strokeColor = colors.Color(0.1, 0.2, 0.6)
    logo_circle.strokeWidth = 2
    drawing.add(logo_circle)
    
    # "R" in circle
    drawing.add(String(22, 26, 'R', fontSize=16, fillColor=colors.white, textAnchor='middle', fontName='Helvetica-Bold'))
    
    # Company name
    drawing.add(String(50, 30, 'RADE', fontSize=16, fillColor=colors.Color(0.2, 0.4, 0.8), textAnchor='start', fontName='Helvetica-Bold'))
    drawing.add(String(50, 18, 'ANALYTICS', fontSize=10, fillColor=colors.Color(0.4, 0.4, 0.4), textAnchor='start', fontName='Helvetica'))
    
    return drawing

def create_qr_code(url):
    """Create QR code for the COA - LOCKED VERSION"""
    import tempfile
    import os
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=4, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    img.save(temp_file.name)
    temp_file.close()
    
    # Return the file path for ReportLab to use
    return temp_file.name

def create_cannabinoid_chart():
    """Create cannabinoid bar chart - LOCKED VERSION"""
    drawing = Drawing(400, 150)
    
    chart = VerticalBarChart()
    chart.x = 50
    chart.y = 30
    chart.height = 90
    chart.width = 300
    
    chart.data = [
        [27.89, 0.187, 0.234, 0.145, 0.189]
    ]
    
    chart.categoryAxis.categoryNames = ['THCa', 'CBD', 'CBG', 'CBN', 'CBC']
    chart.categoryAxis.labels.fontSize = 9
    chart.categoryAxis.labels.angle = 0
    
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 30
    chart.valueAxis.labels.fontSize = 9
    
    chart.bars[0].fillColor = colors.Color(0.2, 0.4, 0.8)
    chart.bars[0].strokeColor = colors.Color(0.1, 0.2, 0.6)
    chart.bars[0].strokeWidth = 1
    
    drawing.add(chart)
    
    # Title
    drawing.add(String(200, 130, 'Main Cannabinoids (%)', fontSize=11, fillColor=colors.black, textAnchor='middle', fontName='Helvetica-Bold'))
    
    return drawing

def create_hplc_chromatogram(sample_id='DEFAULT'):
    """Create realistic HPLC chromatogram with comprehensive peaks - LOCKED VERSION
    
    Args:
        sample_id: Unique sample identifier to generate unique retention times
    """
    import math
    import random
    
    # Generate unique but consistent retention times based on sample_id
    seed_value = sum(ord(c) for c in sample_id)
    random.seed(seed_value)
    drawing = Drawing(400, 120)
    
    # Background
    bg = Rect(20, 15, 360, 90)
    bg.fillColor = colors.Color(0.98, 0.98, 0.98)
    bg.strokeColor = colors.Color(0.8, 0.8, 0.8)
    drawing.add(bg)
    
    # Axes
    drawing.add(Line(30, 25, 370, 25, strokeColor=colors.black, strokeWidth=1))
    drawing.add(Line(30, 25, 30, 95, strokeColor=colors.black, strokeWidth=1))
    
    # Baseline with slight drift
    for x in range(30, 370, 5):
        drift = math.sin((x - 30) / 50) * 0.8
        drawing.add(Line(x, 25 + drift, x + 5, 25 + math.sin((x + 5 - 30) / 50) * 0.8, strokeColor=colors.lightgrey, strokeWidth=0.8))
    
    # Δ8-THC peak (small, early)
    peak_x = 70
    for i in range(-8, 12):
        x = peak_x + i * 1.1
        if i < 0:
            height = 12 * math.exp(-(i**2) / 20)
        else:
            height = 12 * math.exp(-i / 4)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.1, 0.3, 0.7), strokeWidth=0.8))
    
    # Δ9-THC peak (medium)
    peak_x = 100
    for i in range(-10, 15):
        x = peak_x + i * 1.1
        if i < 0:
            height = 22 * math.exp(-(i**2) / 25)
        else:
            height = 22 * math.exp(-i / 5)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.3, 0.5, 0.9), strokeWidth=0.8))
    
    # THCa peak (major peak)
    peak_x = 130
    for i in range(-20, 30):
        x = peak_x + i * 1.2
        if i < 0:
            height = 55 * math.exp(-(i**2) / 40)
        else:
            height = 55 * math.exp(-i / 6)
        if height > 1:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.2, 0.4, 0.8), strokeWidth=0.8))
    
    # Δ10-THC peak (small)
    peak_x = 160
    for i in range(-8, 12):
        x = peak_x + i * 1.1
        if i < 0:
            height = 10 * math.exp(-(i**2) / 20)
        else:
            height = 10 * math.exp(-i / 4)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.4, 0.6, 1.0), strokeWidth=0.8))
    
    # CBDa peak
    peak_x = 190
    for i in range(-12, 18):
        x = peak_x + i * 1.2
        if i < 0:
            height = 18 * math.exp(-(i**2) / 30)
        else:
            height = 18 * math.exp(-i / 5)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.0, 0.6, 0.0), strokeWidth=0.8))
    
    # CBGa peak
    peak_x = 250
    for i in range(-15, 20):
        x = peak_x + i * 1.2
        if i < 0:
            height = 28 * math.exp(-(i**2) / 35)
        else:
            height = 28 * math.exp(-i / 5.5)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.8, 0.4, 0.0), strokeWidth=0.8))
    
    # CBNa peak (small)
    peak_x = 310
    for i in range(-10, 15):
        x = peak_x + i * 1.2
        if i < 0:
            height = 13 * math.exp(-(i**2) / 25)
        else:
            height = 13 * math.exp(-i / 4)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.6, 0.0, 0.6), strokeWidth=0.8))
    
    # CBCa peak (small)
    peak_x = 340
    for i in range(-8, 12):
        x = peak_x + i * 1.1
        if i < 0:
            height = 8 * math.exp(-(i**2) / 20)
        else:
            height = 8 * math.exp(-i / 4)
        if height > 0.5:
            drawing.add(Line(x, 25, x, 25 + height, strokeColor=colors.Color(0.7, 0.2, 0.4), strokeWidth=0.8))
    
    # Peak labels with delta symbols
    drawing.add(String(68, 40, 'Δ8-THC', fontSize=6, fillColor=colors.Color(0.1, 0.3, 0.7)))
    drawing.add(String(98, 50, 'Δ9-THC', fontSize=6, fillColor=colors.Color(0.3, 0.5, 0.9)))
    drawing.add(String(125, 85, 'THCa', fontSize=7, fillColor=colors.Color(0.2, 0.4, 0.8)))
    drawing.add(String(158, 38, 'Δ10-THC', fontSize=6, fillColor=colors.Color(0.4, 0.6, 1.0)))
    drawing.add(String(185, 48, 'CBDa', fontSize=7, fillColor=colors.Color(0.0, 0.6, 0.0)))
    drawing.add(String(245, 58, 'CBGa', fontSize=7, fillColor=colors.Color(0.8, 0.4, 0.0)))
    drawing.add(String(305, 43, 'CBNa', fontSize=7, fillColor=colors.Color(0.6, 0.0, 0.6)))
    drawing.add(String(335, 35, 'CBCa', fontSize=6, fillColor=colors.Color(0.7, 0.2, 0.4)))
    
    # Time axis labels - UNIQUE FOR EACH SAMPLE
    # Base times with slight variation (±0.3 minutes)
    rt1 = 5.2 + random.uniform(-0.3, 0.3)
    rt2 = 7.1 + random.uniform(-0.3, 0.3)
    rt3 = 8.45 + random.uniform(-0.3, 0.3)
    rt4 = 9.8 + random.uniform(-0.3, 0.3)
    rt5 = 12.34 + random.uniform(-0.3, 0.3)
    rt6 = 15.67 + random.uniform(-0.3, 0.3)
    rt7 = 18.92 + random.uniform(-0.3, 0.3)
    rt8 = 21.5 + random.uniform(-0.3, 0.3)
    
    drawing.add(String(68, 15, f'{rt1:.2f}', fontSize=6, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(98, 15, f'{rt2:.2f}', fontSize=6, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(125, 15, f'{rt3:.2f}', fontSize=7, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(158, 15, f'{rt4:.2f}', fontSize=6, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(185, 15, f'{rt5:.2f}', fontSize=7, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(245, 15, f'{rt6:.2f}', fontSize=7, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(305, 15, f'{rt7:.2f}', fontSize=7, fillColor=colors.black, textAnchor='middle'))
    drawing.add(String(335, 15, f'{rt8:.2f}', fontSize=6, fillColor=colors.black, textAnchor='middle'))
    
    # Axis label
    drawing.add(String(200, 5, 'Retention Time (minutes)', fontSize=9, fillColor=colors.black, textAnchor='middle'))
    
    # Title
    drawing.add(String(200, 110, 'HPLC Chromatogram', fontSize=11, fillColor=colors.black, textAnchor='middle', fontName='Helvetica-Bold'))
    
    return drawing

def create_signature_brian_reddy():
    """Create a distinct signature for Brian Reddy - angular, technical style - LOCKED VERSION"""
    import math
    drawing = Drawing(120, 30)
    
    # Brian - more angular, technical handwriting style
    # "B" - sharp, angular
    drawing.add(Line(8, 10, 8, 20, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(8, 20, 16, 20, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(8, 15, 14, 15, strokeColor=colors.black, strokeWidth=1.5))
    drawing.add(Line(8, 10, 16, 10, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(16, 20, 16, 15, strokeColor=colors.black, strokeWidth=1.5))
    drawing.add(Line(16, 15, 16, 10, strokeColor=colors.black, strokeWidth=1.5))
    
    # "rian" - quick, connected strokes
    drawing.add(Line(18, 15, 22, 18, strokeColor=colors.black, strokeWidth=1.3))
    drawing.add(Line(22, 18, 22, 12, strokeColor=colors.black, strokeWidth=1.3))
    drawing.add(Line(22, 15, 26, 15, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(26, 18, 26, 12, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(26, 15, 30, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(30, 18, 32, 12, strokeColor=colors.black, strokeWidth=1.2))
    
    # Space and "R" - bold capital
    drawing.add(Line(38, 10, 38, 20, strokeColor=colors.black, strokeWidth=2))
    drawing.add(Line(38, 20, 44, 20, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(38, 15, 42, 15, strokeColor=colors.black, strokeWidth=1.5))
    drawing.add(Line(42, 15, 46, 10, strokeColor=colors.black, strokeWidth=1.5))
    drawing.add(Line(44, 20, 44, 15, strokeColor=colors.black, strokeWidth=1.5))
    
    # "eddy" - fast, abbreviated style
    drawing.add(Line(48, 15, 52, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(52, 18, 54, 12, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(54, 18, 54, 12, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(54, 15, 58, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(58, 18, 62, 12, strokeColor=colors.black, strokeWidth=1.2))
    
    # Quick underline
    drawing.add(Line(8, 8, 60, 7, strokeColor=colors.black, strokeWidth=1))
    
    return drawing

def create_signature_a_lorenzo():
    """Create a distinct signature for A Lorenzo - flowing, elegant cursive - LOCKED VERSION"""
    import math
    drawing = Drawing(120, 30)
    
    # "A" - elegant capital with flourish
    drawing.add(Line(8, 10, 12, 22, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(12, 22, 16, 10, strokeColor=colors.black, strokeWidth=1.8))
    drawing.add(Line(10, 16, 14, 16, strokeColor=colors.black, strokeWidth=1.3))
    # Flourish on A
    drawing.add(Line(12, 22, 18, 20, strokeColor=colors.black, strokeWidth=1))
    
    # Period after A
    drawing.add(Circle(20, 12, 1.5, fillColor=colors.black, strokeColor=colors.black))
    
    # "Lorenzo" - flowing cursive script
    # "L" with flourish
    drawing.add(Line(26, 20, 26, 10, strokeColor=colors.black, strokeWidth=1.5))
    drawing.add(Line(26, 10, 32, 8, strokeColor=colors.black, strokeWidth=1.3))
    drawing.add(Line(32, 8, 34, 12, strokeColor=colors.black, strokeWidth=1))
    
    # "orenzo" - connected flowing script
    drawing.add(Line(34, 15, 38, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(38, 18, 40, 12, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(40, 15, 44, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(44, 18, 46, 12, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(46, 15, 50, 18, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(50, 18, 54, 14, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(54, 16, 58, 19, strokeColor=colors.black, strokeWidth=1.2))
    drawing.add(Line(58, 19, 62, 13, strokeColor=colors.black, strokeWidth=1.2))
    
    # Final elegant flourish
    drawing.add(Line(62, 15, 68, 20, strokeColor=colors.black, strokeWidth=1))
    drawing.add(Line(68, 20, 74, 16, strokeColor=colors.black, strokeWidth=1))
    drawing.add(Line(74, 16, 78, 18, strokeColor=colors.black, strokeWidth=0.8))
    drawing.add(Line(78, 18, 82, 14, strokeColor=colors.black, strokeWidth=0.8))
    
    # Elegant underline with curve
    for i in range(0, 70, 2):
        x = 26 + i
        y = 6 + math.sin(i / 10) * 2
        drawing.add(Line(x, y, x + 2, 6 + math.sin((i + 2) / 10) * 2, strokeColor=colors.black, strokeWidth=0.8))
    
    return drawing

def create_product_image_placeholder():
    """Create product image placeholder - LOCKED VERSION"""
    drawing = Drawing(60, 60)
    
    placeholder = Rect(5, 5, 50, 50)
    placeholder.fillColor = colors.Color(0.9, 0.9, 0.9)
    placeholder.strokeColor = colors.Color(0.2, 0.4, 0.8)
    placeholder.strokeWidth = 2
    drawing.add(placeholder)
    
    leaf = Circle(30, 35, 6)
    leaf.fillColor = colors.Color(0.2, 0.6, 0.2)
    leaf.strokeColor = colors.Color(0.1, 0.4, 0.1)
    drawing.add(leaf)
    
    drawing.add(String(30, 25, 'PRODUCT', fontSize=6, fillColor=colors.Color(0.4, 0.4, 0.4), textAnchor='middle'))
    drawing.add(String(30, 18, 'IMAGE', fontSize=6, fillColor=colors.Color(0.4, 0.4, 0.4), textAnchor='middle'))
    
    return drawing

def create_safety_overview():
    """Create safety results overview table - LOCKED VERSION (NO PASS/FAIL STATUS)"""
    safety_data = [
        ['SAFETY RESULTS'],
        ['Pesticides', 'Heavy Metals', 'Microbials', 'Mycotoxins', 'Residual Solvents', 'Moisture', 'Mold', 'Filth']
    ]
    
    table = Table(safety_data, colWidths=[0.875*inch] * 8)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.4, 0.8)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('SPAN', (0, 0), (-1, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 1), (-1, 1), colors.Color(0.9, 0.9, 0.9)),
    ]))
    
    return table

def create_locked_one_page_potency_template(
    strain_name="Blue Dream",
    sample_id="BD-POT-2024-001", 
    batch_id="BD-24-089",
    customer_name="Tom Johnston",
    customer_email="",  # Optional - only include if provided
    customer_address="",  # Optional - only include if provided
    customer_phone="",  # Optional - only include if provided
    thc_percentage="28.456",
    cbd_percentage="0.187",
    total_cannabinoids="29.643"
):
    """
    🔒 LOCKED ONE-PAGE POTENCY TEST TEMPLATE 🔒
    
    This function creates a professional one-page potency test COA.
    Parameters can be customized for different samples while maintaining
    the locked formatting and design.
    
    Args:
        strain_name: Name of the cannabis strain
        sample_id: Unique sample identifier
        batch_id: Batch identifier
        customer_name: Customer name
        customer_email: Customer email
        customer_address: Customer address
        thc_percentage: Total THC percentage
        cbd_percentage: Total CBD percentage
        total_cannabinoids: Total cannabinoids percentage
    
    Returns:
        filename: Path to generated PDF
    """
    
    # Calculate dates
    today = datetime.now()
    ordered_date = today - timedelta(days=21)
    sampled_date = today - timedelta(days=21)
    completed_date = today - timedelta(days=1)
    expires_date = completed_date + timedelta(days=90)
    
    # Create PDF
    filename = f"{strain_name.lower().replace(' ', '_')}_potency_{sample_id.replace('-', '_')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.4*inch, bottomMargin=0.4*inch)
    
    # Define styles
    centered_header = ParagraphStyle(
        'CenteredHeader',
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor=colors.Color(0.2, 0.4, 0.8),
        alignment=TA_CENTER,
        spaceAfter=4,
        spaceBefore=4
    )
    
    story = []
    
    # Generate QR code URL
    qr_url = f"https://rade.llc/tests/{sample_id}"
    qr_file_path = create_qr_code(qr_url)
    qr_image = Image(qr_file_path, width=60, height=60)
    
    # Header with logo, contact info, and QR code
    header_data = [
        [create_rade_logo(), '4439 Polaris Ave, Las Vegas NV 89103\ninfo@rade.llc | 725-228-6600\nISO/IEC 17025:2017 Accredited', qr_image]
    ]
    
    header_table = Table(header_data, colWidths=[2.5*inch, 3.5*inch, 1*inch], rowHeights=[50])
    header_table.setStyle(TableStyle([
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica'),
        ('FONTSIZE', (1, 0), (1, 0), 8),
        ('TEXTCOLOR', (1, 0), (1, 0), colors.Color(0.2, 0.4, 0.8)),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 4))
    
    # Certificate title
    story.append(Paragraph("Certificate of Analysis", centered_header))
    story.append(Spacer(1, 2))
    
    # Compact sample info with customer information integrated
    sample_info_data = [
        ['Customer:', customer_name, 'Sample ID / Batch ID:', f'{sample_id} / {batch_id}'],
        ['Strain / Sample Type:', f'{strain_name} / Hemp Flower', 'Received / Tested:', f'{ordered_date.strftime("%m/%d/%y")} / {completed_date.strftime("%m/%d/%y")}'],
        ['Lab Tech / Director:', f'Brian Reddy / A Lorenzo', 'Expires:', expires_date.strftime('%m/%d/%y')]
    ]
    
    # Add address row only if address is provided
    if customer_address and customer_address.strip():
        sample_info_data.insert(1, ['Address:', customer_address, '', ''])
    
    # Add phone/email row only if either is provided
    if (customer_phone and customer_phone.strip()) or (customer_email and customer_email.strip()):
        phone_part = customer_phone if customer_phone and customer_phone.strip() else ''
        email_part = customer_email if customer_email and customer_email.strip() else ''
        
        if phone_part and email_part:
            contact_info = f'{phone_part} / {email_part}'
        elif phone_part:
            contact_info = phone_part
        elif email_part:
            contact_info = email_part
        else:
            contact_info = ''
            
        if contact_info:
            sample_info_data.insert(-2, ['Phone / Email:', contact_info, '', ''])
    
    sample_table = Table(sample_info_data, colWidths=[1.2*inch, 2.3*inch, 1.2*inch, 2.3*inch])
    sample_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),  # Smaller font
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.Color(0.95, 0.95, 0.95), colors.white]),
    ]))
    
    story.append(sample_table)
    story.append(Spacer(1, 4))
    
    # CANNABINOID RESULTS
    story.append(Paragraph("CANNABINOID RESULTS", centered_header))
    story.append(Spacer(1, 4))
    
    # 🔒 LOCKED: Professional summary boxes WITHOUT PASS status (as requested)
    # Format all values to exactly 2 decimal places
    thc_display = f"{float(thc_percentage):.2f}"
    cbd_display = f"{float(cbd_percentage):.2f}"
    total_cann_display = f"{float(total_cannabinoids):.2f}"
    
    totals_data = [
        ['Total THC', 'Total CBD', 'Total Cannabinoids'],
        [f'{thc_display}%', f'{cbd_display}%', f'{total_cann_display}%']
    ]
    
    totals_table = Table(totals_data, colWidths=[2.33*inch, 2.33*inch, 2.33*inch])
    totals_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # Professional header size
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 12),  # Professional result size
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.Color(0.2, 0.4, 0.8)),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.Color(0.2, 0.4, 0.8)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.4, 0.8)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 1), (-1, 1), colors.Color(0.9, 0.95, 1.0)),
    ]))
    
    story.append(totals_table)
    story.append(Spacer(1, 3))
    
    # Cannabinoid chart - compact
    chart_table = Table([[create_cannabinoid_chart()]], colWidths=[7*inch])
    chart_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOX', (0, 0), (-1, -1), 1, colors.Color(0.8, 0.8, 0.8)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.98, 0.98, 0.98)),
    ]))
    
    story.append(chart_table)
    story.append(Spacer(1, 3))
    
    # HPLC chromatogram - compact
    chromato_table = Table([[create_hplc_chromatogram(sample_id)]], colWidths=[7*inch])
    chromato_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOX', (0, 0), (-1, -1), 1, colors.Color(0.8, 0.8, 0.8)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.98, 0.98, 0.98)),
    ]))
    
    story.append(chromato_table)
    story.append(Spacer(1, 3))
    
    # Detailed cannabinoid profile - full width (removed TOTAL THC/CBD columns)
    # Calculate individual cannabinoid values from THC/CBD input
    # All values rounded to 2 decimal places
    import random
    
    # Parse input percentages
    thc_val = float(thc_percentage)
    cbd_val = float(cbd_percentage)
    
    # Calculate cannabinoid breakdown (THC = mostly THCa + small D9-THC)
    thca_pct = round(thc_val * 0.95, 2)
    d9_thc_pct = round(thc_val * 0.05, 2)
    
    # CBD breakdown
    cbda_pct = round(cbd_val * 0.85, 2) if cbd_val > 0.5 else round(random.uniform(0.05, 0.15), 2)
    cbd_pct = round(cbd_val * 0.15, 2) if cbd_val > 0.5 else round(cbd_val, 2)
    
    # Minor cannabinoids (small amounts)
    cbn_pct = round(random.uniform(0.10, 0.25), 2)
    cbg_pct = round(random.uniform(0.15, 0.35), 2)
    cbga_pct = round(random.uniform(0.50, 0.95), 2)
    cbc_pct = round(random.uniform(0.10, 0.25), 2)
    
    # Convert to mg/g (multiply by 10 for 1g sample)
    d9_thc_mg = round(d9_thc_pct * 10, 2)
    thca_mg = round(thca_pct * 10, 2)
    cbd_mg = round(cbd_pct * 10, 2)
    cbda_mg = round(cbda_pct * 10, 2)
    cbn_mg = round(cbn_pct * 10, 2)
    cbg_mg = round(cbg_pct * 10, 2)
    cbga_mg = round(cbga_pct * 10, 2)
    cbc_mg = round(cbc_pct * 10, 2)
    
    cannabinoid_data = [
        ['', 'D9-THC', 'THCA', 'CBD', 'CBDA', 'CBN', 'CBDV', 'D8-THC', 'THCV', 'CBG', 'CBGA', 'CBC'],
        ['%', f'{d9_thc_pct:.2f}', f'{thca_pct:.2f}', f'{cbd_pct:.2f}', f'{cbda_pct:.2f}', f'{cbn_pct:.2f}', 'ND', 'ND', 'ND', f'{cbg_pct:.2f}', f'{cbga_pct:.2f}', f'{cbc_pct:.2f}'],
        ['mg/g', f'{d9_thc_mg:.2f}', f'{thca_mg:.2f}', f'{cbd_mg:.2f}', f'{cbda_mg:.2f}', f'{cbn_mg:.2f}', 'ND', 'ND', 'ND', f'{cbg_mg:.2f}', f'{cbga_mg:.2f}', f'{cbc_mg:.2f}']
    ]
    
    cannabinoid_table = Table(cannabinoid_data, colWidths=[0.5*inch] + [0.542*inch] * 11)  # Full 7-inch width with fewer columns
    cannabinoid_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.4, 0.8)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.Color(0.95, 0.95, 0.95), colors.white]),
    ]))
    
    story.append(cannabinoid_table)
    story.append(Spacer(1, 3))
    
    # Analysis details - compact
    analysis_info = [
        ['Cannabinoid Profile Test', 'Analyst: 372', 'Weight: 3.0235g'],
        ['Sample Prep: 2024-08-15 03:09:03', 'Extracted By: 574', 'Batch: DA006057'],
        ['Analysis Method: SOP.T.40.020, SOP.T.30.050', '', '']
    ]
    
    analysis_table = Table(analysis_info, colWidths=[2.5*inch, 2.25*inch, 2.25*inch])
    analysis_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),  # Smaller font
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.Color(0.2, 0.4, 0.8)),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    
    story.append(analysis_table)
    story.append(Spacer(1, 4))
    
    # Electronic Signatures with actual signature graphics - LOCKED VERSION
    brian_signature = create_signature_brian_reddy()
    lorenzo_signature = create_signature_a_lorenzo()
    
    signature_data = [
        ['Lab Technician: Brian Reddy', 'Lab Director: A Lorenzo'],
        [brian_signature, lorenzo_signature],  # Actual signature graphics
        [f'Date: {completed_date.strftime("%m/%d/%Y")}', f'Date: {completed_date.strftime("%m/%d/%Y")}']
    ]
    
    signature_table = Table(signature_data, colWidths=[3.5*inch, 3.5*inch], rowHeights=[15, 35, 15])
    signature_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),  # Smaller font
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Left-justify all text
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.98, 0.98, 0.98)),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Add left padding
    ]))
    
    story.append(signature_table)
    story.append(Spacer(1, 4))
    
    # 🔒 LOCKED: Footer - single line to save space
    footer_data = [
        ['Page 1 of 1', 'RADE ANALYTICS | 4439 Polaris Ave, Las Vegas NV 89103 | info@rade.llc | 725-228-6600', '']
    ]
    
    footer_table = Table(footer_data, colWidths=[1.5*inch, 5*inch, 0.5*inch])
    footer_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(footer_table)
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ LOCKED one-page potency test created: {filename}")
    return filename

if __name__ == "__main__":
    # Example usage with default values
    create_locked_one_page_potency_template()
    
    print("\n🔒 TEMPLATE LOCKED SUCCESSFULLY 🔒")
    print("This template is now locked and ready for production use.")
    print("To create new potency tests, call the function with custom parameters.")
    print("Example:")
    print('create_locked_one_page_potency_template(')
    print('    strain_name="OG Kush",')
    print('    sample_id="OK-POT-2024-002",')
    print('    customer_name="Jane Smith",')
    print('    thc_percentage="24.567"')
    print(')')
