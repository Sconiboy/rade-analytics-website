// COA Lookup Fix for Static Hosting
// This script intercepts COA lookup requests and redirects to PDF files

(function() {
    // COA Database mapping
    const COA_DATABASE = {
        'HP-POT-2024-001': 'wemby_potency_HP_POT_2024_001.pdf',
        'HP-POT-2024-002': 'lemon_biscuits_potency_HP_POT_2024_002.pdf',
        'HP-POT-2024-003': 'flapjacks_potency_HP_POT_2024_003.pdf',
        'HP-POT-2024-004': 'blackberry_potency_HP_POT_2024_004.pdf',
        'HP-POT-2024-005': 'sherb_cream_pie_potency_HP_POT_2024_005.pdf',
        'HP-POT-2024-006': 'white_boy_cookies_potency_HP_POT_2024_006.pdf',
        'HP-POT-2024-007': 'space_candy_potency_HP_POT_2024_007.pdf',
        'HP-POT-2024-008': 'og_biscuits_potency_HP_POT_2024_008.pdf',
        'HP-POT-2024-009': 'lemon_berry_potency_HP_POT_2024_009.pdf',
        'HP-POT-2024-010': 'biscotti_wedding_potency_HP_POT_2024_010.pdf',
        'HP-POT-2024-011': 'italian_ice_potency_HP_POT_2024_011.pdf',
        'HP-POT-2024-012': '61_potency_HP_POT_2024_012.pdf',
        'HP-POT-2024-013': '41_potency_HP_POT_2024_013.pdf',
        'HP-POT-2024-014': 'green_crack_potency_HP_POT_2024_014.pdf',
        'G41-POT-2024-005': 'gelato_41_potency_G41_POT_2024_005.pdf',
        'BD-POT-2024-001': 'blue_dream_professional_layout_BD_POT_2024_001.pdf',
        'GC-FULL-2024-001': 'green_crack_full_panel_with_signatures_GC_FULL_2024_001.pdf',
        'TEST-FULL-001': 'test_strain_full_panel_TEST-FULL-001.pdf'
    };

    // Override fetch to intercept COA requests
    const originalFetch = window.fetch;
    window.fetch = function(url, options) {
        // Check if this is a COA lookup request
        if (typeof url === 'string' && url.includes('/tests/')) {
            const sampleId = url.split('/tests/')[1];
            const pdfFile = COA_DATABASE[sampleId];
            
            if (pdfFile) {
                // Redirect to PDF file
                window.open(pdfFile, '_blank');
                return Promise.resolve(new Response('', { status: 200 }));
            }
        }
        
        // For all other requests, use original fetch
        return originalFetch.apply(this, arguments);
    };

    // Also intercept any direct navigation attempts
    const originalOpen = window.open;
    window.open = function(url, target, features) {
        if (typeof url === 'string' && url.includes('/tests/')) {
            const sampleId = url.split('/tests/')[1];
            const pdfFile = COA_DATABASE[sampleId];
            
            if (pdfFile) {
                return originalOpen.call(this, pdfFile, target, features);
            }
        }
        
        return originalOpen.apply(this, arguments);
    };

    // Intercept any anchor clicks that might go to /tests/
    document.addEventListener('click', function(e) {
        const target = e.target.closest('a');
        if (target && target.href && target.href.includes('/tests/')) {
            e.preventDefault();
            const sampleId = target.href.split('/tests/')[1];
            const pdfFile = COA_DATABASE[sampleId];
            
            if (pdfFile) {
                window.open(pdfFile, '_blank');
            }
        }
    });

    console.log('COA Lookup Fix loaded - redirecting API calls to PDF files');
})();
