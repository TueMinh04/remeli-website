import glob
import re

# 1. Get the footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', index_content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    
    # 2. Replace footer in all HTML files
    html_files = glob.glob('*.html')
    for file in html_files:
        if file == 'index.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace whatever is between <footer and </footer>
        new_content = re.sub(r'<footer class="site-footer">.*?</footer>', footer_html, content, flags=re.DOTALL)
        
        # If it was named footer without site-footer, handle it
        if new_content == content:
             new_content = re.sub(r'<footer.*?>.*?</footer>', footer_html, content, flags=re.DOTALL)
             
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    print("Footer copied to all files successfully.")
else:
    print("Could not find footer in index.html")
