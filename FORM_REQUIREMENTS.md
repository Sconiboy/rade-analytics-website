# COA Test Submission Form - Additional Fields Needed

## Current Form Fields ✅
- Test Type (Potency/Full Panel)
- Product Type (Flower/Vape/Edible/Concentrate/Pre-Roll)
- Main Cannabinoid (THCa/THCP/CBD/CBN)
- Target Percentage (Optional)
- Company Name
- Contact Name
- Phone
- Email
- Address
- Show Company Info on COA?
- Preferred Payment Method

## REQUIRED ADDITIONS for COA Generation

### Universal Fields (All Product Types)
1. **Strain/Product Name** 
   - Type: Text field
   - Required: Yes
   - Example: "Green Crack", "Blue Dream", "Sour Diesel"

2. **Batch/Lot Number**
   - Type: Text field
   - Required: Yes
   - Example: "BATCH-2025-001", "LOT-ABC123"

3. **Number of Samples**
   - Type: Number field
   - Required: Yes
   - Min: 1
   - Example: 5 (will generate 5 unique COAs)

### Product-Specific Fields

#### For EDIBLES:
4. **Servings per Package**
   - Type: Number field
   - Required: Yes (if product type = Edible)
   - Example: 10

5. **Total Package Weight (grams)**
   - Type: Number field
   - Required: Yes (if product type = Edible)
   - Example: 100

6. **mg per Serving** 
   - Type: Number field
   - Required: No (can be calculated from target %)
   - Example: 10

#### For VAPE/CARTS:
7. **Cart Size**
   - Type: Dropdown
   - Required: Yes (if product type = Vape/Cart)
   - Options: 0.5g, 1g, 2g
   - Default: 1g

#### For CONCENTRATES:
8. **Concentrate Type**
   - Type: Dropdown
   - Required: Yes (if product type = Concentrate)
   - Options: 
     - Shatter
     - Wax
     - Live Resin
     - Distillate
     - Rosin
     - Budder
     - Crumble
     - Other

### Optional but Helpful Fields

9. **Sample Received Date**
   - Type: Date picker
   - Required: No
   - Default: Today's date

10. **Testing Completion Date**
    - Type: Date picker
    - Required: No
    - Default: 3-5 days from received date

11. **Special Instructions/Notes**
    - Type: Text area
    - Required: No
    - Example: "Rush order", "Need by Friday", etc.

## Implementation Notes

- Fields 4-6 should only show when "Edible" is selected
- Field 7 should only show when "Vape/Cart" is selected
- Field 8 should only show when "Concentrate" is selected
- All other fields should show for all product types

## Sample ID Format
- Potency Tests: CT-POT-2025-001, CT-POT-2025-002, etc.
- Full Panel Tests: CT-FULL-2025-001, CT-FULL-2025-002, etc.

## Email Delivery
Form submissions should email to: **bpipkin@gmail.com**

---
*Last updated: October 17, 2025*
*For COA generation automation by Manus AI*

