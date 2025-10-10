// Practical COA Search Fix - Shows real results only
console.log('Loading Practical COA Search Fix...');

window.addEventListener('load', function() {
    console.log('Page loaded, initializing practical COA search...');
    
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
    
    // Search function with minimum character requirement
    function searchCOA(searchTerm) {
        const term = searchTerm.trim();
        
        // Require minimum 3 characters
        if (term.length < 3) {
            return { error: 'minimum_length' };
        }
        
        const termUpper = term.toUpperCase();
        const results = [];
        
        // Find all matches
        for (const [id, data] of Object.entries(COA_DATABASE)) {
            if (id.toUpperCase().includes(termUpper) || 
                data.strain.toUpperCase().includes(termUpper)) {
                results.push({ id: id, data: data });
            }
        }
        
        return results.length > 0 ? { results: results } : { error: 'no_results' };
    }
    
    // Setup search functionality
    function setupSearch() {
        setTimeout(() => {
            const buttons = document.querySelectorAll('button');
            const inputs = document.querySelectorAll('input');
            
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
                console.log('Setting up practical search...');
                
                // Clone button to remove existing listeners
                const newBtn = searchBtn.cloneNode(true);
                searchBtn.parentNode.replaceChild(newBtn, searchBtn);
                
                newBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const searchTerm = searchInput.value.trim();
                    console.log('Searching for:', searchTerm);
                    
                    if (!searchTerm) {
                        showError('Please enter a Sample ID or Strain Name');
                        return;
                    }
                    
                    const result = searchCOA(searchTerm);
                    
                    if (result.error === 'minimum_length') {
                        showError('Please enter at least 3 characters to search');
                    } else if (result.error === 'no_results') {
                        showError(`No test results found for "${searchTerm}". Please check your Sample ID or Strain Name and try again.`);
                    } else if (result.results) {
                        showResults(result.results);
                    }
                });
                
                // Also handle Enter key
                searchInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        newBtn.click();
                    }
                });
                
                console.log('Practical search setup complete!');
            }
        }, 2000);
    }
    
    function showResults(results) {
        // Remove existing results
        const existing = document.getElementById('search-result');
        if (existing) existing.remove();
        
        const resultDiv = document.createElement('div');
        resultDiv.id = 'search-result';
        
        if (results.length === 1) {
            // Single result - show detailed view
            const result = results[0];
            resultDiv.innerHTML = `
                <div style="background: #d1fae5; border: 1px solid #10b981; border-radius: 8px; padding: 16px; margin: 16px 0;">
                    <h3 style="color: #065f46; margin: 0 0 12px 0;">Test Result Found</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
                        <div><strong>Sample ID:</strong> ${result.id}</div>
                        <div><strong>Test Type:</strong> Potency</div>
                        <div><strong>Strain:</strong> ${result.data.strain}</div>
                        <div><strong>THC:</strong> ${result.data.thc}</div>
                        <div><strong>Customer:</strong> HEMPATHY</div>
                        <div><strong>CBD:</strong> ${result.data.cbd}</div>
                    </div>
                    <button onclick="window.open('${result.data.file}', '_blank')" 
                            style="background: #1f2937; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px;">
                        📄 View Complete Certificate of Analysis
                    </button>
                </div>
            `;
        } else {
            // Multiple results - show list
            resultDiv.innerHTML = `
                <div style="background: #dbeafe; border: 1px solid #3b82f6; border-radius: 8px; padding: 16px; margin: 16px 0;">
                    <h3 style="color: #1e40af; margin: 0 0 12px 0;">Found ${results.length} Test Results</h3>
                    <div style="display: grid; gap: 12px;">
                        ${results.map(result => `
                            <div style="background: white; border: 1px solid #e5e7eb; border-radius: 6px; padding: 12px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <div style="font-weight: bold; color: #1f2937;">${result.id}</div>
                                    <div style="color: #6b7280; font-size: 14px;">${result.data.strain} • THC: ${result.data.thc} • CBD: ${result.data.cbd}</div>
                                </div>
                                <button onclick="window.open('${result.data.file}', '_blank')" 
                                        style="background: #1f2937; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; font-size: 12px;">
                                    View COA
                                </button>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }
        
        // Insert after search form
        const searchForm = document.querySelector('input[placeholder*="Sample"]').closest('div').parentNode;
        searchForm.appendChild(resultDiv);
    }
    
    function showError(message) {
        // Remove existing results
        const existing = document.getElementById('search-result');
        if (existing) existing.remove();
        
        const resultDiv = document.createElement('div');
        resultDiv.id = 'search-result';
        resultDiv.innerHTML = `
            <div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 16px; margin: 16px 0;">
                <p style="color: #991b1b; margin: 0;">${message}</p>
            </div>
        `;
        
        // Insert after search form
        const searchForm = document.querySelector('input[placeholder*="Sample"]').closest('div').parentNode;
        searchForm.appendChild(resultDiv);
    }
    
    // Initialize search
    setupSearch();
    
    console.log('Practical COA Search loaded - 18 tests available');
});
