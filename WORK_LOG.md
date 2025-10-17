# COA Today - Work Log

## 2025-10-17

### Website Rebrand
- Rebranded from RADE Analytics to COA Today
- Updated color scheme: Green (#2D5016) + Orange (#FF6B35)
- Updated all copy to focus on hemp testing and franchise model
- Domain: coa.today (currently deployed at rade.llc)

### Test Submission Form
- Added "Submit Test" page with dynamic multi-product form
- Supports up to 50 products per submission
- Fields per product:
  - Product/Strain Name
  - Test Type (Potency $25 / Full Panel $75)
  - Product Type (Flower, Vape, Edible, Concentrate, Pre-Roll, Infused Pre-Roll)
  - Main Cannabinoid (THCa, THCP, CBD, CBN, Delta-9)
  - Target Percentage (optional)
  
### TODO: Product-Specific Fields
Need to add conditional fields based on product type:

**Edible:**
- mg per piece
- number of pieces

**Vape/Cart:**
- cartridge size (0.5g, 1g, 2g, etc.)

**Concentrate:**
- concentrate type (shatter, wax, rosin, live resin, etc.)
- weight

**Pre-Roll:**
- weight per pre-roll
- number in pack

**Infused Pre-Roll:**
- weight per pre-roll
- number in pack
- infusion type (hash rosin, distillate, diamonds, etc.)

### Invoices
- Invoice #002: High Society 420 - $975 (39 potency tests @ $25)
- Payment methods: Cash, Debit/Credit, Venmo (@JesusPisces), Wire/ACH

### COA Template
- New COA Today template with green/orange branding
- Based on original RADE template (25-002)
- Unique retention times per sample to avoid duplicate chromatogram issue

### Forms
- All forms use Web3Forms: `7e57fd05-68ea-4f99-ac15-a902b886a89c`
- Contact: 🔵 CONTACT
- Franchise: 🟢 FRANCHISE
- Affiliate: 🟡 AFFILIATE
- Test Submission: 🧪 TEST SUBMISSION

---

## Notes for Other Sessions
- Hempathy batch PDFs (HP-POT-2025-001 through 014) already sent to client - DO NOT regenerate
- Mobile navigation fixed with hamburger menu
- All buttons on Specials/Affiliates pages now navigate to Contact form

