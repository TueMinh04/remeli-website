import os

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert html font-size
if 'html {' not in content:
    content = content.replace('body {', 'html {\n  font-size: 14.5px;\n}\n\nbody {')

# 2. Reduce massive header sizes
# .hero-title
content = content.replace('clamp(2.9rem, 6.8vw, 6.4rem)', 'clamp(2.5rem, 5.5vw, 5rem)')
# h2 / .split-title / .section-title
content = content.replace('clamp(1.8rem, 3.6vw, 3.4rem)', 'clamp(1.6rem, 3vw, 2.8rem)')
# h3 / .split-item-title
content = content.replace('clamp(1.4rem, 2.5vw, 2.6rem)', 'clamp(1.3rem, 2.2vw, 2.2rem)')
# override
content = content.replace('clamp(2.8rem, 5vw, 4.2rem)', 'clamp(2.4rem, 4.5vw, 3.6rem)')
# mobile hero title
content = content.replace('clamp(2.9rem, 13vw, 4.7rem)', 'clamp(2.5rem, 11vw, 4rem)')
# .step-title
content = content.replace('clamp(1.9rem, 4vw, 3rem)', 'clamp(1.7rem, 3.5vw, 2.6rem)')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Font sizes shrunken successfully.")
