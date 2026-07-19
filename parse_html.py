import re
import json
import glob
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_nodes = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        if tag == 'script' or tag == 'style':
            self.in_script = True

    def handle_endtag(self, tag):
        if tag == 'script' or tag == 'style':
            self.in_script = False

    def handle_data(self, data):
        if not self.in_script and data.strip():
            self.text_nodes.append(data.strip())

files = ['huong-dan-tai-app.html', 'lam-sao-de-pick-up.html', 'about-remeli.html', 'our-team.html', 'tac-dong.html', 'phan-hoi-khach-hang.html']
results = {}
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        parser = MyHTMLParser()
        parser.feed(file.read())
        # Filter out text nodes that are probably translated or short/irrelevant
        # like "Remeli", "VI", "EN", etc.
        valid_nodes = [t for t in parser.text_nodes if len(t) > 3 and t not in ['Remeli', 'VI | EN', 'VI', 'EN', '© 2026 Remeli. All rights reserved.', 'Trang chủ', 'Tác động', 'Cộng đồng', 'FAQ', 'App', 'Hướng dẫn tải App', 'Làm sao để pick up', 'About us', 'About Remeli', 'Our team', 'Phản hồi khách hàng', 'Dành cho Doanh nghiệp', 'Vì sao gia nhập Remeli', 'Đăng ký doanh nghiệp', 'Tham gia sớm', 'Download on the', 'App Store', 'Get it on Google Play', 'Món ngon còn đây, tiết kiệm trong tay.Save Food · Save Money · Save Tomorrow', 'Khám phá', 'Cách hoạt động', 'Doanh nghiệp', 'Pháp lý', 'Điều khoản sử dụng', 'Chính sách bảo mật', 'Chính sách hoàn tiền', 'Liên hệ', 'TP. Hồ Chí Minh, Việt Nam', 'Tham gia danh sách chờ', 'Nhận thông tin sớm nhất từ Remeli', 'Để lại thông tin để Remeli báo cho bạn khi ra mắt tại thành phố của bạn.', 'Email của bạn', 'Thành phố', 'Chọn thành phố', 'Hà Nội', 'Đà Nẵng', 'Cần Thơ', 'Khác', 'Bạn là?', 'Chọn', 'Người dùng', 'Chủ cửa hàng', 'Tham gia danh sách chờ', 'Món ngon còn đây, tiết kiệm trong tay.']]
        
        # also need to remove duplicates and string with only symbols
        filtered = []
        for v in valid_nodes:
            if v not in filtered and re.search('[a-zA-Z]', v):
                filtered.append(v)
        results[f] = filtered

print(json.dumps(results, indent=2, ensure_ascii=False))
