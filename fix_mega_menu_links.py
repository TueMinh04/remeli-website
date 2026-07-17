import os
import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the anchor links in the mega menu
    content = content.replace('href="doanh-nghiep.html#vi-sao-gia-nhap"', 'href="vi-sao-gia-nhap.html"')
    content = content.replace('href="doanh-nghiep.html#dang-ki"', 'href="dang-ki-doanh-nghiep.html"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Fixed mega menu links in {f}")

