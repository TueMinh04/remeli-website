with open('vi-sao-gia-nhap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all instances of script.js script tag
content = content.replace('<script src="script.js"></script>', '')
# Also remove any leftover empty lines if possible, but it's fine.

# Add the script tag right before </body>
content = content.replace('</body>', '<script src="script.js"></script>\n</body>')

with open('vi-sao-gia-nhap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed script order.")
