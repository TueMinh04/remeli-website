import re

# 1. Get the real form from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# We need the form inside merchantModal
start_str = '<h2 id="merchantModalTitle"'
form_start_idx = index_content.find('<form class="stacked-form"', index_content.find(start_str))
form_end_idx = index_content.find('</form>', form_start_idx) + 7
real_form = index_content[form_start_idx:form_end_idx]

# Inject the 'on-page-form' class and specific styling
real_form = real_form.replace('class="stacked-form"', 'class="stacked-form on-page-form" style="width: 100%; max-width: 500px; margin: 0 auto; text-align: left;"')

# 2. Replace the mock form in dang-ki-doanh-nghiep.html
with open('dang-ki-doanh-nghiep.html', 'r', encoding='utf-8') as f:
    page_content = f.read()

# Find the mock form
mock_start = page_content.find('<form style="width: 100%; max-width: 600px;')
mock_end = page_content.find('</form>', mock_start) + 7

if mock_start != -1:
    page_content = page_content[:mock_start] + real_form + page_content[mock_end:]
else:
    print("Could not find mock form.")

# Add custom CSS for on-page-form in the <head> of dang-ki-doanh-nghiep.html
css_injection = """
  <style>
    .on-page-form label {
      color: var(--yellow-soft) !important;
      font-size: 1rem !important;
      font-weight: 600 !important;
    }
    .on-page-form input, .on-page-form select {
      font-size: 1rem !important;
      padding: 14px 18px !important;
      border-radius: 12px !important;
    }
    .on-page-form button {
      font-size: 1.1rem !important;
      padding: 16px !important;
      border-radius: 12px !important;
      margin-top: 8px;
    }
  </style>
"""
if '<style>' not in page_content:
    page_content = page_content.replace('</head>', css_injection + '</head>')

with open('dang-ki-doanh-nghiep.html', 'w', encoding='utf-8') as f:
    f.write(page_content)

print("Form replaced successfully.")
