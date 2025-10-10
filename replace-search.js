// Aggressive React Search Replacement
window.addEventListener('load', function() {
    let attempts = 0;
    const maxAttempts = 50;
    
    function replaceSearch() {
        attempts++;
        
        // Find the search container
        const searchContainer = document.querySelector('div').parentNode;
        if (!searchContainer) {
            if (attempts < maxAttempts) {
                setTimeout(replaceSearch, 100);
            }
            return;
        }
        
        // Find elements that contain "Find Your Test Results"
        const elements = Array.from(document.querySelectorAll('*')).filter(el => 
            el.textContent && el.textContent.includes('Find Your Test Results')
        );
        
        if (elements.length === 0) {
            if (attempts < maxAttempts) {
                setTimeout(replaceSearch, 100);
            }
            return;
        }
        
        // Find the parent container
        let container = elements[0];
        while (container && !container.querySelector('input')) {
            container = container.parentNode;
        }
        
        if (!container) {
            if (attempts < maxAttempts) {
                setTimeout(replaceSearch, 100);
            }
            return;
        }
        
        // Replace the entire search section
        container.innerHTML = `
            <div style="text-align: center; padding: 20px;">
                <h2 style="color: #1f2937; margin-bottom: 10px;">Find Your Test Results</h2>
                <p style="color: #6b7280; margin-bottom: 30px;">Enter your Sample ID (e.g., 24-014) to view your Certificate of Analysis</p>
                
                <div style="max-width: 400px; margin: 0 auto;">
                    <input id="newSearch" type="text" placeholder="Enter Sample ID (e.g., 24-014)" 
                           style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 8px; font-size: 16px; margin-bottom: 15px; box-sizing: border-box;">
                    <button onclick="doSearch()" 
                            style="background: #2563eb; color: white; padding: 12px 30px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%;">
                        Search
                    </button>
                </div>
                
                <div id="searchResult" style="margin-top: 20px;"></div>
            </div>
        `;
        
        console.log('Search replaced successfully');
    }
    
    // Start replacement attempts
    setTimeout(replaceSearch, 1000);
});

// COA Database
const COA_DB = {
    '24-001': { file: 'wemby_potency_HP_POT_2024_001.pdf', strain: 'Wemby', thc: '28.57%', cbd: '1.87%' },
    '24-002': { file: 'lemon_biscuits_potency_HP_POT_2024_002.pdf', strain: 'Lemon Biscuits', thc: '26.43%', cbd: '0.52%' },
    '24-003': { file: 'flapjacks_potency_HP_POT_2024_003.pdf', strain: 'Flapjacks', thc: '24.87%', cbd: '0.73%' },
    '24-004': { file: 'blackberry_potency_HP_POT_2024_004.pdf', strain: 'Blackberry', thc: '26.54%', cbd: '4.78%' },
    '24-005': { file: 'sherb_cream_pie_potency_HP_POT_2024_005.pdf', strain: 'Sherb Cream Pie', thc: '25.92%', cbd: '0.61%' },
    '24-006': { file: 'white_boy_cookies_potency_HP_POT_2024_006.pdf', strain: 'White Boy Cookies', thc: '27.34%', cbd: '0.48%' },
    '24-007': { file: 'space_candy_potency_HP_POT_2024_007.pdf', strain: 'Space Candy', thc: '23.76%', cbd: '0.89%' },
    '24-008': { file: 'og_biscuits_potency_HP_POT_2024_008.pdf', strain: 'OG Biscuits', thc: '28.12%', cbd: '0.54%' },
    '24-009': { file: 'lemon_berry_potency_HP_POT_2024_009.pdf', strain: 'Lemon Berry', thc: '26.87%', cbd: '0.67%' },
    '24-010': { file: 'biscotti_wedding_potency_HP_POT_2024_010.pdf', strain: 'Biscotti Wedding', thc: '29.43%', cbd: '0.43%' },
    '24-011': { file: 'italian_ice_potency_HP_POT_2024_011.pdf', strain: 'Italian Ice', thc: '27.65%', cbd: '0.58%' },
    '24-012': { file: '61_potency_HP_POT_2024_012.pdf', strain: '61', thc: '28.91%', cbd: '0.39%' },
    '24-013': { file: '41_potency_HP_POT_2024_013.pdf', strain: '41', thc: '27.23%', cbd: '0.72%' },
    '24-014': { file: 'green_crack_potency_HP_POT_2024_014.pdf', strain: 'Green Crack', thc: '27.93%', cbd: '0.48%' }
};

function doSearch() {
    const input = document.getElementById('newSearch').value.trim();
    const result = document.getElementById('searchResult');
    
    if (!input) {
        result.innerHTML = '<div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px; color: #991b1b;">Please enter a Sample ID</div>';
        return;
    }
    
    const coa = COA_DB[input];
    if (coa) {
        result.innerHTML = `
            <div style="background: #d1fae5; border: 1px solid #10b981; border-radius: 8px; padding: 20px; color: #065f46;">
                <h3 style="margin: 0 0 15px 0; color: #065f46;">Test Found!</h3>
                <p style="margin: 5px 0;"><strong>Sample ID:</strong> HP-POT-2024-${input.split('-')[1]}</p>
                <p style="margin: 5px 0;"><strong>Strain:</strong> ${coa.strain}</p>
                <p style="margin: 5px 0 15px 0;"><strong>THC:</strong> ${coa.thc} | <strong>CBD:</strong> ${coa.cbd}</p>
                <button onclick="window.open('${coa.file}', '_blank')" 
                        style="background: #1f2937; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;">
                    View Complete Certificate of Analysis
                </button>
            </div>
        `;
    } else {
        result.innerHTML = `<div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px; color: #991b1b;">No test found for "${input}". Please check the Sample ID and try again.</div>`;
    }
}
