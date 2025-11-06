html_file = 'index.html'
with open(html_file, 'r') as f:
    html = f.read()

# Check if chai button already exists
if 'chai-cup-button' not in html or 'id="chaiButton"' not in html:
    
    chai_html = '''
    <!-- Floating Chai Cup - Back to Top -->
    <button class="chai-cup-button" id="chaiButton" aria-label="Scroll to top">
        <svg class="steam" width="30" height="25" xmlns="http://www.w3.org/2000/svg">
            <path class="steam-line" d="M 8 20 Q 8 10, 8 0" />
            <path class="steam-line" d="M 15 20 Q 15 10, 15 0" />
            <path class="steam-line" d="M 22 20 Q 22 10, 22 0" />
        </svg>
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M 6 6 L 8 18 C 8 19 9 20 10 20 L 14 20 C 15 20 16 19 16 18 L 18 6 Z" 
                  fill="none" stroke="currentColor" stroke-width="2"/>
            <path d="M 18 8 Q 22 8, 22 12 Q 22 16, 18 16" 
                  fill="none" stroke="currentColor" stroke-width="2"/>
            <ellipse cx="12" cy="6" rx="6" ry="1.5" 
                     fill="none" stroke="currentColor" stroke-width="2"/>
        </svg>
    </button>
'''
    
    # Add HTML before </body>
    html = html.replace('</body>', chai_html + '\n</body>')
    print('✅ Chai HTML added!')
else:
    print('⚠️  Chai HTML already exists')

# Check if JavaScript exists
if 'chaiButton' not in html or 'getElementById' not in html or 'chaiButton' not in html:
    
    chai_js = """
        // Floating Chai Cup - Scroll to Top
        const chaiButton = document.getElementById('chaiButton');
        if (chaiButton) {
            window.addEventListener('scroll', () => {
                if (window.scrollY > 500) {
                    chaiButton.classList.add('visible');
                } else {
                    chaiButton.classList.remove('visible');
                }
            });
            
            chaiButton.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
"""
    
    # Add JS before closing script tag
    html = html.replace('    </script>', chai_js + '\n    </script>')
    print('✅ Chai JavaScript added!')
else:
    print('⚠️  Chai JavaScript already exists')

with open(html_file, 'w') as f:
    f.write(html)

print('🍵 CHAI CUP COMPLETE!')
