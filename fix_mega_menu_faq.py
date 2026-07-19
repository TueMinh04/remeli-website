import glob
import re

for filename in glob.glob("*.html"):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace inside the main-nav's mega menu column.
    # The target string is:
    # <a href="phan-hoi-khach-hang.html" data-i18n="megaCustomerFeedback">Phản hồi khách hàng</a>
    # Or variations of it (with or without data-i18n, etc, but we've normalized it recently)
    
    # We will search for:
    # <a href="phan-hoi-khach-hang.html" data-i18n="megaCustomerFeedback">Phản hồi khách hàng</a>
    # and check if the next line is </div> or FAQ.
    
    # Find all occurrences
    target = '<a href="phan-hoi-khach-hang.html" data-i18n="megaCustomerFeedback">Phản hồi khách hàng</a>'
    insert = '<a href="faq.html" data-i18n="navFaq">FAQ</a>'
    
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        if target in line:
            # Check if next line is already FAQ
            if i + 1 < len(lines) and insert in lines[i+1]:
                pass # already there
            else:
                # Insert FAQ with same indentation
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + insert)
        i += 1
        
    new_content = '\n'.join(new_lines)
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
