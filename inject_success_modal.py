# 1. Get successModal from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

start_str = '<div class="modal" id="successModal"'
modal_start = index_content.find(start_str)
# Find the closing </div> of this modal by counting divs or just finding the next modal
modal_end = index_content.find('<iframe name="hidden_iframe"', modal_start)
success_modal_html = index_content[modal_start:modal_end]

# 2. Inject into dang-ki-doanh-nghiep.html
with open('dang-ki-doanh-nghiep.html', 'r', encoding='utf-8') as f:
    page_content = f.read()

if 'id="successModal"' not in page_content:
    page_content = page_content.replace('<iframe name="hidden_iframe"', success_modal_html + '\n<iframe name="hidden_iframe"')
    
with open('dang-ki-doanh-nghiep.html', 'w', encoding='utf-8') as f:
    f.write(page_content)

print("Injected successModal successfully.")
