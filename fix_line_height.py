import re

for filename in ['vi-sao-gia-nhap.html', 'dang-ki-doanh-nghiep.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace line-height: 1.1; with line-height: 1.3;
    content = content.replace('line-height: 1.1;', 'line-height: 1.35;')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed line-height in both files.")
