// Final Simple COA Search - Last 6 characters only
window.addEventListener('load', function() {
    setTimeout(() => {
        const COA_DB = {
            '24-001': 'wemby_potency_HP_POT_2024_001.pdf',
            '24-002': 'lemon_biscuits_potency_HP_POT_2024_002.pdf',
            '24-003': 'flapjacks_potency_HP_POT_2024_003.pdf',
            '24-004': 'blackberry_potency_HP_POT_2024_004.pdf',
            '24-005': 'sherb_cream_pie_potency_HP_POT_2024_005.pdf',
            '24-006': 'white_boy_cookies_potency_HP_POT_2024_006.pdf',
            '24-007': 'space_candy_potency_HP_POT_2024_007.pdf',
            '24-008': 'og_biscuits_potency_HP_POT_2024_008.pdf',
            '24-009': 'lemon_berry_potency_HP_POT_2024_009.pdf',
            '24-010': 'biscotti_wedding_potency_HP_POT_2024_010.pdf',
            '24-011': 'italian_ice_potency_HP_POT_2024_011.pdf',
            '24-012': '61_potency_HP_POT_2024_012.pdf',
            '24-013': '41_potency_HP_POT_2024_013.pdf',
            '24-014': 'green_crack_potency_HP_POT_2024_014.pdf'
        };
        
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Search'));
        const input = document.querySelector('input[placeholder*="Sample"]');
        
        if (btn && input) {
            const newBtn = btn.cloneNode(true);
            btn.parentNode.replaceChild(newBtn, btn);
            
            newBtn.onclick = (e) => {
                e.preventDefault();
                e.stopPropagation();
                const val = input.value.trim();
                const file = COA_DB[val];
                
                document.getElementById('result')?.remove();
                const div = document.createElement('div');
                div.id = 'result';
                
                if (file) {
                    div.innerHTML = `<div style="background:#d1fae5;border:1px solid #10b981;border-radius:8px;padding:16px;margin:16px 0;"><h3 style="color:#065f46;margin:0 0 12px 0;">Test Found</h3><button onclick="window.open('${file}','_blank')" style="background:#1f2937;color:white;padding:12px 24px;border:none;border-radius:4px;cursor:pointer;">View COA</button></div>`;
                } else {
                    div.innerHTML = `<div style="background:#fef2f2;border:1px solid #f87171;border-radius:8px;padding:16px;margin:16px 0;"><p style="color:#991b1b;margin:0;">No test found for "${val}". Try format: 24-014</p></div>`;
                }
                
                input.closest('div').parentNode.appendChild(div);
            };
        }
    }, 3000);
});
