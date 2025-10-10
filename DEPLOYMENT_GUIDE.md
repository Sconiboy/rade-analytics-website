# RADE Analytics - Final Deployment Guide

## 🎯 What's Included

This package contains your complete, updated RADE Analytics website with:

✅ **57 COA PDF files** - All Hempathy, Hemp Hut 508, and test series
✅ **ISO certification claims removed** - Legally compliant
✅ **Working search functionality** - Finds COAs by sample ID
✅ **Clean, professional design** - Consistent blue branding
✅ **Both domains configured** - rade.llc and rade-analytics.pages.dev

## 📦 Files in This Package

- `index.html` - Main website file
- `assets/` - JavaScript and CSS files
- `*.pdf` - All 57 COA certificates
- `favicon.ico` - Site icon
- `_redirects` - Cloudflare redirect rules (for old QR codes)

## 🚀 Deployment Steps

### Option 1: GitHub Web Interface (Recommended)

1. **Go to your GitHub repository:**
   https://github.com/Sconiboy/rade-analytics-website

2. **Delete old files** (if any):
   - Click on each old file
   - Click the trash icon
   - Commit the deletion

3. **Upload ALL files from this package:**
   - Click "Add file" → "Upload files"
   - Drag and drop ALL files from this folder
   - Include the `assets` folder
   - Include all PDF files
   - Write commit message: "Complete update - 57 COAs, no ISO claims, comprehensive search"
   - Click "Commit changes"

4. **Wait 1-2 minutes** for Cloudflare Pages to deploy

5. **Visit your site:**
   - https://rade.llc
   - https://rade-analytics.pages.dev

### Option 2: Git Command Line

```bash
cd /path/to/rade-analytics-website
git add .
git commit -m "Complete update - 57 COAs, no ISO claims, comprehensive search"
git push origin main
```

## 🔍 Testing the Search

After deployment, test these searches:

**Hempathy Tests (Paying Customer):**
- Search: `24-001` → Should find: Wemby
- Search: `24-200` → Should find: Wemby (batch ID)
- Search: `HP-24-200` → Should find: Wemby
- Search: `HP-POT-2024-001` → Should find: Wemby
- Search: `24-004` → Should find: Blackberry
- Search: `24-203` → Should find: Blackberry (batch ID)

**Hemp Hut 508 (Paying Customer):**
- Search: `SF-4993` → Should find: SherbFuel
- Search: `SF-SAMPLE-4993` → Should find: SherbFuel

**2025 Format:**
- Search: `25-001` → Should find: Wemby (2025 version)
- Search: `25-004` → Should find: Blackberry (2025 version)

## 📋 Sample ID Reference

### Hempathy (HP) - 14 Tests
Each test has TWO searchable IDs:

| Sample ID | Batch ID | Strain | Filename |
|-----------|----------|--------|----------|
| HP-POT-2024-001 | HP-24-200 | Wemby | wemby_potency_HP_POT_2024_001.pdf |
| HP-POT-2024-002 | HP-24-201 | Lemon Biscuits | lemon_biscuits_potency_HP_POT_2024_002.pdf |
| HP-POT-2024-003 | HP-24-202 | Flapjacks | flapjacks_potency_HP_POT_2024_003.pdf |
| HP-POT-2024-004 | HP-24-203 | Blackberry | blackberry_potency_HP_POT_2024_004.pdf |
| HP-POT-2024-005 | HP-24-204 | Sherb Cream Pie | sherb_cream_pie_potency_HP_POT_2024_005.pdf |
| HP-POT-2024-006 | HP-24-205 | White Boy Cookies | white_boy_cookies_potency_HP_POT_2024_006.pdf |
| HP-POT-2024-007 | HP-24-206 | Space Candy | space_candy_potency_HP_POT_2024_007.pdf |
| HP-POT-2024-008 | HP-24-207 | OG Biscuits | og_biscuits_potency_HP_POT_2024_008.pdf |
| HP-POT-2024-009 | HP-24-208 | Lemon Berry | lemon_berry_potency_HP_POT_2024_009.pdf |
| HP-POT-2024-010 | HP-24-209 | Biscotti Wedding | biscotti_wedding_potency_HP_POT_2024_010.pdf |
| HP-POT-2024-011 | HP-24-210 | Italian Ice | italian_ice_potency_HP_POT_2024_011.pdf |
| HP-POT-2024-012 | HP-24-211 | 61 | 61_potency_HP_POT_2024_012.pdf |
| HP-POT-2024-013 | HP-24-212 | 41 | 41_potency_HP_POT_2024_013.pdf |

### Hemp Hut 508
| Sample ID | Batch ID | Strain | Filename |
|-----------|----------|--------|----------|
| SF-SAMPLE-4993 | SF-BATCH-4919 | SherbFuel | sherbfuel-4993-coa.pdf |

## 🔄 Old QR Code Redirects

The `_redirects` file handles old QR codes:
- Any URL with `/tests/` → Redirects to Test Results page
- Any URL with `/coa/` → Redirects to Test Results page
- Any 404 error → Redirects to Test Results page

This ensures old QR codes always lead customers to the search page.

## ✅ What Was Fixed

1. **Removed ISO/IEC 17025:2017 claims** - No longer claiming accreditation
2. **Added all 57 COA PDFs** - Every test is now searchable
3. **Comprehensive search** - Handles all ID formats (sample IDs, batch IDs, short formats)
4. **Clean design** - Professional blue branding throughout
5. **Redirect rules** - Old QR codes work

## 📝 Next Steps (Future Updates)

1. **Franchise Page Content** - Add detailed franchise information
2. **News Articles** - Add articles about:
   - Kratom testing
   - MGM-15 (new cannabinoid)
   - Research chemicals
   - Industry trends
3. **SofloFarm Tests** - Add when available

## 🆘 Troubleshooting

**Search not finding tests?**
- Make sure all PDF files uploaded correctly
- Check that filenames match exactly
- Try searching with different formats (24-001, 24-200, HP-24-200)

**Old QR codes not working?**
- Make sure `_redirects` file is uploaded
- Cloudflare Pages should automatically use it

**Site not updating?**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 2-3 minutes for Cloudflare to deploy
- Try incognito/private browsing mode

## 📞 Support

If you need help, you can:
1. Check the Cloudflare Pages deployment logs
2. Verify files are in the GitHub repository
3. Test the search with known sample IDs

---

**Deployment Date:** October 10, 2025
**Version:** 2.0 - Comprehensive COA Search
**Status:** Ready for Production ✅

