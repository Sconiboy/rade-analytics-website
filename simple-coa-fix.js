// Simple COA Search Fix - Direct approach
console.log('Loading Simple COA Search Fix...');

// Wait for page to fully load
window.addEventListener('load', function() {
    console.log('Page loaded, initializing COA search...');
    
    // Complete COA database
    const COA_DATABASE = {
        'HP-POT-2024-001': { file: 'wemby_potency_HP_POT_2024_001.pdf', strain: 'Wemby', thc: '28.57%', cbd: '1.87%' },
        'HP-POT-2024-002': { file: 'lemon_biscuits_potency_HP_POT_2024_002.pdf', strain: 'Lemon Biscuits', thc: '24.12%', cbd: '0.89%' },
        'HP-POT-2024-003': { file: 'flapjacks_potency_HP_POT_2024_003.pdf', strain: 'Flapjacks', thc: '26.34%', cbd: '1.23%' },
        'HP-POT-2024-004': { file: 'blackberry_potency_HP_POT_2024_004.pdf', strain: 'Blackberry', thc: '26.54%', cbd: '4.78%' },
        'HP-POT-2024-005': { file: 'sherb_cream_pie_potency_HP_POT_2024_005.pdf', strain: 'Sherb Cream Pie', thc: '25.67%', cbd: '1.45%' },
        'HP-POT-2024-006': { file: 'white_boy_cookies_potency_HP_POT_2024_006.pdf', strain: 'White Boy Cookies', thc: '27.89%', cbd: '0.67%' },
        'HP-POT-2024-007': { file: 'space_candy_potency_HP_POT_2024_007.pdf', strain: 'Space Candy', thc: '23.45%', cbd: '2.34%' },
        'HP-POT-2024-008': { file: 'og_biscuits_potency_HP_POT_2024_008.pdf', strain: 'OG Biscuits', thc: '28.12%', cbd: '1.12%' },
        'HP-POT-2024-009': { file: 'lemon_berry_potency_HP_POT_2024_009.pdf', strain: 'Lemon Berry', thc: '26.78%', cbd: '1.89%' },
        'HP-POT-2024-010': { file: 'biscotti_wedding_potency_HP_POT_2024_010.pdf', strain: 'Biscotti Wedding', thc: '29.34%', cbd: '0.78%' },
        'HP-POT-2024-011': { file: 'italian_ice_potency_HP_POT_2024_011.pdf', strain: 'Italian Ice', thc: '27.56%', cbd: '1.34%' },
        'HP-POT-2024-012': { file: '61_potency_HP_POT_2024_012.pdf', strain: '61', thc: '25.89%', cbd: '2.12%' },
        'HP-POT-2024-013': { file: '41_potency_HP_POT_2024_013.pdf', strain: '41', thc: '26.45%', cbd: '1.67%' },
        'HP-POT-2024-014': { file: 'green_crack_potency_HP_POT_2024_014.pdf', strain: 'Green Crack', thc: '27.93%', cbd: '0.48%' },
        'G41-POT-2024-005': { file: 'gelato_41_potency_G41_POT_2024_005.pdf', strain: 'Gelato 41', thc: '24.67%', cbd: '1.23%' },
        'BD-POT-2024-001': { file: 'blue_dream_professional_layout_BD_POT_2024_001.pdf', strain: 'Blue Dream', thc: '22.34%', cbd: '3.45%' },
        'GC-FULL-2024-001': { file: 'green_crack_full_panel_with_signatures_GC_FULL_2024_001.pdf', strain: 'Green Crack Full Panel', thc: '28.73%', cbd: '0.49%' },
        'TEST-FULL-001': { file: 'test_strain_full_panel_TEST-FULL-001.pdf', strain: 'Test Strain Full Panel', thc: '25.00%', cbd: '2.00%' }
    };
    
    // Make database globally available
    window.COA_DATABASE = COA_DATABASE;
    
    // Search function
    function searchCOA(searchTerm) {
        const term = searchTerm.toUpperCase().trim();
        
        // Exact match first
        if (COA_DATABASE[searchTerm]) {
            return { id: searchTerm, data: COA_DATABASE[searchTerm] };
        }
        
        // Partial matches
        for (const [id, data] of Object.entries(COA_DATABASE)) {
            if (id.toUpperCase().includes(term) || 
                data.strain.toUpperCase().includes(term)) {
                return { id: id, data: data };
            }
        }
        
        return null;
    }
    
    // Override search functionality
    function setupSearch() {
        const searchButton = document.querySelector('button:contains("Search")') || 
                           document.querySelector('button[class*="search"]') ||
                           document.querySelectorAll('button').forEach(btn => {
                               if (btn.textContent.includes('Search')) return btn;
                           });
        
        // Try multiple times to find elements
        setTimeout(() => {
            const buttons = document.querySelectorAll('button');
            const inputs = document.querySelectorAll('input');
            
            console.log('Found', buttons.length, 'buttons and', inputs.length, 'inputs');
            
            // Find search button and input
            let searchBtn = null;
            let searchInput = null;
            
            buttons.forEach(btn => {
                if (btn.textContent.includes('Search')) {
                    searchBtn = btn;
                }
            });
            
            inputs.forEach(input => {
                if (input.placeholder && input.placeholder.includes('Sample')) {
                    searchInput = input;
                }
            });
            
            if (searchBtn && searchInput) {
                console.log('Found search elements, setting up enhanced search...');
                
                // Clone button to remove existing listeners
                const newBtn = searchBtn.cloneNode(true);
                searchBtn.parentNode.replaceChild(newBtn, searchBtn);
                
                newBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const searchTerm = searchInput.value.trim();
                    console.log('Searching for:', searchTerm);
                    
                    if (!searchTerm) return;
                    
                    const result = searchCOA(searchTerm);
                    if (result) {
                        showResult(result.id, result.data);
                    } else {
                        showAvailableTests(searchTerm);
                    }
                });
                
                console.log('Enhanced search setup complete!');
            } else {
                console.log('Could not find search elements');
            }
        }, 2000);
    }
    
    function showResult(sampleId, data) {
        // Remove existing results
        const existing = document.getElementById('enhanced-result');
        if (existing) existing.remove();
        
        // Create result div
        const resultDiv = document.createElement('div');
        resultDiv.id = 'enhanced-result';
        resultDiv.innerHTML = `
            <div style="background: #d1fae5; border: 1px solid #10b981; border-radius: 8px; padding: 16px; margin: 16px 0;">
                <h3 style="color: #065f46; margin: 0 0 12px 0;">✅ Test Result Found</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
                    <div><strong>Sample ID:</strong> ${sampleId}</div>
                    <div><strong>Test Type:</strong> Potency</div>
                    <div><strong>Strain:</strong> ${data.strain}</div>
                    <div><strong>THC:</strong> ${data.thc}</div>
                    <div><strong>Customer:</strong> HEMPATHY</div>
                    <div><strong>CBD:</strong> ${data.cbd}</div>
                </div>
                <button onclick="window.open('${data.file}', '_blank')" 
                        style="background: #1f2937; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px;">
                    📄 View Complete Certificate of Analysis
                </button>
            </div>
        `;
        
        // Insert after search form
        const searchForm = document.querySelector('input[placeholder*="Sample"]').closest('div').parentNode;
        searchForm.appendChild(resultDiv);
    }
    
    function showAvailableTests(searchTerm) {
        // Remove existing results
        const existing = document.getElementById('enhanced-result');
        if (existing) existing.remove();
        
        const availableTests = Object.entries(COA_DATABASE).slice(0, 12);
        
        const resultDiv = document.createElement('div');
        resultDiv.id = 'enhanced-result';
        resultDiv.innerHTML = `
            <div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 16px; margin: 16px 0;">
                <h3 style="color: #991b1b; margin: 0 0 12px 0;">❌ No Results Found</h3>
                <p>No test found for "${searchTerm}"</p>
                <p><strong>Available Sample IDs:</strong></p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px; margin: 12px 0;">
                    ${availableTests.map(([id, data]) => `
                        <div style="background: white; padding: 8px; border-radius: 4px; border: 1px solid #e5e7eb;">
                            <div style="font-family: monospace; font-weight: bold; color: #1f2937;">${id}</div>
                            <div style="font-size: 12px; color: #6b7280;">${data.strain}</div>
                        </div>
                    `).join('')}
                </div>
                <p style="margin-top: 12px; font-size: 12px; color: #6b7280;">
                    Try searching by Sample ID (e.g., HP-POT-2024-014) or Strain Name (e.g., Green Crack)
                </p>
            </div>
        `;
        
        // Insert after search form
        const searchForm = document.querySelector('input[placeholder*="Sample"]').closest('div').parentNode;
        searchForm.appendChild(resultDiv);
    }
    
    // Initialize search
    setupSearch();
    
    console.log('Simple COA Search Fix loaded successfully!');
    console.log('Available tests:', Object.keys(COA_DATABASE).length);
});
