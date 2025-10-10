# RADE Analytics Website - Integrated COA Search Deployment

## What's New
✅ **Working COA search functionality** integrated into the main React site  
✅ **Consistent blue branding** throughout (no more multi-colored navigation)  
✅ **Simple search format** - users can search using "25-014" format  
✅ **Professional styling** matching the main site design  
✅ **All 14 COA PDFs** included and ready to search  

## Deployment Instructions

### Option 1: Upload via GitHub Web Interface (RECOMMENDED)

1. **Go to your GitHub repository:**
   - Visit: https://github.com/Sconiboy/rade-analytics-website

2. **Delete old files (if needed):**
   - Click on each old file in the repository
   - Click the trash icon to delete
   - Commit the deletion

3. **Upload new files:**
   - Click "Add file" → "Upload files"
   - Drag and drop ALL files from this folder
   - Make sure to include:
     - `index.html`
     - `favicon.ico`
     - `assets` folder (with all its contents)
     - All 14 PDF files (HP_POT_2025_*.pdf)
   - Write commit message: "Integrate working COA search with blue branding"
   - Click "Commit changes"

4. **Cloudflare Pages will automatically deploy:**
   - Wait 1-2 minutes for deployment
   - Visit: https://rade-analytics.pages.dev
   - Click "Test Results" to try the search

### Option 2: Using Git Command Line

If you have Git installed locally:

```bash
# Clone or navigate to your repository
cd /path/to/rade-analytics-website

# Copy all files from this folder to your repository
# (Replace /path/to/this/folder with actual path)

# Add, commit, and push
git add -A
git commit -m "Integrate working COA search with blue branding"
git push origin main
```

## Testing the Search

Once deployed, test the search functionality:

1. Go to https://rade-analytics.pages.dev
2. Click "Test Results" in the navigation
3. Try searching for these Sample IDs:
   - `25-001` (Wemby)
   - `25-004` (Blackberry)
   - `25-014` (Green Crack)

## Features Included

### Search Functionality
- Short format search: `25-014`
- Full format search: `HP-POT-2025-014`
- Instant results with strain name and sample ID
- Direct PDF viewing in new tab

### Design Updates
- Consistent blue navigation bar (no multi-colored buttons)
- Professional typography matching main site
- Responsive design for mobile and desktop
- Clean, modern interface

### COA Files Included
1. wemby_potency_HP_POT_2025_001.pdf
2. lemon_biscuits_potency_HP_POT_2025_002.pdf
3. flapjacks_potency_HP_POT_2025_003.pdf
4. blackberry_potency_HP_POT_2025_004.pdf
5. sherb_cream_pie_potency_HP_POT_2025_005.pdf
6. white_boy_cookies_potency_HP_POT_2025_006.pdf
7. space_candy_potency_HP_POT_2025_007.pdf
8. og_biscuits_potency_HP_POT_2025_008.pdf
9. lemon_berry_potency_HP_POT_2025_009.pdf
10. biscotti_wedding_potency_HP_POT_2025_010.pdf
11. italian_ice_potency_HP_POT_2025_011.pdf
12. 61_potency_HP_POT_2025_012.pdf
13. 41_potency_HP_POT_2025_013.pdf
14. green_crack_potency_HP_POT_2025_014.pdf

## Adding New COAs

To add new COA files in the future:

1. Name them using the format: `strainname_potency_HP_POT_YYYY_XXX.pdf`
2. Upload the PDF to your GitHub repository
3. The search will automatically find them (no code changes needed)

## Support

If you encounter any issues:
- Check that all files uploaded correctly
- Verify Cloudflare Pages deployment completed
- Clear your browser cache and try again
- Contact support if problems persist

---

**Deployment Date:** October 10, 2025  
**Version:** 2.0 - Integrated Search with Blue Branding

