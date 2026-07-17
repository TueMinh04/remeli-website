import os
import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Change color: var(--green-900); to color: var(--white);
    new_content = content.replace(
        '<h4 style="margin-top: 20px; margin-bottom: 8px; color: var(--green-900); font-weight: 700; font-size: 1rem;">Doanh nghiệp</h4>',
        '<h4 style="margin-top: 20px; margin-bottom: 8px; color: var(--white); font-weight: 700; font-size: 1.1rem;">Doanh nghiệp</h4>'
    )
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed color in {f}")
    else:
        print(f"No changes in {f}")
