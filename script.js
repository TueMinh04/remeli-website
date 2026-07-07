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
    navMerchant: 'Cửa hàng',
    navImpact: 'Tác động',
    navCommunity: 'Cộng đồng',
    navFaq: 'FAQ',
    joinEarly: 'Tham gia sớm',
    waitlistButton: 'Tham gia danh sách chờ',
    recommendStoreButton: 'Giới thiệu cửa hàng',

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

    footerSlogan: 'Món ngon còn đây, tiết kiệm trong tay.<br />Save Food. Save Money. Save Tomorrow.',
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
    emailPlaceholder: 'you@email.com',
    cityLabel: 'Thành phố',
    cityPlaceholder: 'Chọn thành phố',
    cityHanoi: 'Hà Nội',
    cityDanang: 'Đà Nẵng',
    cityCantho: 'Cần Thơ',
    cityOther: 'Khác',
    roleLabel: 'Bạn là?',
    rolePlaceholder: 'Bạn là?',
    roleUser: 'Người dùng',
    roleMerchant: 'Chủ cửa hàng',
    roleOther: 'Khác',

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
    formError: 'Có lỗi xảy ra, vui lòng thử lại hoặc gửi email cho Remeli.'
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
    navMerchant: 'For stores',
    navImpact: 'Impact',
    navCommunity: 'Community',
    navFaq: 'FAQ',
    joinEarly: 'Join early',
    waitlistButton: 'Join the waitlist',
    recommendStoreButton: 'Recommend a store',

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
    merchantPointOne: 'Create end-of-day bags quickly',
    merchantPointTwo: 'Set quantity, price, and pickup time',
    merchantPointThree: 'Customers reserve and pick up',
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
    emailPlaceholder: 'you@email.com',
    cityLabel: 'City',
    cityPlaceholder: 'Choose your city',
    cityHanoi: 'Hanoi',
    cityDanang: 'Da Nang',
    cityCantho: 'Can Tho',
    cityOther: 'Other',
    roleLabel: 'You are',
    rolePlaceholder: 'You are',
    roleUser: 'Customer',
    roleMerchant: 'Store owner',
    roleOther: 'Other',

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
    formError: 'Something went wrong. Please try again or email Remeli directly.'
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

function setupGoogleSheetForm(form, successKey) {
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
      if (messageEl) messageEl.textContent = t(successKey);
    }, 2000);
  });
}

// Kích hoạt nộp dữ liệu tự động cho cả 3 form 
setupGoogleSheetForm(document.getElementById("waitlistForm"), "waitlistSuccess");

const storeForm = document.querySelector('input[value="store"]')?.closest('form');
if (storeForm) setupGoogleSheetForm(storeForm, "demoSuccess");

const merchantForm = document.querySelector('input[value="merchant"]')?.closest('form');
if (merchantForm) setupGoogleSheetForm(merchantForm, "demoSuccess");

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