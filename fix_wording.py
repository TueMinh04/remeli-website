import os
import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the footer and anywhere else
    new_content = content.replace('Đăng ký gian hàng', 'Đăng ký doanh nghiệp')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed wording in {f}")
    else:
        pass
