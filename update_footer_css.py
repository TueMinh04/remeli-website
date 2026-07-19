import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# .site-footer gap and padding
content = content.replace('gap: 70px;', 'gap: 40px;')
content = content.replace('padding: 64px max(24px, calc((100vw - var(--max)) / 2)) 34px;', 'padding: 40px max(24px, calc((100vw - var(--max)) / 2)) 24px;\n  font-size: 0.88rem;')

# .footer-links gap
content = content.replace('gap: 38px;', 'gap: 24px;')

# footer heading margins
content = content.replace('margin: 0 0 14px;', 'margin: 0 0 10px;')

# link margins
content = content.replace('margin: 10px 0;', 'margin: 8px 0;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated footer CSS.")
