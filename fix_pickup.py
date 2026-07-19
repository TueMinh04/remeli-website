from html.parser import HTMLParser
import re

class Translater(HTMLParser):
    def __init__(self, replacements):
        super().__init__(convert_charrefs=False)
        self.replacements = replacements
        self.output = []
        
    def handle_starttag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        
    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")
        
    def handle_startendtag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        
    def handle_data(self, data):
        data_stripped = data.strip()
        if data_stripped:
            for old, key in self.replacements:
                if re.sub(r'\s+', ' ', old.strip()) == re.sub(r'\s+', ' ', data_stripped):
                    for i in range(len(self.output)-1, -1, -1):
                        if self.output[i].startswith('<') and not self.output[i].startswith('</'):
                            tag_text = self.output[i]
                            if 'data-i18n=' not in tag_text:
                                space_idx = tag_text.find(' ')
                                if space_idx == -1:
                                    space_idx = tag_text.find('>')
                                self.output[i] = tag_text[:space_idx] + f' data-i18n="{key}"' + tag_text[space_idx:]
                            break
                    break
        self.output.append(data)
        
    def handle_entityref(self, name):
        self.output.append(f"&{name};")
        
    def handle_charref(self, name):
        self.output.append(f"&#{name};")
        
    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")
        
    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")
        
    def handle_pi(self, data):
        self.output.append(f"<?{data}>")

def process(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = Translater(replacements)
    parser.feed(content)
    
    new_content = "".join(parser.output)
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

pickup = [
    ("Trải nghiệm nhận hàng", "pickupPageTitle"),
    ("Hướng dẫn", "pickupHeroTitle1"),
    ("Pick up", "pickupHeroTitle2"),
    ("Thực hiện 4 bước đơn giản sau để nhận ngay phần ăn tuyệt hảo tại cửa hàng.", "pickupHeroDesc"),
    ("Đặt & Thanh toán", "pickupStep1"),
    ("Click chọn phần ăn bạn yêu thích và tiến hành thanh toán an toàn ngay trên ứng dụng.", "pickupStep1Desc"),
    ("Xem địa chỉ & Hướng dẫn", "pickupStep2"),
    ("Hệ thống sẽ hiện chi tiết địa chỉ cùng các hướng dẫn nhận món trực tiếp từ cửa hàng.", "pickupStep2Desc"),
    ("Mở mã QR trên App", "pickupStep3"),
    ("Khi đến cửa hàng, bạn chỉ cần mở ứng dụng và chuẩn bị sẵn mã QR xác nhận đơn hàng.", "pickupStep3Desc"),
    ("Scan QR & Nhận món", "pickupStep4"),
    ("Đưa mã QR cho nhân viên cửa hàng scan để hoàn tất việc xác nhận và mang món ngon về.", "pickupStep4Desc")
]

process('lam-sao-de-pick-up.html', pickup)
