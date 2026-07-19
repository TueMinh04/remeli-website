const header = document.getElementById('siteHeader');
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.querySelectorAll('.main-nav a');
const revealItems = document.querySelectorAll('.reveal');
const foodCloud = document.getElementById('foodCloud');
const foodItems = document.querySelectorAll('.food-item');
const parallaxTargets = document.querySelectorAll('.hero-line, .soft-blob');
const metaDescription = document.querySelector('meta[name="description"]');
const languageButtons = document.querySelectorAll('[data-lang-switch]');

const translations = {
  vi: {
    pageTitle: 'Remeli | Món ngon còn đây, tiết kiệm trong tay',
    metaDescription: 'Remeli giúp bạn tìm món ngon còn lại trong ngày từ cửa hàng địa phương tại Việt Nam, đặt trước dễ dàng và nhận tại cửa hàng.',
    brandAria: 'Remeli trang chủ',
    menuOpen: 'Mở menu',
    mainMenu: 'Menu chính',
    languageLabel: 'Đổi ngôn ngữ',
    scrollCue: 'Cuộn xuống phần cách hoạt động',
    marqueeLabel: 'Danh mục món chạy ngang',
    socialLabel: 'Mạng xã hội',
    closeModal: 'Đóng',

    navHome: 'Trang chủ',
    navHow: 'Cách hoạt động',
    navMerchant: 'Doanh nghiệp',
    navImpact: 'Tác động',
    navCommunity: 'Cộng đồng',
    navFaq: 'FAQ',
    joinEarly: 'Tham gia sớm',
    waitlistButton: 'Tham gia danh sách chờ',
    recommendStoreButton: 'Giới thiệu cửa hàng',

    megaApp: 'Ứng dụng',
    megaDownloadApp: 'Hướng dẫn tải Remeli',
    megaHowToPickup: 'Hướng dẫn nhận hàng',
    megaAboutUs: 'Về chúng tôi',
    megaAboutRemeli: 'Về Remeli',
    megaOurTeam: 'Đội ngũ',
    megaCommunity: 'Cộng đồng',
    megaImpact: 'Tác động',
    megaCustomerFeedback: 'Phản hồi khách hàng',

    heroTitle: '<span>Món ngon còn đây</span><span>Tiết kiệm trong tay</span>',
    heroSubtitle: 'Save Food · Save Money · Save Tomorrow',

    marqueeBakery: 'Tiệm bánh',
    marqueeCafe: 'Quán cà phê',
    marqueeMeal: 'Nhà hàng',
    marqueeBanhMi: 'Siêu thị',
    marqueeEat: 'Ăn ngon hơn',
    marqueeSave: 'Tiết kiệm hơn',
    marqueeLessWaste: 'Lãng phí ít hơn',

    howEyebrow: 'Đơn giản & minh bạch',
    howTitle: '<span>Cách Remeli</span><span>hoạt động</span>',
    howDescription: '<span>Ba bước đơn giản để bạn ăn ngon hơn,</span><span>tiết kiệm hơn và lãng phí ít hơn mỗi ngày.</span>',
    stepOneTitle: 'Tìm món gần bạn',
    stepOneText: 'Khám phá cửa hàng gần bạn đang có phần món ngon cuối ngày.',
    stepTwoTitle: 'Đặt trước',
    stepTwoText: 'Chọn gói/món phù hợp, xem giá, số lượng và thời gian nhận.',
    stepThreeTitle: 'Đến nhận',
    stepThreeText: 'Ghé cửa hàng trong khung giờ đã chọn và nhận món dễ dàng.',

    foodEyebrow: 'Không chỉ là một món ngon',
    foodTitle: '<span>Remeli mang đến</span><span>điều gì?</span>',
    foodDescription: 'Một lần đặt nhỏ có thể giúp bạn tiết kiệm, khám phá gần hơn và giảm lãng phí hơn.',
    impactSaveTitle: 'Tiết kiệm',
    impactSaveText: 'Ăn ngon với mức giá dễ chịu hơn mỗi ngày.',
    impactEnvTitle: 'Bảo vệ môi trường',
    impactEnvText: 'Góp phần giảm lãng phí qua từng phần ăn được sử dụng.',
    impactDiscoverTitle: 'Khám phá món mới',
    impactDiscoverText: 'Cơ hội trải nghiệm những quán ăn trước giờ bạn đã bỏ quên.',
    impactLocalTitle: 'Hỗ trợ cửa hàng',
    impactLocalText: 'Giúp cửa hàng địa phương mang những món ngon đến với người tiêu dùng.',
    bagSmall: 'Cửa hàng địa phương',

    whyEyebrow: 'Remeli mang đến ảnh hưởng gì?',
    whyTitle: 'Lựa chọn nhỏ, thay đổi lớn',
    benefitSaveTitle: '25K+',
    benefitSaveText: 'Phần ăn được giải cứu',
    benefitLocalTitle: '8.4T',
    benefitLocalText: 'Ckg CO₂e được ngăn chặn',
    benefitWasteTitle: '15.2T',
    benefitWasteText: 'kg food được cứu',

    merchantEyebrow: 'Dành cho chủ cửa hàng',
    merchantTitle: '<span>Bán hết dễ dàng</span><span>vận hành nhẹ nhàng.</span>',
    merchantDescription: 'Remeli giúp bạn bán phần món còn ngon trong ngày một cách đơn giản và hiệu quả.',
    merchantCta: 'Đăng ký cửa hàng',
    merchantPointOne: 'Tạo đơn dễ dàng',
    merchantPointTwo: 'Tự chọn số lượng, giá và giờ nhận',
    merchantPointThree: 'Khách đặt trước và đến nhận',
    merchantPointFour: 'Báo cáo đơn giản, dễ theo dõi',

    communityEyebrow: 'Cộng đồng Remeli',
    communityTitle: 'Cùng giới thiệu những cửa hàng bạn yêu thích.',
    communityDescription: 'Một cửa hàng tốt đôi khi chỉ cần thêm một cách mới để gặp đúng khách hàng.',

    faqEyebrow: 'FAQ',
    faqTitle: 'Câu hỏi thường gặp',
    faq1Q: 'Remeli có phải app giao đồ ăn không?',
    faq1A: 'Không. Remeli tập trung vào việc giúp người dùng đặt giữ phần ăn còn tốt trong app và đến nhận tại cửa hàng trong khung giờ đã chọn. Mô hình này giúp giảm chi phí vận hành và phù hợp với giai đoạn đầu tại Việt Nam.',
    faq2Q: 'Tôi có đặt món trên website được không?',
    faq2A: 'Không. Website Remeli dùng để giới thiệu, gửi link tải app, nhận thông tin người dùng và đối tác. Việc tìm món, đặt giữ phần, thanh toán hoặc xác nhận đơn được xử lý trong app Remeli.',
    faq3Q: 'Món trong hộp có biết trước không?',
    faq3A: 'Tùy cửa hàng. Một số hộp có thể mô tả rõ danh mục món, một số là hộp món linh hoạt dựa trên lượng còn trong ngày. Remeli khuyến khích cửa hàng ghi rõ loại món, khẩu phần, khung giờ nhận và lưu ý dị ứng.',
    faq4Q: 'Đồ ăn có an toàn không?',
    faq4A: 'Đối tác F&B chịu trách nhiệm chỉ đăng món còn tốt và phù hợp để sử dụng trong khung giờ nhận. Remeli yêu cầu đối tác cung cấp thông tin rõ ràng và phối hợp xử lý khi có phản hồi từ người dùng.',
    faq5Q: 'Nếu tôi đến trễ thì sao?',
    faq5A: 'Mỗi phần ăn có khung giờ nhận cụ thể. Nếu đến ngoài khung giờ, cửa hàng có thể không giữ được phần ăn. Điều kiện hỗ trợ sẽ được hiển thị trong app trước khi xác nhận.',
    faq6Q: 'Tôi thanh toán bằng cách nào?',
    faq6A: 'Phương thức thanh toán được hiển thị trong app tại thời điểm đặt giữ phần,  Remeli cho phép dùng thẻ tín dụng và ví ngân hàng điện tử.',
    faq7Q: 'Tôi có thể yêu cầu xóa thông tin cá nhân không?',
    faq7A: 'Có. Bạn có thể gửi yêu cầu liên quan đến thông tin cá nhân qua form liên hệ hoặc email remeli.vn@gmail.com. Remeli sẽ xử lý theo chính sách quyền riêng tư và quy định pháp luật áp dụng.',
    faq8Q: 'Cửa hàng đăng ký Remeli có mất phí không?',
    faq8A: 'Chi tiết phí và mô hình hợp tác sẽ được trao đổi trực tiếp khi cửa hàng đăng ký tư vấn. Remeli cần hiểu loại hình, khu vực, quy mô và quy trình vận hành trước khi đề xuất phương án phù hợp.',
    faq9Q: 'Remeli có phù hợp với quán nhỏ không?',
    faq9A: 'Có. Remeli được thiết kế để cả quán nhỏ, tiệm bánh, quán cà phê và cửa hàng địa phương đều có thể đăng phần ăn còn tốt với thao tác đơn giản.',
    faq10Q: 'Tôi muốn hợp tác truyền thông hoặc cộng đồng thì liên hệ ở đâu?',
    faq10A: 'Bạn có thể gửi thông tin qua form liên hệ hoặc gửi email tới <a href="mailto:remeli.vn@gmail.com">remeli.vn@gmail.com</a>.',

    footerSlogan: 'Món ngon còn đây, tiết kiệm trong tay.<br />Save Food · Save Money · Save Tomorrow',
    footerExplore: 'Khám phá',
    footerLegal: 'Pháp lý',
    footerContact: 'Liên hệ',
    terms: 'Điều khoản sử dụng',
    privacy: 'Chính sách bảo mật',
    refund: 'Chính sách hoàn tiền',
    location: 'TP. Hồ Chí Minh, Việt Nam',

    waitlistEyebrow: 'Tham gia danh sách chờ',
    waitlistModalTitle: 'Nhận thông tin sớm nhất từ Remeli',
    waitlistModalText: 'Để lại thông tin để Remeli báo cho bạn khi ra mắt tại thành phố của bạn.',
    emailLabel: 'Email của bạn',
    emailShortLabel: 'Email',
    emailPlaceholder: 'name@gmail.com',
    phonePlaceholder: '09xxxxxxxx',
    cityLabel: 'Thành phố',
    cityPlaceholder: 'Chọn thành phố',
    cityHanoi: 'Hà Nội',
    cityDanang: 'Đà Nẵng',
    cityCantho: 'Cần Thơ',
    cityOther: 'Khác',
    roleLabel: 'Bạn là?',
    rolePlaceholder: 'Chọn',
    roleUser: 'Người dùng',
    roleMerchant: 'Chủ cửa hàng',
    roleOther: 'Khác',

    // Nav & Footer
    megaForBusiness: 'Dành cho Doanh nghiệp',
    megaWhyJoin: 'Vì sao gia nhập Remeli',
    megaRegisterBusiness: 'Đăng ký doanh nghiệp',
    footerMerchantSection: 'Doanh nghiệp',
    footerWhyJoin: 'Vì sao gia nhập Remeli',
    footerRegisterBusiness: 'Đăng ký doanh nghiệp',

    // Vì sao gia nhập
    whyHeroEyebrow: 'Dành cho đối tác',
    whyHeroTitle: 'Mở rộng kinh doanh,<br/><span style="color: var(--yellow);">Giảm thiểu lãng phí</span>',
    whyHeroDesc: 'Đồng hành cùng Remeli để biến lượng thức ăn dư thừa cuối ngày<br/>thành nguồn doanh thu mới và thu hút thêm lượng lớn khách hàng tiềm năng.',
    whyHeroBtn: 'Đăng ký đối tác ngay',
    whyBenefitEyebrow: 'Lợi ích thiết thực',
    whyBenefitTitle: 'Vì sao gia nhập Remeli?',
    whyBen1Title: 'Giảm thiểu lãng phí',
    whyBen1Desc: 'Không còn nỗi đau phải bỏ đi những mẻ bánh ngon hay nồi canh tâm huyết. Remeli giúp bạn tối ưu hoá 100% nguyên liệu sản xuất mỗi ngày.',
    whyBen2Title: 'Thêm nguồn thu nhập',
    whyBen2Desc: 'Biến thức ăn thừa thành tiền. Những sản phẩm từng bị lãng quên giờ đây sẽ mang lại doanh thu gia tăng cho cửa hàng của bạn một cách dễ dàng.',
    whyBen3Title: 'Khách hàng tiềm năng',
    whyBen3Desc: 'Tiếp cận hàng ngàn người dùng trẻ tuổi, yêu môi trường qua app. Họ đến nhận món và hoàn toàn có thể trở thành khách hàng trung thành của quán.',
    whyOpEyebrow: 'Vận hành đơn giản',
    whyOpTitle: 'Chỉ với 3 bước mỗi ngày',
    whyStep1Title: 'Đóng gói & Cập nhật',
    whyStep1Desc: 'Vào cuối ca làm, bạn chụp ảnh các phần ăn còn dư (hoặc gom vào Túi mù - Surprise Bag) và lên app cập nhật số lượng chỉ trong 5 giây.',
    whyStep2Title: 'Khách đặt qua App',
    whyStep2Desc: 'Người dùng trong khu vực sẽ nhận được thông báo, tiến hành thanh toán giữ chỗ trực tiếp trên ứng dụng Remeli.',
    whyStep3Title: 'Giao món tận tay',
    whyStep3Desc: 'Khách ghé tiệm theo khung giờ quy định, bạn chỉ cần quét mã QR xác nhận và giao túi thức ăn. Tiền sẽ tự động cộng vào ví!',
    whyMetric1: 'Phí khởi tạo ban đầu',
    whyMetric2: 'Doanh thu ước tính tăng thêm',
    whyMetric3Value: 'Hỗ trợ',
    whyMetric3: 'Marketing độc quyền 0đ',
    whyCtaTitle: 'Bắt đầu hành trình<br/>chống lãng phí cùng Remeli',
    whyCtaDesc: 'Tham gia hoàn toàn miễn phí. Hàng ngàn khách hàng đang chờ để "giải cứu" những món ngon của bạn mỗi ngày.',
    whyCtaBtn: 'Đăng ký cửa hàng ngay',

    // Đăng ký doanh nghiệp
    regHeroEyebrow: 'Đăng ký doanh nghiệp',
    regHeroTitle: 'Trở thành đối tác<br/><span style="color: var(--yellow);">cùng Remeli</span>',
    regHeroDesc: 'Hãy để lại thông tin, chúng tôi sẽ giúp bạn biến thức ăn cuối ngày thành nguồn doanh thu mới ngay hôm nay.',
    regFormTitle: 'Đăng ký cửa hàng',
    regFormDesc: 'Để lại thông tin, đội ngũ Remeli sẽ liên hệ hỗ trợ bạn thiết lập gian hàng chỉ trong vòng 24 giờ. Hoàn toàn miễn phí đăng ký!',
    regFormName: 'Tên cửa hàng *',
    regFormNamePlace: 'Nhập tên quán ăn, nhà hàng, tiệm bánh...',
    regFormPhone: 'Số điện thoại *',
    regFormPhonePlace: 'Nhập số điện thoại liên hệ...',
    regFormArea: 'Khu vực (Thành phố/Quận) *',
    regFormAreaPlace: 'Ví dụ: Quận 1, TP.HCM...',
    regFormSubmit: 'Gửi thông tin đăng ký',

    // App Instructions
    appDownloadApp: 'Tải ứng dụng',
    appGetStarted: 'Bắt đầu với',
    appRemeli: 'Remeli',

    appEasyDaily: 'Easy to use every day',
    appEasyDesc: 'With just a few basic steps on the app, you can enjoy delicious food at great prices.',
    appStep1: 'Step 01',
    appFindSelect: 'Find & Select',
    appFood: 'your food',
    appStep1Desc2: 'Open the app, discover nearby stores, and choose your favorite food at a discounted price.',
    appStep2: 'Step 02',
    appReserve: 'Reserve &',
    appPay: 'Pay',
    appStep2Desc2: 'Pay and reserve in advance through the app to ensure your meal is always ready.',
    appStep3: 'Step 03',
    appArrive: 'Arrive',
    appPickup: '(Pick up)',
    appStep3Desc2: 'Go directly to the store during the designated time window to pick up your hot food easily.',
    appImg1: '[Illustration 1]',
    appImg2: '[Illustration 2]',
    appImg3: '[Illustration 3]',

    appEasyDaily: 'Dễ dàng sử dụng mỗi ngày',
    appEasyDesc: 'Chỉ với vài thao tác cơ bản trên ứng dụng, bạn đã có thể tận hưởng món ngon với mức giá siêu hời.',
    appStep1: 'Bước 01',
    appFindSelect: 'Tìm & Chọn',
    appFood: 'món ăn',
    appStep1Desc2: 'Mở ứng dụng, khám phá các cửa hàng xung quanh và chọn gói món ăn bạn yêu thích với mức giá siêu hời.',
    appStep2: 'Bước 02',
    appReserve: 'Đặt chỗ &',
    appPay: 'Thanh toán',
    appStep2Desc2: 'Thanh toán và giữ chỗ trước qua ứng dụng để đảm bảo phần ăn của bạn luôn sẵn sàng.',
    appStep3: 'Bước 03',
    appArrive: 'Đến lấy',
    appPickup: '(Pick up)',
    appStep3Desc2: 'Đến trực tiếp cửa hàng theo đúng khung giờ quy định để nhận món ăn nóng hổi một cách dễ dàng.',
    appImg1: '[Hình ảnh minh hoạ 1]',
    appImg2: '[Hình ảnh minh hoạ 2]',
    appImg3: '[Hình ảnh minh hoạ 3]',
    appHeroDesc: 'Khám phá các phần ăn ngon cuối ngày từ các nhà hàng xung quanh bạn.<br />Tải ứng dụng trên App Store hoặc Google Play ngay hôm nay!',
    appSmooth: 'Trải nghiệm mượt mà',
    appJustOneMin: 'Chỉ 1 phút',
    appToStart: 'để bắt đầu',
    appNoComplex: 'Bạn không cần tạo tài khoản phức tạp. Đăng nhập bằng Apple, Google hoặc số điện thoại chỉ trong vài giây.',
    appStep1Title: 'Tải ứng dụng',
    appStep1Desc: 'Tìm Remeli trên kho ứng dụng App Store hoặc Google Play và cài đặt hoàn toàn miễn phí.',
    appStep2Title: 'Đăng nhập nhanh',
    appStep2Desc: 'Sử dụng tài khoản Google, Apple hoặc số điện thoại để vào app ngay lập tức.',
    appStep3Title: 'Khám phá',
    appStep3Desc: 'Bật định vị để xem ngay các cửa hàng đang có phần ăn hấp dẫn xung quanh bạn.',

    // How to pick up
    pickupPageTitleDoc: 'Remeli | Trải nghiệm nhận hàng',
    pickupImageAlt: '[Hình ảnh minh hoạ Pick up]',
    pickupPageTitle: 'Trải nghiệm nhận hàng',
    pickupHeroTitle1: 'Hướng dẫn',
    pickupHeroTitle2: 'Pick up',
    pickupHeroDesc: 'Thực hiện 4 bước đơn giản sau để nhận ngay phần ăn tuyệt hảo tại cửa hàng.',
    pickupStep1: 'Đặt & Thanh toán',
    pickupStep1Desc: 'Click chọn phần ăn bạn yêu thích và tiến hành thanh toán an toàn ngay trên ứng dụng.',
    pickupStep2: 'Xem địa chỉ & Hướng dẫn',
    pickupStep2Desc: 'Hệ thống sẽ hiện chi tiết địa chỉ cùng các hướng dẫn nhận món trực tiếp từ cửa hàng.',
    pickupStep3: 'Mở mã QR trên App',
    pickupStep3Desc: 'Khi đến cửa hàng, bạn chỉ cần mở ứng dụng và chuẩn bị sẵn mã QR xác nhận đơn hàng.',
    pickupStep4: 'Scan QR & Nhận món',
    pickupStep4Desc: 'Đưa mã QR cho nhân viên cửa hàng scan để hoàn tất việc xác nhận và mang món ngon về.',
    
    // Impact Page

    // Pickup Guide
    pickupGuide: 'Hướng dẫn lấy món',
    pickupHowTo: 'Làm sao để',
    pickupReceive: 'nhận món?',
    pickupDesc: 'Đơn giản, nhanh chóng và thân thiện. Dưới đây là các bước để bạn lấy phần ăn đã đặt.',
    pickupProcess: 'Quy trình nhận món',
    pickup3Steps: '3 bước',
    pickupAtStore: 'tại cửa hàng',
    pickupStep1Title: 'Tới đúng giờ',
    pickupStep1Desc: 'Đến cửa hàng trong khung giờ nhận được thông báo trên ứng dụng.',
    pickupStep2Title: 'Đưa mã cho nhân viên',
    pickupStep2Desc: 'Mở app, đưa mã QR hoặc mã đơn hàng cho nhân viên cửa hàng xác nhận.',
    pickupStep3Title: 'Nhận phần ăn',
    pickupStep3Desc: 'Tận hưởng món ngon và tự hào vì bạn vừa giúp giảm lãng phí thực phẩm!',

    // About Remeli
    aboutUs: 'Về chúng tôi',
    aboutStory: 'Câu chuyện',
    aboutRemeli: 'Remeli',
    aboutHeroDesc: 'Hành trình kết nối những bữa ăn ngon với sứ mệnh giảm thiểu lãng phí và bảo vệ môi trường Việt Nam.',
    aboutIdea: 'Ý tưởng khởi nguồn',
    aboutSaveFood: 'Cứu lấy thức ăn, bảo vệ Trái Đất',
    aboutVisionDesc: 'Tại Việt Nam, hàng tấn thức ăn hoàn toàn ngon lành bị lãng phí mỗi ngày chỉ vì chưa tìm được người dùng kịp thời. Remeli ra đời với một khát vọng đơn giản: tạo ra một nền tảng kết nối các cửa hàng thực phẩm với những người yêu ẩm thực, giúp <strong>cứu lấy những bữa ăn ngon</strong>, tiết kiệm chi phí, và quan trọng nhất là <strong>giảm thiểu lượng khí thải carbon</strong> gây hiệu ứng nhà kính từ rác thải thực phẩm.',
    aboutWhyRemeli: 'Vì sao Remeli',
    aboutBorn: 'ra đời?',
    aboutProtectEnv: 'Bảo vệ Môi trường',
    aboutProtectEnvDesc: 'Mỗi phần ăn được cứu khỏi thùng rác đồng nghĩa với việc giảm thiểu lượng khí thải methane. Cùng nhau, chúng ta đang làm xanh lại bầu không khí của Việt Nam.',
    aboutFightWaste: 'Chống Lãng phí',
    aboutFightWasteDesc: 'Chúng tôi tin rằng thức ăn ngon được tạo ra là để thưởng thức. Remeli giúp các nhà hàng tối ưu hoá nguồn nguyên liệu và không để phí phạm công sức đầu bếp.',
    aboutSaveConnect: 'Tiết kiệm & Gắn kết',
    aboutSaveConnectDesc: 'Người dùng được ăn ngon với mức giá ưu đãi, cửa hàng có thêm thu nhập, và cộng đồng xích lại gần nhau hơn trong một mục tiêu chung vô cùng ý nghĩa.',

    // Our Team
    teamEyebrow: 'Đội ngũ Remeli',
    teamPeople: 'Những người',
    teamBehind: 'đứng sau Remeli',
    teamDesc: 'Một nhóm những người trẻ đam mê công nghệ, ẩm thực và môi trường, chung tay vì một Việt Nam xanh hơn.',
    teamVision: 'Tầm nhìn chung',
    teamNotJustApp: 'Chúng tôi không chỉ',
    teamMakingApp: 'làm một ứng dụng',
    teamVisionDesc: 'Chúng tôi đang xây dựng một cộng đồng những người quan tâm đến bữa ăn của mình và môi trường xung quanh. Mục tiêu là biến việc "cứu" thức ăn trở thành một thói quen hàng ngày của mọi người.',
    teamVietnamese: 'Người Việt',
    teamCreate: 'Kiến tạo',
    teamVietnameseDesc: 'Chúng tôi là tập hợp những con người Việt Nam trẻ tuổi, đầy đam mê, cùng chung một khát vọng giải quyết bài toán chống lãng phí thực phẩm tại quê hương mình.',
    teamFounders: 'Những nhà sáng lập',
    teamOurGroup: 'Nhóm chúng tôi',
    teamEyebrow2: 'Đội ngũ',
    teamOps: 'Trưởng phòng Vận hành',
    teamTech: 'Giám đốc Kỹ thuật',
    teamMkt: 'Giám đốc Marketing',

    // Impact
    impactOfRemeli: 'Tác động của Remeli',
    impactSmallChoice: 'Lựa chọn nhỏ',
    impactBigChange: 'Thay đổi lớn',
    impactHeroDesc: 'Hành động tuy nhỏ bé của bạn đang từng bước tạo ra những tác động khổng lồ, góp phần bảo vệ hành tinh xanh của chúng ta.',
    impactMetric1: '25K+',
    impactMealsSaved: 'Phần ăn được giải cứu',
    impactMealsSavedDesc: 'Hàng chục ngàn bữa ăn ngon miệng đã đến tay người dùng kịp thời thay vì kết thúc tại bãi rác.',
    impactMetric2: '8.4T',
    impactCO2: 'CO₂e được ngăn chặn',
    impactCO2Desc: 'Lượng khí thải carbon tương đương (CO₂e) khổng lồ được cắt giảm từ việc ngăn chặn rác thải.',
    impactMetric3: '15.2T',
    impactKgSaved: 'kg thức ăn được cứu',
    impactKgSavedDesc: '15.2 Tấn (tương đương 15,200 kg) nguyên liệu tươi ngon đã không bị lãng phí vô ích.',
    impactVision: 'Tầm nhìn bền vững',
    impactEveryMeal: 'Mỗi phần ăn được cứu',
    impactStepForEarth: 'là một bước tiến vì Trái Đất',
    impactVisionDesc: 'Lãng phí thực phẩm không chỉ là bài toán về kinh tế mà còn là gánh nặng khổng lồ đối với môi trường. Khi thức ăn bị vứt bỏ, toàn bộ năng lượng và nguồn tài nguyên nước dùng để gieo trồng, thu hoạch, vận chuyển và đóng gói cũng đều biến mất. Bằng việc đồng hành cùng Remeli, bạn đang góp phần vào một chuỗi cung ứng thực phẩm tuần hoàn, nơi mọi giá trị đều được trân trọng và Trái Đất được giảm tải áp lực.',
    impactEnvTitle: 'Tác động Môi trường',
    impactReduce: 'Giảm thiểu',
    impactGreenhouse: 'Khí nhà kính',
    impactEnvDesc: 'Thực phẩm khi bị chôn lấp sẽ sinh ra lượng lớn khí methane - loại khí gây hiệu ứng nhà kính mạnh gấp 25 lần so với CO₂. Bằng việc cứu lấy thức ăn, chúng ta trực tiếp ngăn chặn sự nóng lên toàn cầu và bảo vệ bầu không khí trong lành cho thế hệ tương lai.',
    impactEconTitle: 'Tác động Kinh tế',
    impactOptimize: 'Tối ưu hoá',
    impactResources: 'Nguồn lực',
    impactEconDesc: 'Mọi nguyên liệu, nhân công và năng lượng để sản xuất ra một món ăn đều đáng giá. Remeli giúp các doanh nghiệp và nhà hàng thu hồi được chi phí sản xuất, đồng thời mang đến cho người tiêu dùng những bữa ăn chất lượng với mức giá vô cùng hợp lý.',
    impactSocialTitle: 'Tác động Xã hội',
    impactConnect: 'Gắn kết',
    impactCommunity: 'Cộng đồng',
    impactSocialDesc: 'Không chỉ dừng lại ở việc mua bán, Remeli đang xây dựng một cộng đồng những người tiêu dùng có ý thức trách nhiệm cao. Chúng ta kết nối với nhau, với cửa hàng địa phương bằng một thông điệp tích cực: Sống xanh, tiêu dùng thông minh và trân trọng thức ăn.',
    impactBePart: 'Trở thành một phần',
    impactOfSolution: 'của giải pháp',
    impactCtaDesc: 'Tải Remeli ngay hôm nay để bắt đầu hành trình giải cứu thức ăn và bảo vệ môi trường cùng hàng chục ngàn người Việt Nam khác.',
    impactCtaBtn: 'Tải Ứng Dụng Ngay',

    // Feedback
    fbCommunity: 'Cộng đồng Remeli',
    fbVoice: 'Tiếng nói từ',
    fbComm: 'Cộng đồng',
    fbUsers: 'Người dùng',
    fbDesc: 'Khám phá những trải nghiệm chân thực nhất từ hàng ngàn khách hàng và đối tác đã đồng hành cùng Remeli trên hành trình chống lãng phí.',
    fbRealExp: 'Cảm nhận thực tế',
    fbTitle1: 'Bí kíp ăn ngon, giá hời!',
    fbText1: '"App siêu tiện lợi luôn! Mình hay canh giờ tối để đặt túi mù từ tiệm bánh yêu thích. Vừa được ăn ngon, vừa tiết kiệm được kha khá tiền, cảm giác bóc quà bất ngờ lắm!"',
    fbRole1: 'Người dùng • TP. HCM',
    fbTitle2: 'Cứu cánh cuối tháng',
    fbText2: '"Là sinh viên nên Remeli cứu rỗi ví tiền của mình rất nhiều. Thức ăn vẫn còn rất nóng hổi và chất lượng, hy vọng app mở rộng thêm nhiều cửa hàng gần trường mình hơn."',
    fbRole2: 'Sinh viên • Hà Nội',
    fbTitle3: 'Giải pháp chống lãng phí',
    fbText3: '"Từ ngày đăng ký bán phần ăn cuối ngày trên Remeli, quán tôi không còn phải bỏ mứa đồ ăn nữa. Doanh thu tăng nhẹ nhưng vui nhất là không lãng phí công sức nấu nướng."',
    fbRole3: 'Đối tác • Quận 3',
    fbTitle4: 'Hành động nhỏ, ý nghĩa lớn',
    fbText4: '"Thật tuyệt vời khi được chung tay bảo vệ môi trường mỗi ngày chỉ bằng những bữa ăn ngon. Thiết kế app cực kỳ dễ thương và dễ sử dụng!"',
    fbRole4: 'Người dùng • Đà Nẵng',
    fbTitle5: 'Tiện lợi, mượt mà',
    fbText5: '"Tính năng pick-up của app hoạt động cực kỳ mượt mà. Mình tan làm ghé ngang cửa hàng, chỉ cần đưa mã quét là nhận đồ ngay, không phải chờ đợi phút nào."',
    fbRole5: 'Nhân viên văn phòng • TP.HCM',
    fbTitle6: 'Niềm vui người thợ bánh',
    fbText6: '"Không còn đau đầu vì bánh tồn kho mỗi tối, tôi cảm thấy rất biết ơn đội ngũ Remeli đã tạo ra một nền tảng thực sự ý nghĩa cho xã hội."',
    fbRole6: 'Chủ tiệm bánh • Hà Nội',

    storeModalTitle: 'Giới thiệu cửa hàng',
    storeModalText: 'Biết một cửa hàng nên có mặt trên Remeli? Gửi thông tin để đội ngũ Remeli tìm hiểu thêm.',
    storeNameLabel: 'Tên cửa hàng',
    storeNamePlaceholder: 'Ví dụ: Tiệm Bánh Mây',
    storeAddressLabel: 'Khu vực / địa chỉ',
    storeAddressPlaceholder: 'Ví dụ: Quận 3, TP. Hồ Chí Minh',
    foodTypeLabel: 'Loại món',
    foodTypePlaceholder: 'Tiệm bánh, Quán cà phê, Siêu thị...',
    sendRecommendation: 'Gửi giới thiệu',

    merchantModalTitle: 'Đăng ký cửa hàng',
    merchantModalText: 'Để lại thông tin, Remeli sẽ liên hệ khi bắt đầu onboarding cửa hàng.',
    storeNameSimplePlaceholder: 'Tên cửa hàng',

    // Thêm ngôn ngữ cho Tên người đại diện
    representativeNameLabel: 'Tên người đại diện',
    representativeNamePlaceholder: 'Nhập họ và tên',

    // Thêm ngôn ngữ cho Địa chỉ cửa hàng
    storeAddressLabel: 'Địa chỉ cửa hàng',
    storeAddressPlaceholder: 'Số nhà, tên đường, quận/huyện...',

    businessTypeLabel: 'Loại hình',
    businessTypePlaceholder: 'Chọn loại hình',
    typeCafe: 'Quán cà phê',
    typeBakery: 'Tiệm bánh',
    typeFoodShop: 'Quán ăn',
    typeRestaurant: 'Nhà hàng',
    typeMiniMart: 'Siêu thị mini',
    phoneLabel: 'Số điện thoại',
    merchantSubmit: 'Gửi đăng ký',

    waitlistSuccess: 'Bạn đã có trong danh sách chờ của Remeli.',
    demoSuccess: 'Đã gửi thông tin. Remeli sẽ liên hệ sớm.',
    formSending: 'Đang gửi...',
    formError: 'Có lỗi xảy ra, vui lòng thử lại hoặc gửi email cho Remeli.',
    successWaitlistTitle: 'Cảm ơn bạn đã quan tâm Remeli',
    successWaitlistMessage: 'Remeli sẽ sớm liên hệ với bạn.',
    successMerchantTitle: 'Cảm ơn bạn đã đăng ký với Remeli',
    successMerchantMessage: 'Remeli sẽ sớm liên hệ với bạn.',
    successStoreTitle: 'Cảm ơn bạn đã giới thiệu cửa hàng',
    successStoreMessage: 'Remeli sẽ sớm xem xét và liên hệ với họ.',
    returnHome: 'Trở về trang chủ',

    feedback1Text: '"App siêu tiện lợi luôn! Mình hay canh giờ tối để đặt túi bánh ngọt từ tiệm gần nhà, bánh vẫn siêu ngon mà giá giảm được một nửa, vừa tiết kiệm vừa đỡ phí đồ ăn."',
    feedback1Role: 'Người dùng • TP. HCM',
    feedback2Text: '"Là sinh viên nên Remeli cứu rỗi ví tiền của mình rất nhiều. Thao tác đặt trước trên app rồi tự ghé tiệm lấy rất nhanh gọn, chủ quán lại nhiệt tình nữa."',
    feedback2Role: 'Sinh viên • Hà Nội',
    feedback3Text: '"Từ ngày đăng ký bán phần ăn cuối ngày trên Remeli, quán mình vừa giảm hẳn lượng đồ ăn thừa bỏ đi, lại vừa tiếp cận thêm được rất nhiều khách hàng mới trong khu vực."',
    feedback3Role: 'Đối tác • Quận 3'
  },
  en: {
    pageTitle: 'Remeli | Save Food · Save Money · Save Tomorrow',
    metaDescription: 'Remeli helps you find good food left at local stores in Vietnam, reserve it easily, and pick it up in store.',
    brandAria: 'Remeli home',
    menuOpen: 'Open menu',
    mainMenu: 'Main menu',
    languageLabel: 'Change language',
    scrollCue: 'Scroll to how it works',
    marqueeLabel: 'Scrolling food categories',
    socialLabel: 'Social media',
    closeModal: 'Close',

    navHome: 'Home',
    navHow: 'How it works',
    navMerchant: 'Business',
    navImpact: 'Impact',
    navCommunity: 'Community',
    navFaq: 'FAQ',
    joinEarly: 'Join early',
    waitlistButton: 'Join the waitlist',
    recommendStoreButton: 'Recommend a store',

    megaApp: 'App',
    megaDownloadApp: 'How to download App',
    megaHowToPickup: 'How to pick up',
    megaAboutUs: 'About us',
    megaAboutRemeli: 'About Remeli',
    megaOurTeam: 'Our team',
    megaCommunity: 'Community',
    megaImpact: 'Impact',
    megaCustomerFeedback: 'Customer feedback',

    heroTitle: '<span>Good food finds</span><span> Good people</span>',
    heroSubtitle: 'Save Food · Save Money · Save Tomorrow',

    marqueeBakery: 'Bakery',
    marqueeCafe: 'Cafe',
    marqueeMeal: 'Restaurant',
    marqueeBanhMi: 'Supermarket',
    marqueeEat: 'Eat better',
    marqueeSave: 'Save more',
    marqueeLessWaste: 'Waste less',

    howEyebrow: 'Simple & clear',
    howTitle: '<span>How Remeli</span><span>works</span>',
    howDescription: '<span>Three simple steps to eat better,</span><span>save more and waste less every day.</span>',
    stepOneTitle: 'Find food nearby',
    stepOneText: 'Discover nearby stores with good end-of-day food available.',
    stepTwoTitle: 'Reserve ahead',
    stepTwoText: 'Choose a bag or item, then check the price, quantity, and pickup time.',
    stepThreeTitle: 'Pick it up',
    stepThreeText: 'Visit the store during the selected pickup window and collect your food.',

    foodEyebrow: 'More than good food',
    foodTitle: '<span>What Remeli brings</span><span>to your day</span>',
    foodDescription: 'One small pickup can help you save more, discover nearby stores, and waste less.',
    impactSaveTitle: 'Save money',
    impactSaveText: 'Enjoy good food at a friendlier price every day.',
    impactEnvTitle: 'Protect the planet',
    impactEnvText: 'Help reduce food waste through every meals.',
    impactDiscoverTitle: 'Discover new food',
    impactDiscoverText: 'Chance to explore new food that you have forgotten.',
    impactLocalTitle: 'Support stores',
    impactLocalText: 'Help local businesses sell good food to customers.',
    bagSmall: 'Local store',

    whyEyebrow: 'Why Remeli?',
    whyTitle: 'Small choice, big impact',
    benefitSaveTitle: '25K+',
    benefitSaveText: 'Rescue orders',
    benefitLocalTitle: '8.4T',
    benefitLocalText: 'Ckg CO₂e prevented',
    benefitWasteTitle: '15.2T',
    benefitWasteText: 'kg food saved',

    merchantEyebrow: 'For store owners',
    merchantTitle: '<span>Sell out more easily</span><span>operate more lightly.</span>',
    merchantDescription: 'Remeli helps you sell good food left at the end of the day in a simple and efficient way.',
    merchantCta: 'Register your store',
    merchantPointOne: 'Create orders easily',
    merchantPointTwo: 'Set quantity, price, and pickup time',
    merchantPointThree: 'Customer reserve and pick up',
    merchantPointFour: 'Simple reports, easy tracking',

    communityEyebrow: 'Remeli community',
    communityTitle: 'Recommend the stores you love.',
    communityDescription: 'A great store sometimes just needs a better way to meet the right customers.',

    faqEyebrow: 'FAQ',
    faqTitle: 'Frequently asked questions',
    faq1Q: 'Is Remeli a food delivery app?',
    faq1A: 'No. Remeli focuses on helping users reserve a bag in the app and pick it up in store during a chosen time window. This model keeps operating costs low and fits our early stage in Vietnam.',
    faq2Q: 'Can I order on the website?',
    faq2A: 'No. The Remeli website is for introducing the service, sharing the app download link, and collecting info from users and partners. Browsing, reserving, paying, and confirming orders all happen inside the Remeli app.',
    faq3Q: "Do I know what's in the bag beforehand?",
    faq3A: 'It depends on the store. Some bags clearly describe the food category, while others are flexible "surprise" bags based on what is left that day. Remeli encourages partners to note the food type, portion, pickup window, and allergy warnings.',
    faq4Q: 'Is the food safe to eat?',
    faq4A: 'F&B partners are responsible for only listing food that is still good and suitable for consumption within the pickup window. Remeli requires partners to provide clear information and to cooperate on resolving any user feedback.',
    faq5Q: 'What if I arrive late?',
    faq5A: 'Each bag has a specific pickup window. If you arrive outside that window, the store may not be able to hold your order. Support conditions are shown in the app before you confirm.',
    faq6Q: 'How do I pay?',
    faq6A: 'Payment methods are shown in the app at the time you reserve a bag. Depending on the stage of operations, Remeli may support payment in store or a suitable digital payment method.',
    faq7Q: 'Can I request deletion of my personal data?',
    faq7A: 'Yes. You can send a request regarding your personal data through the contact form or by emailing privacy@remeli.vn. Remeli will process it according to our privacy policy and applicable law.',
    faq8Q: 'Is there a fee for stores to join Remeli?',
    faq8A: 'Fee details and the partnership model are discussed directly when a store registers for consultation. Remeli needs to understand the business type, area, scale, and operating process before proposing a suitable plan.',
    faq9Q: 'Is Remeli suitable for small shops?',
    faq9A: 'Yes. Remeli is designed so small eateries, bakeries, cafes, and local stores can all list their remaining good food with a simple process.',
    faq10Q: 'Where can I reach out for media or community partnerships?',
    faq10A: 'You can send details through the contact form and choose the <strong>Media/Community</strong> topic, or email <a href="mailto:remeli.vn@gmail.com">remeli.vn@gmail.com</a>.',

    footerSlogan: 'Good food finds Good people<br />Save Food · Save Money · Save Tomorrow',
    footerExplore: 'Explore',
    footerLegal: 'Legal',
    footerContact: 'Contact',
    terms: 'Terms of use',
    privacy: 'Privacy policy',
    refund: 'Refund policy',
    location: 'Ho Chi Minh City, Vietnam',

    waitlistEyebrow: 'Join the waitlist',
    waitlistModalTitle: 'Get the earliest updates from Remeli',
    waitlistModalText: 'Leave your details and Remeli will notify you when we launch in your city.',
    emailLabel: 'Your email',
    emailShortLabel: 'Email',
    emailPlaceholder: 'name@gmail.com',
    phonePlaceholder: '09xxxxxxxx',
    cityLabel: 'City',
    cityPlaceholder: 'Choose your city',
    cityHanoi: 'Hanoi',
    cityDanang: 'Da Nang',
    cityCantho: 'Can Tho',
    cityOther: 'Other',
    roleLabel: 'You are',
    rolePlaceholder: 'Selection',
    roleUser: 'Customer',
    roleMerchant: 'Store owner',
    roleOther: 'Other',

    // Nav & Footer
    megaForBusiness: 'For Business',
    megaWhyJoin: 'Why join Remeli',
    megaRegisterBusiness: 'Register business',
    footerMerchantSection: 'Business',
    footerWhyJoin: 'Why join Remeli',
    footerRegisterBusiness: 'Register business',

    // Vì sao gia nhập
    whyHeroEyebrow: 'For Partners',
    whyHeroTitle: 'Grow your business,<br/><span style="color: var(--yellow);">Reduce waste</span>',
    whyHeroDesc: 'Join Remeli to turn end-of-day surplus food<br/>into new revenue and attract potential customers.',
    whyHeroBtn: 'Register as a partner',
    whyBenefitEyebrow: 'Practical Benefits',
    whyBenefitTitle: 'Why join Remeli?',
    whyBen1Title: 'Reduce waste',
    whyBen1Desc: 'No more pain of throwing away good food. Remeli helps you optimize 100% of your daily ingredients.',
    whyBen2Title: 'Extra revenue',
    whyBen2Desc: 'Turn surplus food into cash. Forgotten products will now easily generate extra revenue for your store.',
    whyBen3Title: 'Potential customers',
    whyBen3Desc: 'Reach thousands of young, eco-conscious users. They pick up food and can easily become loyal customers.',
    whyOpEyebrow: 'Simple Operation',
    whyOpTitle: 'Just 3 steps a day',
    whyStep1Title: 'Pack & Update',
    whyStep1Desc: 'At the end of your shift, simply snap a photo of surplus food (or create a Surprise Bag) and update the quantity on the app in 5 seconds.',
    whyStep2Title: 'Order via App',
    whyStep2Desc: 'Nearby users get notified, reserve, and pay directly on the Remeli app.',
    whyStep3Title: 'Hand over',
    whyStep3Desc: 'Customers visit during the pickup window. Just scan the QR code and hand over the bag. Money goes straight to your wallet!',
    whyMetric1: 'Initial setup fee',
    whyMetric2: 'Estimated revenue increase',
    whyMetric3Value: 'Support',
    whyMetric3: 'Exclusive marketing 0đ',
    whyCtaTitle: 'Start your zero-waste journey<br/>with Remeli',
    whyCtaDesc: 'Join for free. Thousands of customers are waiting to "rescue" your good food every day.',
    whyCtaBtn: 'Register store now',

    // Đăng ký doanh nghiệp
    regHeroEyebrow: 'Register Business',
    regHeroTitle: 'Become a partner<br/><span style="color: var(--yellow);">with Remeli</span>',
    regHeroDesc: 'Leave your information, we will help you turn end-of-day food into new revenue today.',
    regFormTitle: 'Register Store',
    regFormDesc: 'Leave your details, Remeli team will contact you to set up your store within 24 hours. 100% free!',
    regFormName: 'Store Name *',
    regFormNamePlace: 'e.g., Cafe, Restaurant, Bakery...',
    regFormPhone: 'Phone Number *',
    regFormPhonePlace: 'Enter contact phone number...',
    regFormArea: 'Area (City/District) *',
    regFormAreaPlace: 'e.g., District 1, HCMC...',
    regFormSubmit: 'Submit Registration',

    // App Instructions
    appDownloadApp: 'Download app',
    appGetStarted: 'Get started with',
    appRemeli: 'Remeli',

    appEasyDaily: 'Easy to use every day',
    appEasyDesc: 'With just a few basic steps on the app, you can enjoy delicious food at great prices.',
    appStep1: 'Step 01',
    appFindSelect: 'Find & Select',
    appFood: 'your food',
    appStep1Desc2: 'Open the app, discover nearby stores, and choose your favorite food at a discounted price.',
    appStep2: 'Step 02',
    appReserve: 'Reserve &',
    appPay: 'Pay',
    appStep2Desc2: 'Pay and reserve in advance through the app to ensure your meal is always ready.',
    appStep3: 'Step 03',
    appArrive: 'Arrive',
    appPickup: '(Pick up)',
    appStep3Desc2: 'Go directly to the store during the designated time window to pick up your hot food easily.',
    appImg1: '[Illustration 1]',
    appImg2: '[Illustration 2]',
    appImg3: '[Illustration 3]',
    appHeroDesc: 'Discover delicious surplus food from nearby restaurants.<br />Download the app on the App Store or Google Play today!',
    appSmooth: 'Smooth experience',
    appJustOneMin: 'Just 1 minute',
    appToStart: 'to get started',
    appNoComplex: 'No complex account creation. Sign in with Apple, Google, or phone number in seconds.',
    appStep1Title: 'Download the app',
    appStep1Desc: 'Find Remeli on the App Store or Google Play and install it for free.',
    appStep2Title: 'Quick login',
    appStep2Desc: 'Use your Google, Apple account or phone number to sign in instantly.',
    appStep3Title: 'Discover',
    appStep3Desc: 'Turn on location to find stores with great food around you.',

    // How to pick up
    pickupPageTitleDoc: 'Remeli | How to pick up',
    pickupImageAlt: '[Pickup Illustration]',
    pickupPageTitle: 'Pickup Experience',
    pickupHeroTitle1: 'Guide to',
    pickupHeroTitle2: 'Pick up',
    pickupHeroDesc: 'Follow these 4 simple steps to collect your perfect meal at the store.',
    pickupStep1: 'Order & Pay',
    pickupStep1Desc: 'Select your favorite meal and securely checkout right in the app.',
    pickupStep2: 'View Address & Instructions',
    pickupStep2Desc: 'The system will show detailed address and direct pickup instructions from the store.',
    pickupStep3: 'Open QR Code on App',
    pickupStep3Desc: 'When you arrive at the store, simply open the app and have your order confirmation QR code ready.',
    pickupStep4: 'Scan QR & Collect',
    pickupStep4Desc: 'Show the QR code to the store staff to scan for confirmation and take your delicious meal home.',
    
    // Impact Page

    // Pickup Guide
    pickupGuide: 'Pickup Guide',
    pickupHowTo: 'How to',
    pickupReceive: 'pick up?',
    pickupDesc: 'Simple, fast, and friendly. Here are the steps to collect your order.',
    pickupProcess: 'Pickup process',
    pickup3Steps: '3 steps',
    pickupAtStore: 'at the store',
    pickupStep1Title: 'Arrive on time',
    pickupStep1Desc: 'Go to the store within the pickup window shown in the app.',
    pickupStep2Title: 'Show code to staff',
    pickupStep2Desc: 'Open the app, show the QR code or order code to the staff.',
    pickupStep3Title: 'Collect food',
    pickupStep3Desc: 'Enjoy delicious food and be proud that you helped reduce food waste!',

    // About Remeli
    aboutUs: 'About Us',
    aboutStory: 'The Story of',
    aboutRemeli: 'Remeli',
    aboutHeroDesc: 'A journey connecting delicious meals with the mission of reducing waste and protecting Vietnam\'s environment.',
    aboutIdea: 'The Founding Idea',
    aboutSaveFood: 'Save food, protect the Earth',
    aboutVisionDesc: 'In Vietnam, tons of perfectly good food are wasted every day because they don\'t reach consumers in time. Remeli was founded with a simple goal: to create a platform connecting food stores with food lovers, helping <strong>save delicious meals</strong>, save money, and most importantly <strong>reduce greenhouse gas emissions</strong> from food waste.',
    aboutWhyRemeli: 'Why was Remeli',
    aboutBorn: 'created?',
    aboutProtectEnv: 'Protect the Environment',
    aboutProtectEnvDesc: 'Every meal saved from the bin means reducing methane emissions. Together, we are making the air in Vietnam greener.',
    aboutFightWaste: 'Fight Food Waste',
    aboutFightWasteDesc: 'We believe good food is meant to be eaten. Remeli helps restaurants optimize ingredients and respect the chefs\' efforts.',
    aboutSaveConnect: 'Save & Connect',
    aboutSaveConnectDesc: 'Users enjoy good food at affordable prices, stores earn extra income, and the community unites for a meaningful goal.',

    // Our Team
    teamEyebrow: 'Remeli Team',
    teamPeople: 'The people',
    teamBehind: 'behind Remeli',
    teamDesc: 'A group of young people passionate about technology, food, and the environment, working together for a greener Vietnam.',
    teamVision: 'Shared Vision',
    teamNotJustApp: 'We are not just',
    teamMakingApp: 'building an app',
    teamVisionDesc: 'We are building a community of people who care about their meals and the environment. Our goal is to make "rescuing" food a daily habit for everyone.',
    teamVietnamese: 'Vietnamese',
    teamCreate: 'Creators',
    teamVietnameseDesc: 'We are young, passionate Vietnamese individuals sharing a desire to solve the food waste problem in our hometown.',
    teamFounders: 'The Founders',
    teamOurGroup: 'Our team',
    teamEyebrow2: 'The Team',
    teamOps: 'Head of Operations',
    teamTech: 'Chief Technology Officer',
    teamMkt: 'Chief Marketing Officer',

    // Impact
    impactOfRemeli: 'Impact of Remeli',
    impactSmallChoice: 'Small choice',
    impactBigChange: 'Big impact',
    impactHeroDesc: 'Your small action creates a huge impact, contributing to protecting our green planet.',
    impactMetric1: '25K+',
    impactMealsSaved: 'Meals saved',
    impactMealsSavedDesc: 'Tens of thousands of delicious meals reached users in time instead of ending up in landfills.',
    impactMetric2: '8.4T',
    impactCO2: 'CO₂e prevented',
    impactCO2Desc: 'A massive amount of greenhouse gas (CO₂e) has been prevented by reducing waste.',
    impactMetric3: '15.2T',
    impactKgSaved: 'kg of food saved',
    impactKgSavedDesc: '15.2 Tons (or 15,200 kg) of fresh ingredients have not been wasted.',
    impactVision: 'Sustainable Vision',
    impactEveryMeal: 'Every meal saved',
    impactStepForEarth: 'is a step for the Earth',
    impactVisionDesc: 'Food waste is not only an economic issue but a massive burden on the environment. When food is thrown away, all the energy and water used to grow, harvest, transport, and package it is also lost. By joining Remeli, you are part of a circular food supply chain where value is respected, and pressure on the Earth is reduced.',
    impactEnvTitle: 'Environmental Impact',
    impactReduce: 'Reduce',
    impactGreenhouse: 'Greenhouse Gases',
    impactEnvDesc: 'Food in landfills generates methane, a greenhouse gas 25 times more potent than CO₂. By rescuing food, we directly prevent global warming and protect clean air for future generations.',
    impactEconTitle: 'Economic Impact',
    impactOptimize: 'Optimize',
    impactResources: 'Resources',
    impactEconDesc: 'All ingredients, labor, and energy used to produce a meal are valuable. Remeli helps businesses recover production costs while providing users with quality meals at very reasonable prices.',
    impactSocialTitle: 'Social Impact',
    impactConnect: 'Connect',
    impactCommunity: 'Community',
    impactSocialDesc: 'Beyond buying and selling, Remeli is building a community of conscious consumers. We connect with each other and local stores through a positive message: Live green, consume smart, and value food.',
    impactBePart: 'Be part of',
    impactOfSolution: 'the solution',
    impactCtaDesc: 'Download Remeli today to start your journey of saving food and protecting the environment with tens of thousands of other Vietnamese.',
    impactCtaBtn: 'Download App Now',

    // Feedback
    fbCommunity: 'Remeli Community',
    fbVoice: 'Voice from',
    fbComm: 'the Community',
    fbUsers: 'Users',
    fbDesc: 'Discover the most authentic experiences from thousands of customers and partners who have joined Remeli on the journey against food waste.',
    fbRealExp: 'Real Experiences',
    fbTitle1: 'Great food, great price!',
    fbText1: '"Super convenient app! I often order surprise bags from my favorite bakery at night. Good food, saves money, and feels like opening a surprise gift!"',
    fbRole1: 'User • HCMC',
    fbTitle2: 'End-of-month lifesaver',
    fbText2: '"As a student, Remeli really saves my wallet. The food is still hot and high quality. I hope more stores near my university join the app."',
    fbRole2: 'Student • Hanoi',
    fbTitle3: 'Anti-waste solution',
    fbText3: '"Since selling surplus food on Remeli, our restaurant no longer throws away food. Revenue went up slightly, but the best part is not wasting our cooking efforts."',
    fbRole3: 'Partner • District 3',
    fbTitle4: 'Small act, big meaning',
    fbText4: '"It feels great to help protect the environment every day just by eating good food. The app design is also very cute and easy to use!"',
    fbRole4: 'User • Da Nang',
    fbTitle5: 'Convenient and smooth',
    fbText5: '"The pickup feature works extremely well. I stop by the store after work, show the code, and get the food immediately without any waiting."',
    fbRole5: 'Office Worker • HCMC',
    fbTitle6: 'Joy of a baker',
    fbText6: '"No more headaches about unsold cakes every night. I am very grateful to the Remeli team for creating such a meaningful platform for society."',
    fbRole6: 'Bakery Owner • Hanoi',

    storeModalTitle: 'Recommend a store',
    storeModalText: 'Know a store that should be on Remeli? Send us the details so our team can learn more.',
    storeNameLabel: 'Store name',
    storeNamePlaceholder: 'Example: May Bakery',
    storeAddressLabel: 'Area / address',
    storeAddressPlaceholder: 'Example: District 3, Ho Chi Minh City',
    foodTypeLabel: 'Food type',
    foodTypePlaceholder: 'Bakery, cafe, restaurants...',
    sendRecommendation: 'Send recommendation',

    merchantModalTitle: 'Register your store',
    merchantModalText: 'Leave your details and Remeli will contact you when store onboarding begins.',
    storeNameSimplePlaceholder: 'Store name',
    representativeNameLabel: 'Representative name',
    representativeNamePlaceholder: 'Enter full name',
    businessTypeLabel: 'Business type',
    businessTypePlaceholder: 'Choose business type',
    typeCafe: 'Cafe',
    typeBakery: 'Bakery',
    typeFoodShop: 'Food shop',
    typeRestaurant: 'Restaurant',
    typeMiniMart: 'Mini mart',
    phoneLabel: 'Phone number',
    merchantSubmit: 'Submit registration',

    waitlistSuccess: 'You are now on Remeli’s waitlist.',
    demoSuccess: 'Submitted. Remeli will contact you soon.',
    formSending: 'Sending...',
    formError: 'Something went wrong. Please try again or email Remeli directly.',
    successWaitlistTitle: 'Thank you for your interest in Remeli',
    successWaitlistMessage: 'Remeli will contact you soon.',
    successMerchantTitle: 'Thank you for registering with Remeli',
    successMerchantMessage: 'Remeli will contact you soon.',
    successStoreTitle: 'Thank you for your recommendation',
    successStoreMessage: 'Remeli will review and contact them soon.',
    returnHome: 'Return to home',

    feedback1Text: '"Super convenient app! I often order pastry bags from a nearby bakery in the evening. The cakes are still delicious at half price, which saves money and reduces food waste."',
    feedback1Role: 'User • HCMC',
    feedback2Text: '"As a student, Remeli saves my wallet a lot. Reserving ahead on the app and picking up at the store is very quick, and the store owners are so enthusiastic."',
    feedback2Role: 'Student • Hanoi',
    feedback3Text: '"Since registering to sell end-of-day food on Remeli, our shop has significantly reduced food waste and reached many new customers in the area."',
    feedback3Role: 'Partner • District 3'
  }
};

let currentLang = localStorage.getItem('remeli-lang') || 'vi';

function t(key) {
  return translations[currentLang][key] || translations.vi[key] || key;
}

function applyLanguage(lang) {
  currentLang = translations[lang] ? lang : 'vi';
  localStorage.setItem('remeli-lang', currentLang);
  document.documentElement.lang = currentLang;
  document.title = t('pageTitle');
  if (metaDescription) metaDescription.setAttribute('content', t('metaDescription'));

  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.dataset.i18n;
    element.innerHTML = t(key);
  });

  document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
    const key = element.dataset.i18nPlaceholder;
    element.setAttribute('placeholder', t(key));
  });

  document.querySelectorAll('[data-i18n-aria-label]').forEach(element => {
    const key = element.dataset.i18nAriaLabel;
    element.setAttribute('aria-label', t(key));
  });

  languageButtons.forEach(button => {
    const isActive = button.dataset.langSwitch === currentLang;
    button.classList.toggle('active', isActive);
    button.setAttribute('aria-pressed', String(isActive));
  });

  const waitlistMessage = document.getElementById('waitlistMessage');
  if (waitlistMessage) waitlistMessage.textContent = '';
  document.querySelectorAll('.form-message').forEach(message => {
    if (message.id !== 'waitlistMessage') message.textContent = '';
  });
}

function updateHeader() {
  header.classList.toggle('scrolled', window.scrollY > 20);
}

function updateActiveNav() {
  if (document.body.classList.contains('faq-page')) {
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      link.classList.toggle('active', href === 'faq.html');
    });
    return;
  }

  const sections = [...document.querySelectorAll('main section[id]')];
  const current = sections
    .filter(section => section.getBoundingClientRect().top <= 130)
    .pop();

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    link.classList.toggle('active', current && href === `#${current.id}`);
  });
}

function updateHeroParallax() {
  const y = window.scrollY;
  parallaxTargets.forEach((target, index) => {
    const speed = (index % 2 === 0 ? 0.035 : -0.025);
    target.style.translate = `0 ${y * speed}px`;
  });
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function updateFoodFlight() {
  if (!foodCloud) return;

  const rect = foodCloud.getBoundingClientRect();
  const viewport = window.innerHeight;
  const progress = clamp((viewport * 0.74 - rect.top) / (viewport * 0.74), 0, 1);
  const eased = 1 - Math.pow(1 - progress, 3);

  foodItems.forEach((item, index) => {
    const x = Number(item.dataset.x || 0);
    const y = Number(item.dataset.y || 0);
    const r = Number(item.dataset.r || 0);
    const delay = index * 0.035;
    const local = clamp((eased - delay) / (1 - delay), 0, 1);
    const scale = 0.28 + local * 0.72;
    const opacity = clamp(local * 1.25, 0, 1);

    item.style.opacity = opacity;
    item.style.transform = `translate(calc(-50% + ${x * local}px), calc(-50% + ${y * local}px)) rotate(${r * local}deg) scale(${scale})`;
  });
}

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.16 });

revealItems.forEach(item => revealObserver.observe(item));

menuToggle?.addEventListener('click', () => {
  const isOpen = header.classList.toggle('menu-open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
});

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    header.classList.remove('menu-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  });
});

languageButtons.forEach(button => {
  button.addEventListener('click', () => {
    applyLanguage(button.dataset.langSwitch);
    header.classList.remove('menu-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  });
});

function openModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return;
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  const firstInput = modal.querySelector('input, select, textarea');
  firstInput?.focus();
}

function closeModal(modal) {
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

document.querySelectorAll('[data-open-modal]').forEach(button => {
  button.addEventListener('click', (event) => {
    event.preventDefault();
    header.classList.remove('menu-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
    openModal(button.dataset.openModal);
  });
});

document.querySelectorAll('[data-close-modal]').forEach(item => {
  item.addEventListener('click', () => closeModal(item.closest('.modal')));
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    document.querySelectorAll('.modal.open').forEach(closeModal);
  }
});

// Cấu hình lưu về hệ thống Google Sheet Web App của bạn
const GOOGLE_SCRIPT_ENDPOINT = "https://script.google.com/macros/s/AKfycbz02_CwynBXLxD4ofVWuuCcy0Z5YHeLYgymd5x6QaJ5G5QAr4hnDKX-C0Sxp8bsQAZKMg/exec";

function setupGoogleSheetForm(form, titleKey, messageKey) {
  if (!form) return;

  const messageEl = form.querySelector(".form-message");
  const submitBtn = form.querySelector('button[type="submit"]');

  form.addEventListener("submit", () => {
    form.setAttribute("action", GOOGLE_SCRIPT_ENDPOINT);
    form.setAttribute("target", "hidden_iframe");

    if (submitBtn) submitBtn.disabled = true;
    if (messageEl) messageEl.textContent = t("formSending");

    setTimeout(() => {
      form.reset();
      if (submitBtn) submitBtn.disabled = false;
      if (messageEl) messageEl.textContent = "";
      const currentModal = form.closest(".modal");
      if (currentModal) closeModal(currentModal);
      
      const successTitleEl = document.getElementById("successModalTitle");
      const successMessageEl = document.querySelector("#successModal p");
      if (successTitleEl && successMessageEl) {
        successTitleEl.dataset.i18n = titleKey;
        successTitleEl.innerHTML = t(titleKey);
        successMessageEl.dataset.i18n = messageKey;
        successMessageEl.innerHTML = t(messageKey);
      }
      
      openModal("successModal");
    }, 2000);
  });
}

// Kích hoạt nộp dữ liệu tự động cho cả 3 form 
setupGoogleSheetForm(document.getElementById("waitlistForm"), "successWaitlistTitle", "successWaitlistMessage");

const storeForm = document.querySelector('input[value="store"]')?.closest('form');
if (storeForm) setupGoogleSheetForm(storeForm, "successStoreTitle", "successStoreMessage");

const merchantForm = document.querySelector('input[value="merchant"]')?.closest('form');
if (merchantForm) setupGoogleSheetForm(merchantForm, "successMerchantTitle", "successMerchantMessage");

const merchantPageForm = document.getElementById("merchantPageForm");
if (merchantPageForm) setupGoogleSheetForm(merchantPageForm, "successMerchantTitle", "successMerchantMessage");

let ticking = false;
function onScroll() {
  if (ticking) return;
  window.requestAnimationFrame(() => {
    updateHeader();
    updateActiveNav();
    updateHeroParallax();
    updateFoodFlight();
    ticking = false;
  });
  ticking = true;
}

window.addEventListener('scroll', onScroll, { passive: true });
window.addEventListener('resize', updateFoodFlight);

applyLanguage(currentLang);
updateHeader();
updateActiveNav();
updateHeroParallax();
updateFoodFlight();