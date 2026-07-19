import re

def add_i18n(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for old_text, i18n_key in replacements:
        # We look for the exact old_text wrapped in > and <, or we just replace the text itself
        # Since HTML can have newlines, we'll use a regex replacement that matches the text flexibly inside tags
        # Or even simpler, we can replace >old_text< with >old_text< but add data-i18n to the preceding tag
        # To make it robust, let's just do a string replacement of the tag containing it.
        # It's better to just write a simple regex that finds the tag containing the text and adds data-i18n to it
        
        # Escape the text for regex, replace spaces with \s+ to handle formatting
        escaped_text = re.escape(old_text).replace(r'\ ', r'\s+')
        
        # Regex to find <tag ...>text</tag>
        # We need to add data-i18n to the opening tag
        pattern = re.compile(r'(<[^>]+?)(>)\s*(' + escaped_text + r')\s*(</)', re.DOTALL)
        
        def replacer(match):
            tag_start = match.group(1)
            # if data-i18n is already there, don't add it
            if 'data-i18n="' in tag_start:
                return match.group(0)
            return f'{tag_start} data-i18n="{i18n_key}">{match.group(3)}{match.group(4)}'

        new_content = pattern.sub(replacer, content)
        if new_content == content:
            print(f"WARNING: Could not find or replace '{old_text}' in {filepath}")
        content = new_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# lam-sao-de-pick-up.html
pickup = [
    ("Hướng dẫn lấy món", "pickupGuide"),
    ("Làm sao để", "pickupHowTo"),
    ("nhận món?", "pickupReceive"),
    ("Đơn giản, nhanh chóng và thân thiện. Dưới đây là các bước để bạn lấy phần ăn đã đặt.", "pickupDesc"),
    ("Quy trình nhận món", "pickupProcess"),
    ("3 bước", "pickup3Steps"),
    ("tại cửa hàng", "pickupAtStore"),
    ("Bước 01", "appStep1"),
    ("Tới đúng giờ", "pickupStep1Title"),
    ("Đến cửa hàng trong khung giờ nhận được thông báo trên ứng dụng.", "pickupStep1Desc"),
    ("Bước 02", "appStep2"),
    ("Đưa mã cho nhân viên", "pickupStep2Title"),
    ("Mở app, đưa mã QR hoặc mã đơn hàng cho nhân viên cửa hàng xác nhận.", "pickupStep2Desc"),
    ("Bước 03", "appStep3"),
    ("Nhận phần ăn", "pickupStep3Title"),
    ("Tận hưởng món ngon và tự hào vì bạn vừa giúp giảm lãng phí thực phẩm!", "pickupStep3Desc")
]
add_i18n('lam-sao-de-pick-up.html', pickup)

# about-remeli.html
about = [
    ("Về chúng tôi", "aboutUs"),
    ("Câu chuyện", "aboutStory"),
    ("Remeli", "aboutRemeli"),
    ("Hành trình kết nối những bữa ăn ngon với sứ mệnh giảm thiểu lãng phí và bảo vệ môi trường Việt Nam.", "aboutHeroDesc"),
    ("Ý tưởng khởi nguồn", "aboutIdea"),
    ("Cứu lấy thức ăn, bảo vệ Trái Đất", "aboutSaveFood"),
    ("Tại Việt Nam, hàng tấn thức ăn hoàn toàn ngon lành bị lãng phí mỗi ngày chỉ vì chưa tìm được người dùng kịp thời. Remeli ra đời với một khát vọng đơn giản: tạo ra một nền tảng kết nối các cửa hàng thực phẩm với những người yêu ẩm thực, giúp <strong>cứu lấy những bữa ăn ngon</strong>, tiết kiệm chi phí, và quan trọng nhất là <strong>giảm thiểu lượng khí thải carbon</strong> gây hiệu ứng nhà kính từ rác thải thực phẩm.", "aboutVisionDesc"),
    ("Vì sao Remeli", "aboutWhyRemeli"),
    ("ra đời?", "aboutBorn"),
    ("Bảo vệ Môi trường", "aboutProtectEnv"),
    ("Mỗi phần ăn được cứu khỏi thùng rác đồng nghĩa với việc giảm thiểu lượng khí thải methane. Cùng nhau, chúng ta đang làm xanh lại bầu không khí của Việt Nam.", "aboutProtectEnvDesc"),
    ("Chống Lãng phí", "aboutFightWaste"),
    ("Chúng tôi tin rằng thức ăn ngon được tạo ra là để thưởng thức. Remeli giúp các nhà hàng tối ưu hoá nguồn nguyên liệu và không để phí phạm công sức đầu bếp.", "aboutFightWasteDesc"),
    ("Tiết kiệm & Gắn kết", "aboutSaveConnect"),
    ("Người dùng được ăn ngon với mức giá ưu đãi, cửa hàng có thêm thu nhập, và cộng đồng xích lại gần nhau hơn trong một mục tiêu chung vô cùng ý nghĩa.", "aboutSaveConnectDesc")
]
add_i18n('about-remeli.html', about)

# our-team.html
team = [
    ("Đội ngũ", "teamEyebrow2"),
    ("Người Việt", "teamVietnamese"),
    ("Kiến tạo", "teamCreate"),
    ("Chúng tôi là tập hợp những con\n        người Việt Nam trẻ tuổi, đầy đam mê, cùng chung một khát vọng giải quyết bài toán chống lãng phí thực phẩm tại\n        quê hương mình.", "teamVietnameseDesc"),
    ("Những nhà sáng lập", "teamFounders"),
    ("Nguyễn Văn A", "teamName1"),
    ("CEO & Founder", "teamRole1"),
    ("Trần Thị B", "teamName2"),
    ("Trưởng phòng Vận hành", "teamOps"),
    ("Lê Văn C", "teamName3"),
    ("Giám đốc Kỹ thuật", "teamTech"),
    ("Phạm Thị D", "teamName4"),
    ("Giám đốc Marketing", "teamMkt")
]
add_i18n('our-team.html', team)

# tac-dong.html
impact = [
    ("Tác động của Remeli", "impactOfRemeli"),
    ("Lựa chọn nhỏ", "impactSmallChoice"),
    ("Thay đổi lớn", "impactBigChange"),
    ("Hành động tuy nhỏ bé của bạn đang từng bước tạo ra những tác động khổng lồ, góp phần bảo vệ hành tinh xanh của chúng ta.", "impactHeroDesc"),
    ("25K+", "impactMetric1"),
    ("Phần ăn được giải cứu", "impactMealsSaved"),
    ("Hàng chục ngàn bữa ăn ngon miệng đã đến tay người dùng kịp thời thay vì kết thúc tại bãi rác.", "impactMealsSavedDesc"),
    ("8.4T", "impactMetric2"),
    ("CO₂e được ngăn chặn", "impactCO2"),
    ("Lượng khí thải carbon tương đương (CO₂e) khổng lồ được cắt giảm từ việc ngăn chặn rác thải.", "impactCO2Desc"),
    ("15.2T", "impactMetric3"),
    ("kg thức ăn được cứu", "impactKgSaved"),
    ("15.2 Tấn (tương đương 15,200 kg) nguyên liệu tươi ngon đã không bị lãng phí vô ích.", "impactKgSavedDesc"),
    ("Tầm nhìn bền vững", "impactVision"),
    ("Mỗi phần ăn được cứu", "impactEveryMeal"),
    ("là một bước tiến vì Trái Đất", "impactStepForEarth"),
    ("Lãng phí thực phẩm không chỉ là bài toán về kinh tế mà còn là gánh nặng khổng lồ đối với môi trường. Khi thức ăn bị vứt bỏ, toàn bộ năng lượng và nguồn tài nguyên nước dùng để gieo trồng, thu hoạch, vận chuyển và đóng gói cũng đều biến mất. Bằng việc đồng hành cùng Remeli, bạn đang góp phần vào một chuỗi cung ứng thực phẩm tuần hoàn, nơi mọi giá trị đều được trân trọng và Trái Đất được giảm tải áp lực.", "impactVisionDesc"),
    ("Tác động Môi trường", "impactEnvTitle"),
    ("Giảm thiểu", "impactReduce"),
    ("Khí nhà kính", "impactGreenhouse"),
    ("Thực phẩm khi bị chôn lấp sẽ sinh ra lượng lớn khí methane - loại khí gây hiệu ứng nhà kính mạnh gấp 25 lần so với CO₂. Bằng việc cứu lấy thức ăn, chúng ta trực tiếp ngăn chặn sự nóng lên toàn cầu và bảo vệ bầu không khí trong lành cho thế hệ tương lai.", "impactEnvDesc"),
    ("Tác động Kinh tế", "impactEconTitle"),
    ("Tối ưu hoá", "impactOptimize"),
    ("Nguồn lực", "impactResources"),
    ("Mọi nguyên liệu, nhân công và năng lượng để sản xuất ra một món ăn đều đáng giá. Remeli giúp các doanh nghiệp và nhà hàng thu hồi được chi phí sản xuất, đồng thời mang đến cho người tiêu dùng những bữa ăn chất lượng với mức giá vô cùng hợp lý.", "impactEconDesc"),
    ("Tác động Xã hội", "impactSocialTitle"),
    ("Gắn kết", "impactConnect"),
    ("Cộng đồng", "impactCommunity"),
    ("Không chỉ dừng lại ở việc mua bán, Remeli đang xây dựng một cộng đồng những người tiêu dùng có ý thức trách nhiệm cao. Chúng ta kết nối với nhau, với cửa hàng địa phương bằng một thông điệp tích cực: Sống xanh, tiêu dùng thông minh và trân trọng thức ăn.", "impactSocialDesc"),
    ("Trở thành một phần", "impactBePart"),
    ("của giải pháp", "impactOfSolution"),
    ("Tải Remeli ngay hôm nay để bắt đầu hành trình giải cứu thức ăn và bảo vệ môi trường cùng hàng chục ngàn người Việt Nam khác.", "impactCtaDesc"),
    ("Tải Ứng Dụng Ngay", "impactCtaBtn")
]
add_i18n('tac-dong.html', impact)

# phan-hoi-khach-hang.html
feedback = [
    ("Cộng đồng Remeli", "fbCommunity"),
    ("Tiếng nói từ", "fbVoice"),
    ("Cộng đồng", "fbComm"),
    ("Khám phá những trải nghiệm chân thực nhất từ hàng ngàn khách hàng và đối tác đã đồng hành cùng Remeli trên hành trình chống lãng phí.", "fbDesc"),
    ("Cảm nhận thực tế", "fbRealExp"),
    ("Bí kíp ăn ngon, giá hời!", "fbTitle1"),
    ('"App siêu tiện lợi luôn! Mình hay canh giờ tối để đặt túi mù từ tiệm bánh yêu thích. Vừa được ăn ngon, vừa tiết kiệm được kha khá tiền, cảm giác bóc quà bất ngờ lắm!"', "fbText1"),
    ("Thảo Nguyễn", "fbName1"),
    ("Người dùng • TP. HCM", "fbRole1"),
    ("Cứu cánh cuối tháng", "fbTitle2"),
    ('"Là sinh viên nên Remeli cứu rỗi ví tiền của mình rất nhiều. Thức ăn vẫn còn rất nóng hổi và chất lượng, hy vọng app mở rộng thêm nhiều cửa hàng gần trường mình hơn."', "fbText2"),
    ("Hoàng Hải", "fbName2"),
    ("Sinh viên • Hà Nội", "fbRole2"),
    ("Giải pháp chống lãng phí", "fbTitle3"),
    ('"Từ ngày đăng ký bán phần ăn cuối ngày trên Remeli, quán tôi không còn phải bỏ mứa đồ ăn nữa. Doanh thu tăng nhẹ nhưng vui nhất là không lãng phí công sức nấu nướng."', "fbText3"),
    ("Cơm Tấm Mười", "fbName3"),
    ("Đối tác • Quận 3", "fbRole3"),
    ("Hành động nhỏ, ý nghĩa lớn", "fbTitle4"),
    ('"Thật tuyệt vời khi được chung tay bảo vệ môi trường mỗi ngày chỉ bằng những bữa ăn ngon. Thiết kế app cực kỳ dễ thương và dễ sử dụng!"', "fbText4"),
    ("Mai Lan", "fbName4"),
    ("Người dùng • Đà Nẵng", "fbRole4"),
    ("Tiện lợi, mượt mà", "fbTitle5"),
    ('"Tính năng pick-up của app hoạt động cực kỳ mượt mà. Mình tan làm ghé ngang cửa hàng, chỉ cần đưa mã quét là nhận đồ ngay, không phải chờ đợi phút nào."', "fbText5"),
    ("Phan Anh", "fbName5"),
    ("Nhân viên văn phòng • TP.HCM", "fbRole5"),
    ("Niềm vui người thợ bánh", "fbTitle6"),
    ('"Không còn đau đầu vì bánh tồn kho mỗi tối, tôi cảm thấy rất biết ơn đội ngũ Remeli đã tạo ra một nền tảng thực sự ý nghĩa cho xã hội."', "fbText6"),
    ("Lò Bánh Tươi", "fbName6"),
    ("Chủ tiệm bánh • Hà Nội", "fbRole6")
]
add_i18n('phan-hoi-khach-hang.html', feedback)
