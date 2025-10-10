// Enhanced COA Lookup Fix for Static Hosting
// This script provides better search functionality and shows available tests

(function() {
    // Complete COA Database mapping with strain names for better search
    const COA_DATABASE = {
        'HP-POT-2024-001': { file: 'wemby_potency_HP_POT_2024_001.pdf', strain: 'Wemby', customer: 'HEMPATHY', thc: '28.57%', cbd: '1.87%' },
        'HP-POT-2024-002': { file: 'lemon_biscuits_potency_HP_POT_2024_002.pdf', strain: 'Lemon Biscuits', customer: 'HEMPATHY', thc: '24.12%', cbd: '0.89%' },
        'HP-POT-2024-003': { file: 'flapjacks_potency_HP_POT_2024_003.pdf', strain: 'Flapjacks', customer: 'HEMPATHY', thc: '26.34%', cbd: '1.23%' },
        'HP-POT-2024-004': { file: 'blackberry_potency_HP_POT_2024_004.pdf', strain: 'Blackberry', customer: 'HEMPATHY', thc: '26.54%', cbd: '4.78%' },
        'HP-POT-2024-005': { file: 'sherb_cream_pie_potency_HP_POT_2024_005.pdf', strain: 'Sherb Cream Pie', customer: 'HEMPATHY', thc: '25.67%', cbd: '1.45%' },
        'HP-POT-2024-006': { file: 'white_boy_cookies_potency_HP_POT_2024_006.pdf', strain: 'White Boy Cookies', customer: 'HEMPATHY', thc: '27.89%', cbd: '0.67%' },
        'HP-POT-2024-007': { file: 'space_candy_potency_HP_POT_2024_007.pdf', strain: 'Space Candy', customer: 'HEMPATHY', thc: '23.45%', cbd: '2.34%' },
        'HP-POT-2024-008': { file: 'og_biscuits_potency_HP_POT_2024_008.pdf', strain: 'OG Biscuits', customer: 'HEMPATHY', thc: '28.12%', cbd: '1.12%' },
        'HP-POT-2024-009': { file: 'lemon_berry_potency_HP_POT_2024_009.pdf', strain: 'Lemon Berry', customer: 'HEMPATHY', thc: '26.78%', cbd: '1.89%' },
        'HP-POT-2024-010': { file: 'biscotti_wedding_potency_HP_POT_2024_010.pdf', strain: 'Biscotti Wedding', customer: 'HEMPATHY', thc: '29.34%', cbd: '0.78%' },
        'HP-POT-2024-011': { file: 'italian_ice_potency_HP_POT_2024_011.pdf', strain: 'Italian Ice', customer: 'HEMPATHY', thc: '27.56%', cbd: '1.34%' },
        'HP-POT-2024-012': { file: '61_potency_HP_POT_2024_012.pdf', strain: '61', customer: 'HEMPATHY', thc: '25.89%', cbd: '2.12%' },
        'HP-POT-2024-013': { file: '41_potency_HP_POT_2024_013.pdf', strain: '41', customer: 'HEMPATHY', thc: '26.45%', cbd: '1.67%' },
        'HP-POT-2024-014': { file: 'green_crack_potency_HP_POT_2024_014.pdf', strain: 'Green Crack', customer: 'HEMPATHY', thc: '27.93%', cbd: '0.48%' },
        'G41-POT-2024-005': { file: 'gelato_41_potency_G41_POT_2024_005.pdf', strain: 'Gelato 41', customer: 'Green Labs', thc: '24.67%', cbd: '1.23%' },
        'BD-POT-2024-001': { file: 'blue_dream_professional_layout_BD_POT_2024_001.pdf', strain: 'Blue Dream', customer: 'Dream Labs', thc: '22.34%', cbd: '3.45%' },
        'GC-FULL-2024-001': { file: 'green_crack_full_panel_with_signatures_GC_FULL_2024_001.pdf', strain: 'Green Crack', customer: 'Premium Cannabis Co.', thc: '28.73%', cbd: '0.49%' },
        'TEST-FULL-001': { file: 'test_strain_full_panel_TEST-FULL-001.pdf', strain: 'Test Strain', customer: 'Test Customer', thc: '25.00%', cbd: '2.00%' }
    };

    // Create a search function that works with strain names too
    function searchCOA(searchTerm) {
        const term = searchTerm.toUpperCase();
        
        // First try exact sample ID match
        if (COA_DATABASE[searchTerm]) {
            return { id: searchTerm, data: COA_DATABASE[searchTerm] };
        }
        
        // Then try partial matches on sample ID or strain name
        for (const [id, data] of Object.entries(COA_DATABASE)) {
            if (id.toUpperCase().includes(term) || 
                data.strain.toUpperCase().includes(term) ||
                data.customer.toUpperCase().includes(term)) {
                return { id: id, data: data };
            }
        }
        
        return null;
    }

    // Override the React app's search functionality
    function interceptReactSearch() {
        // Wait for React to load
        setTimeout(() => {
            // Find search input and button
            const searchInput = document.querySelector('input[placeholder*="Sample ID"]');
            const searchButton = document.querySelector('button:contains("Search")') || 
                                document.querySelector('button[type="submit"]') ||
                                document.querySelectorAll('button')[document.querySelectorAll('button').length - 1];
            
            if (searchInput && searchButton) {
                // Remove existing event listeners and add our own
                const newSearchButton = searchButton.cloneNode(true);
                searchButton.parentNode.replaceChild(newSearchButton, searchButton);
                
                newSearchButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const searchTerm = searchInput.value.trim();
                    if (!searchTerm) return;
                    
                    const result = searchCOA(searchTerm);
                    if (result) {
                        // Create and show result
                        showSearchResult(result.id, result.data);
                    } else {
                        showNoResult(searchTerm);
                    }
                });
                
                // Also handle Enter key
                searchInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        newSearchButton.click();
                    }
                });
            }
        }, 1000);
    }

    function showSearchResult(sampleId, data) {
        // Find or create result container
        let resultContainer = document.getElementById('coa-search-result');
        if (!resultContainer) {
            resultContainer = document.createElement('div');
            resultContainer.id = 'coa-search-result';
            const searchForm = document.querySelector('input[placeholder*="Sample ID"]').closest('div').parentNode;
            searchForm.appendChild(resultContainer);
        }
        
        resultContainer.innerHTML = `
            <div style="background: #d1fae5; border: 1px solid #10b981; border-radius: 8px; padding: 16px; margin: 16px 0;">
                <h3 style="color: #065f46; margin: 0 0 12px 0;">Test Result Found</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
                    <div><strong>Sample ID:</strong> ${sampleId}</div>
                    <div><strong>Test Type:</strong> Potency</div>
                    <div><strong>Strain:</strong> ${data.strain}</div>
                    <div><strong>THC:</strong> ${data.thc}</div>
                    <div><strong>Customer:</strong> ${data.customer}</div>
                    <div><strong>CBD:</strong> ${data.cbd}</div>
                </div>
                <button onclick="window.open('${data.file}', '_blank')" 
                        style="background: #1f2937; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;">
                    📄 View Complete Certificate of Analysis
                </button>
            </div>
        `;
    }

    function showNoResult(searchTerm) {
        let resultContainer = document.getElementById('coa-search-result');
        if (!resultContainer) {
            resultContainer = document.createElement('div');
            resultContainer.id = 'coa-search-result';
            const searchForm = document.querySelector('input[placeholder*="Sample ID"]').closest('div').parentNode;
            searchForm.appendChild(resultContainer);
        }
        
        const availableIds = Object.keys(COA_DATABASE).slice(0, 10); // Show first 10
        
        resultContainer.innerHTML = `
            <div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 16px; margin: 16px 0;">
                <h3 style="color: #991b1b; margin: 0 0 12px 0;">No Results Found</h3>
                <p>No test found for "${searchTerm}"</p>
                <p><strong>Available Sample IDs (examples):</strong></p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 4px; font-family: monospace; font-size: 12px;">
                    ${availableIds.map(id => `<div>${id}</div>`).join('')}
                </div>
                <p style="margin-top: 12px; font-size: 12px; color: #6b7280;">
                    You can search by Sample ID, Strain Name, or Customer Name
                </p>
            </div>
        `;
    }

    // Initialize when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', interceptReactSearch);
    } else {
        interceptReactSearch();
    }

    // Also try again after a delay in case React takes time to render
    setTimeout(interceptReactSearch, 2000);
    setTimeout(interceptReactSearch, 5000);

    console.log('Enhanced COA Lookup loaded - ' + Object.keys(COA_DATABASE).length + ' tests available');
    console.log('Available Sample IDs:', Object.keys(COA_DATABASE));
})();
