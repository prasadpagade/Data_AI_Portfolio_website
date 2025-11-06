import re

html_file = 'index.html'
with open(html_file, 'r') as f:
    html = f.read()

# Remove old chai CSS
html = re.sub(r'/\* Floating Chai Cup - Back to Top \*/.*?(?=\n/\*|\n    </style>)', '', html, flags=re.DOTALL)

# GOLD CLASSY CHAI CSS
new_chai_css = """
/* Floating Chai Cup - Back to Top (Gold Classy Edition) */
.chai-cup-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 65px;
    height: 65px;
    background: var(--cream);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 20px rgba(212, 175, 55, 0.15);
    opacity: 0;
    visibility: hidden;
    transform: translateY(100px);
    transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 1000;
    border: 2px solid var(--gold);
}

.chai-cup-button.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.chai-cup-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(212, 175, 55, 0.35);
    border-color: var(--gold);
    background: var(--off-white);
}

.chai-cup-button svg {
    width: 38px;
    height: 38px;
    fill: none;
    stroke: var(--gold);
    stroke-width: 2.5;
    stroke-linecap: round;
    stroke-linejoin: round;
    transition: all 0.3s ease;
}

.chai-cup-button:hover svg {
    stroke: var(--gold);
    transform: scale(1.05);
}

/* Continuous Rising Steam */
.steam {
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
}

.steam-line {
    fill: none;
    stroke: var(--gold);
    stroke-width: 2;
    stroke-linecap: round;
    opacity: 0;
    animation: steam-rise-continuous 3s ease-in-out infinite;
}

.steam-line:nth-child(1) {
    animation-delay: 0s;
}

.steam-line:nth-child(2) {
    animation-delay: 1s;
}

.steam-line:nth-child(3) {
    animation-delay: 2s;
}

@keyframes steam-rise-continuous {
    0% {
        opacity: 0;
        transform: translateY(0) translateX(0);
    }
    20% {
        opacity: 0.6;
    }
    40% {
        opacity: 0.8;
    }
    60% {
        opacity: 0.6;
    }
    80% {
        opacity: 0.3;
    }
    100% {
        opacity: 0;
        transform: translateY(-25px) translateX(3px);
    }
}

/* Mobile */
@media (max-width: 768px) {
    .chai-cup-button {
        width: 55px;
        height: 55px;
        bottom: 20px;
        right: 20px;
    }
    
    .chai-cup-button svg {
        width: 32px;
        height: 32px;
    }
}
"""

# Insert new CSS before </style>
html = html.replace('</style>', new_chai_css + '\n    </style>')

with open(html_file, 'w') as f:
    f.write(html)

print('✅ GOLD CHAI CUP - CLASSY & SEAMLESS!')
print('💛 Gold outline cup')
print('✨ Gold continuous steam')
print('🍵 Cream background')
print('⭕ Gold border')
