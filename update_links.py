import os
import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the main "Doanh nghiệp" link in both nav and footer
    content = content.replace('href="doanh-nghiep.html"', 'href="vi-sao-gia-nhap.html"')
    
    # 2. Because of #1, the anchor links became 'href="vi-sao-gia-nhap.html#vi-sao-gia-nhap"'
    # We fix that:
    content = content.replace('href="vi-sao-gia-nhap.html#vi-sao-gia-nhap"', 'href="vi-sao-gia-nhap.html"')
    content = content.replace('href="vi-sao-gia-nhap.html#dang-ki"', 'href="dang-ki-doanh-nghiep.html"')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated links in {f}")
