import re

with open('index.html', 'r') as f:
    html = f.read()

# All CSS enhancements
all_css = """
/* Achievement Counter Animation */
.stat-number {
    display: inline-block;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--gold) 0%, var(--olive) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-item {
    text-align: center;
    padding: 1.5rem;
}

.stat-label {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #666;
}

/* Testimonial Cards */
.testimonial-snippet {
    background: linear-gradient(135deg, #F5F3EE 0%, #FAF9F6 100%);
    border-left: 4px solid var(--gold);
    padding: 1.5rem;
    margin: 2rem 0;
    border-radius: 8px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
}

.testimonial-snippet:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.testimonial-snippet blockquote {
    font-style: italic;
    font-size: 1.1rem;
    line-height: 1.6;
    margin: 0 0 1rem 0;
    color: #333;
}

.testimonial-snippet cite {
    font-style: normal;
    color: var(--gold);
    font-weight: 600;
}

/* Skill Category Filters */
.skill-filters {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 0.75rem 1.5rem;
    background: transparent;
    border: 2px solid var(--olive);
    border-radius: 50px;
    color: var(--olive);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.filter-btn:hover {
    background: var(--olive);
    color: white;
    transform: translateY(-2px);
}

.filter-btn.active {
    background: var(--gold);
    border-color: var(--gold);
    color: white;
}

/* Micro-interactions */
.skill-node:hover .node-circle {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 8px 30px rgba(212, 175, 55, 0.3);
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Resume Download Button */
.resume-download-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2rem;
    background: var(--gold);
    color: var(--black);
    border-radius: 50px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    margin-top: 2rem;
}

.resume-download-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
}

.resume-download-btn .btn-arrow {
    transition: transform 0.3s ease;
}

.resume-download-btn:hover .btn-arrow {
    transform: translateX(5px);
}

/* Currently Learning Badge */
.learning-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid var(--gold);
    border-radius: 50px;
    font-size: 0.9rem;
    margin-top: 1rem;
}

.pulse-dot {
    width: 8px;
    height: 8px;
    background: var(--gold);
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.5); opacity: 0.5; }
}

/* Gradient Headers */
.section-title {
    background: linear-gradient(135deg, var(--gold) 0%, var(--olive) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Parallax */
.hero {
    background-attachment: fixed;
}
"""

html = html.replace('</style>', all_css + '\n    </style>')

# JavaScript enhancements
enhanced_js = """
        // Achievement Counter Animation
        function animateCounters() {
            const statNumbers = document.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target') || stat.textContent.replace(/[^0-9]/g, ''));
                stat.setAttribute('data-target', target);
                
                let current = 0;
                const increment = target / 50;
                const duration = 2000;
                const stepTime = duration / 50;
                
                const counter = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.textContent = target.toLocaleString();
                        clearInterval(counter);
                    } else {
                        stat.textContent = Math.floor(current).toLocaleString();
                    }
                }, stepTime);
            });
        }

        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');
                    animateCounters();
                }
            });
        }, { threshold: 0.5 });

        const aboutSection = document.querySelector('#about');
        if (aboutSection) statsObserver.observe(aboutSection);

        // Skill Filters
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                
                const category = e.target.dataset.category;
                document.querySelectorAll('.skill-node').forEach(node => {
                    if (category === 'all' || node.dataset.category === category) {
                        node.style.display = 'flex';
                        node.style.opacity = '1';
                    } else {
                        node.style.opacity = '0.2';
                    }
                });
            });
        });

        // Konami Code Easter Egg
        let konamiCode = [];
        const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

        document.addEventListener('keydown', (e) => {
            konamiCode.push(e.key);
            konamiCode = konamiCode.slice(-10);
            
            if (konamiCode.join(',') === konamiSequence.join(',')) {
                document.body.style.animation = 'rainbow 5s linear infinite';
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes rainbow {
                        0% { filter: hue-rotate(0deg); }
                        100% { filter: hue-rotate(360deg); }
                    }
                `;
                document.head.appendChild(style);
                
                setTimeout(() => {
                    alert('🎉 You found the secret! Prasad appreciates attention to detail. Let\\'s talk!');
                }, 500);
            }
        });
"""

html = html.replace('    </script>', enhanced_js + '\n    </script>')

with open('index.html', 'w') as f:
    f.write(html)

print('✅ Enhancements applied!')
