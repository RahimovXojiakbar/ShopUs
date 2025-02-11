from django.db import models
from shortuuid.django_fields import ShortUUIDField

class MyShortUuid(models.Model):
    uuid = ShortUUIDField(
        primary_key=True,
        editable=False,
        max_length=12,
        alphabet = 'abcdefghijklmnopqrstuvwxz123456789',
    )
    
    class Meta:
        abstract  = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BaseModel(MyShortUuid):
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BigCategories(models.TextChoices):
    ELEKTRONIKA = "Elektronika"
    MAISHIY_TEXNIKA = "Maishiy texnika"
    MATO = "Mato"
    POYABZAL = "Poyabzal"
    AKSESUAR = "Aksesuar"
    GOZALLIK_VA_PARVARISH = "Go'zallik va parvarish"
    SALOMATLIK = "Salomatlik"
    UY_ROZGOR_BUYUMLARI = "Uy ro'zg'or buyumlari"
    QURILISH_VA_TAMIRLASH = "Qurilish va tamirlash"
    BOLALAR_TOVARLARI = "Bolalar tavarlari"
    OZIQ_OVQAT = "Oziq ovqat"
    MAISHIY_KIMYOVIY_MODDALAR = 'Maishiy kimyoviy moddalar'
    SPORT_VA_DAM_OLISH = "Sport va dam olish"
    KANTSELYARIYA = "Kantselyariya"
    UY_HAYVONLARI_UCHUN = "Uy hayvonlari uchun mahsulotlar"
    YOZGI_UY_BOG_VA_SABZAVOT_BOGI = "Yozgi uy, Bog' va sabzavot bog'i"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class SmallCategories(models.TextChoices):
    SMARTFONLAR_VA_TELEFONLAR = "Smartfonlar va telefonlar"
    KOMPYUTER_USKUNALARI = "Kompyuter uskunalari"
    SOATLAR_VA_ELEKTRON_BUDILNIKLAR = "Soatlar va elektron budilniklar"
    KVADROKOPTERLAR_VA_AKSESUARLAR = "Kvadrokopterlar va aksessuarlar"
    OPTIK_ASBOBLAR = "Optik asboblar"
    ELEKTRONIKA_UCHUN_AKSESUARLAR = "Elektronika uchun aksessuarlar"
    NAVIGATORLAR = "Navigatorlar"
    AQLI_UY_VA_XAVFSIZLIK = "Aqlli uy va xavfsizlik"
    NAUSHNIKLAR_VA_AUDIO_USKUNALAR = "Naushniklar va audio uskunalar"
    AQLI_SOATLAR_VA_FITNES_BILAKUZUKLAR = "Aqlli soatlar va fitnes bilakuzuklar"
    NOUTBUKLAR_PLANSHETLAR_VA_ELEKTRON_KITOBLAR = "Noutbuklar, planshetlar va elektron kitoblar"
    FOTO_VA_VIDEO_USKUNALAR = "Foto va video uskunalar"
    TELEVIZORLAR_VA_VIDEO_USKUNALAR = "Televizorlar va video uskunalar"
    GEYMETLAR_UCHUN_MAHSULOTLAR = "Geymetlar uchun mahsulotlar"
    GOZALLIK_USKUNALARI = "Go'zallik uskunalari"
    IQLIMNI_NAZORAT_QILISH_USKUNALARI = "Iqlimni nazorat qilish uskunalari"
    MAISHIY_TEXNIKA = "Maishiy texnika"
    KATTA_MAISHIY_TEXNIKA = "Katta maishiy texnika"
    OSHXONA_JIHOZLARI = "Oshxona jihozlari"
    AYOLLAR_KIYIMI = "Ayollar kiyimi"
    ERKAKLAR_KIYIMI = "Erkaklar kiyimi"
    QIZLAR_UCHUN_KIYIMLAR = "Qizlar uchun kiyimlar"
    OGIL_BOLALAR_UCHUN_KIYIMLAR = "O'g'il bolalar uchun kiyimlar"
    YANGI_TUGILGAN_CHAQALOQLAR_UCHUN_KIYIMLAR = "Yangi tug'ilgan chaqaloqlar uchun kiyimlar"
    AYOLLAR_POYABZALI = "Ayollar poyabzali"
    ERKAKLAR_POYABZALI = "Erkaklar poyabzali"
    QIZLAR_UCHUN_POYABZAL = "Qizlar uchun poyabzal"
    OGIL_BOLALAR_UCHUN_POYABZAL = "O'g'il bolalar uchun poyabzal"
    POYAFZAL_AKSESUARLARI = "Poyafzal aksessuarlari"
    AYOLLAR_UCHUN_AKSESUARLAR = "Ayollar uchun aksessuarlar"
    ERKAKLAR_UCHUN_AKSESUARLAR = "Erkaklar uchun aksessuarlar"
    QIZLAR_UCHUN_AKSESUARLAR = "Qizlar uchun aksessuarlar"
    OGIL_BOLALAR_UCHUN_AKSESUARLAR = "O'g'il bolalar uchun aksessuarlar"
    SAYOHAT_AKSESUARLARI = "Sayohat aksessuarlari"
    CHANGI_AKSESUARLARI = "Chang'i aksessuarlari"
    DINIY_AKSESUARLAR = "Diniy aksessuarlar"
    GRIM_SURMOQ_PARDOZ_QILMOQ = "Grim surmoq, pardoz qilmoq; yasamoq, tuzmoq"
    YUZNI_PARVARISH_QILISH = "Yuzni parvarish qilish"
    SOCHNI_PARVARISH_QILISH = "Sochni parvarish qilish"
    TANA_PARVARISHI = "Tana parvarishi"
    MANIKYUR_VA_PEDIKYUR = "Manikyur va pedikyur"
    ERKAKLAR_UCHUN = "Erkaklar uchun"
    PARFYUMERIYA = "Parfyumeriya"
    TATUIROVKA_SALONI_UCHUN_USKUNALAR_VA_MATERIALLAR = "Tatuirovka saloni uchun uskunalar va materiallar"
    DERMAKOSMETIKA = "Dermakosmetika"
    KOREYA_KOSMETIKASI = "Koreya kosmetikasi"
    SHAXSIY_GIGIENA = "Shaxsiy gigiena"
    PROFESSIONAL_KOSMETIKA = "Professional kosmetika"
    VITAMINLAR_VA_XUN_TAKVIYELERI = "Vitaminlar va xun takviyeleri"
    INTIM_KOSMETIKA = "Intim kosmetika"
    MASSAJ_VA_MASSAJ_USKUNALARI = "Massaj va massaj uskunalari"
    TIBBIY_MAHSULOTLAR_VA_SARF_MATERIALLARI = "Tibbiy mahsulotlar va sarf materiallari"
    TIBBIY_ASBOBLAR = "Tibbiy asboblar"
    OPTIKA = "Optika"
    ORTOPEDIK_MAHSULOTLAR = "Ortopedik mahsulotlar"
    PREZERVATIVLAR_VA_MOYLASH_MATERIALLARI = "Prezervativlar va moylash materiallari"
    SPORT_OVQATLANISHI = "Sport ovqatlanishi"
    REABILITATSIYA_MAHSULOTLARI = "Reabilitatsiya mahsulotlari"
    OSHXONA_BUYUMLARI = "Oshxona buyumlari"
    TOQIMACHILIK = "To'qimachilik"
    UY_ROZGOR_BUYUMLARI = "Uy-ro'zg'or buyumlari"
    NARSALARNI_SAQLASH = "Narsalarni saqlash"
    DEKOR_VA_INTERYER = "Dekor va interyer"
    UY_OSIMLIKLARI_MAHSULOTLARI = "Uy o'simliklari mahsulotlari"
    HAMMOM_VA_SAUNA_MAHSULOTLARI = "Hammom va sauna mahsulotlari"
    BAYRAM_MAHSULOTLARI = "Bayram mahsulotlari"
    MEBEL = "Mebel"
    QOL_ASBOBLARI_VA_JIHOZLARI = "Qo'l asboblari va jihozlari"
    SANTEXNIKA = "Santexnika"
    QURILISH_USKUNALARI = "Qurilish uskunalari"
    ELEKTR = "Elektr"
    YORITISH = "Yoritish"
    VENTILYATSIYA = "Ventilyatsiya"
    SARF_MATERIALLARI_VA_USKUNALAR = "Sarf materiallari va uskunalar"
    TUGATISH_MATERIALLARI = "Tugatish materiallari"
    UY_VA_BOG_UCHUN_SUV_TAMINOTI = "Uy va bog' uchun suv ta'minoti"
    ASBOBLAR = "Asboblar"
    MAHKAMLAGICHLAR_VA_ARMATURA = "Mahkamlagichlar va armatura"
    ISITISH = "Isitish"
    GIGIENA_VA_TAGLIKLAR = "Gigiena va tagliklar"
    BOLALAR_XONASI = "Bolalar xonasi"
    BOLALAR_SPORTI_VA_FAOL_DAM_OLISH = "Bolalar sporti va faol dam olish"
    BOLALAR_OVQATI = "Bolalar ovqati"
    BOLALAR_IJODIYATI = "Bolalar ijodiyoti"
    OYINCHOQLAR_VA_OYINLAR = "O'yinchoqlar va o'yinlar"
    ARAVACHALAR_VA_AVTOMOBIL_ORINDIQLARI = "Aravachalar va avtomobil o'rindiqlari"
    OZIQLANTIRISH_MAHSULOTLARI = "Oziqlantirish mahsulotlari"
    ONALAR_UCHUN_MAHSULOTLAR = "Onalar uchun mahsulotlar"
    FAOL_DAM_OLISH = "Faol dam olish"
    VELOSPORT = "Velosport"
    SPORT = "Sport"
    OZIQ_OVQAT = "Oziq ovqat"
    SUZ_SPORTI_VA_SUVDA_DAM_OLISH = "Suv sporti va suvda dam olish"
    QISHKI_SPORT_TURLARI = "Qishki sport turlari"
    OCHIQ_HAVODA_DAM_OLISH_BALIQ_OVLASH_VA_OV_QILISH = "Ochiq havoda dam olish, baliq ovlash va ov qilish"
    ROLITLI_KONKILAR_USKUNALAR_VA_EHTIYOT_QISMLAR = "Rolikli konkilar, uskunalar va ehtiyot qismlar"
    SKUTERLAR_VA_AKSESSUARLAR = "Skuterlar va aksessuarlar"
    ERKIN_VAZNLAR = "Erkin vaznlar"
    SKEYTBORDING = "Skeytbording"
    MASHQ_QILISH_MASHINALARI = "Mashq qilish mashinalari"
    FITNES_VA_YOGA = "Fitnes va yoga"
    ELEKTR_TRANSPORTI = "Elektr transporti"
    YOG_LAR_SOSLAR_VA_ZIRAVORLAR = "Yog'lar, soslar va ziravorlar"
    CHOY_QAHVA_VA_KAKAO = "Choy, qahva va kakao"
    SUV_SHARBATLAR_ICHIMLIKLAR = "Suv, sharbatlar, ichimliklar"
    PISHIRILGAN_MAHSULOTLAR_VA_SHIRINLIKlar = "Pishirilgan mahsulotlar va shirinliklar"
    ASAL_MURABBO_SHIRIN_KONSERVERLAR = "Asal, murabbo, shirin konservalar"
    APERATIFLER_YONGOQLAR_VA_URUGLAR = "Aperatifler, yong'oqlar va urug'lar"
    SOGLOM_OVQATLARNISH = "Sog'lom ovqatlanish"
    SAKLASH = "Saqlash"
    MAKARON_DON_VA_NONUSHTA_DONLARI = "Makaron, don va nonushta donlari"
    UN_SHAKAR_VA_TUZ = "Un, shakar va tuz"
    PISHIRIKLAR_VA_SHIRINLIKLAR_UCHUN_MAHSULOTLAR = "Pishiriqlar va shirinliklar uchun mahsulotlar"
    HASHAROTLAR_VA_KEMIRUVCHILARGA_QARSHI_VOSITALAR = "Hasharotlar va kemiruvchilarga qarshi vositalar"
    YUVISH_UCHUN_VOSITALAR = "Yuvish uchun vositalar"
    TOZALASH_VA_YUVISH_VOSITALARI = "Tozalash va yuvish vositalari"
    POYABZALLARNI_PARVARISH_QILISH_UCHUN_VOSITALAR = "Poyabzallarni parvarish qilish uchun vositalar"
    MAISHIY_TEXNIKA_PARVARISHI_UCHUN_VOSITALAR = "Maishiy texnika parvarishi uchun vositalar"
    IDISH_YUVISH_MASHINALARI_UCHUN_VOSITALAR = "Idish yuvish mashinalari uchun vositalar"
    HAVONI_MUSAFFOLASHTIRGICHLAR_VA_NEYTRALIZATORLAR = "Havoni musaffolashtirgichlar va neytralizatorlar"
    QOG_OZ_MAHSULOTLAR = "Qog'oz mahsulotlari"
    KORGAZMA_TAHTALARI = "Ko'rgazma taxtalari"
    KALKULYATORLAR = "Kalkulyatorlar"
    PATRONLAR = "Patronlar"
    STOL_STENDLARI_VA_BIZNES_KARTA_EGALARI = "Stol stendlari va biznes karta egalari"
    SAVDO_UCHUN_USKUNALAR = "Savdo uchun uskunalar"
    OFIS_JIHOZLARI = "Ofis jihozlari"
    PAPKALAR_VA_FAYLLAR = "Papkalar va fayllar"
    MUHR_VA_SHTAMPLAR = "Muhr va shtamplar"
    YOZISH_ASBObLARI = "Yozish asboblari"
    MAKTAB_VA_TALIM_MAHSULOTLARI = "Maktab va ta'lim mahsulotlari"
    CHIZMA_AKSESSUARLARI = "Chizma aksessuarlari"
    VETERINARIYA_DORIXONASI = "Veterinariya dorixonasi"
    GIGIENA = "Gigiena"
    KEMIRUVCHILAR_UCHUN = "Kemiruvchilar uchun"
    MUSHUKLAR_UCHUN = "Mushuklar uchun"
    QUSHLAR_UCHUN = "Qushlar uchun"
    BALIQ_VA_SUDRALUVCHILAR_UCHUN = "Baliq va sudraluvchilar uchun"
    QISHLOQ_HAYVONLARI_UCHUN = "Qishloq hayvonlari uchun"
    ITLAR_UCHUN = "Itlar uchun"
    BOG_USKUNALARI = "Bog 'uskunalari"
    HOVUZLAR_VA_AKSESSUARLAR = "Hovuzlar va aksessuarlar"
    YOZGI_UY_VA_BOG_NI_TARTIBGA_SOLISH = "Yozgi uy va bog'ni tartibga solish"
    HAYVONLAR_VA_HASHAROTLARGA_QARSHI_VOSITALAR = "Hayvonlar va hasharotlarga qarshi vositalar"
    PIKNIK_BARBEKYU_PANJARA = "Piknik, barbekyu, panjara"
    BOG_MEBELLARI_VA_BEZAKLARI = "Bog 'mebellari va bezaklari"
    BOG_VOSITA = "Bog 'vosita"
    URUGLAR_VA_KOCHATLAR = "Urug'lar va ko'chatlar"
    OGITLAR_VA_OSIMLIKLARNI_PARVARISH_QILISH = "O'g'itlar va o'simliklarni parvarish qilish"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   
class Bigcategory(BaseModel):
    name = models.CharField(choices=BigCategories, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class SmallCategory(BaseModel):
    big_category = models.ForeignKey(Bigcategory, on_delete=models.SET_NULL, null=True, related_name='small_category')
    name = models.CharField(choices=SmallCategories, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Product(BaseModel):
    big_category = models.ForeignKey(Bigcategory, on_delete=models.SET_NULL, null=True ,related_name='big_product')
    small_category = models.ForeignKey(SmallCategory, on_delete=models.SET_NULL, null=True, related_name='small_product')
    name = models.CharField(max_length=255, verbose_name="Nomi")
    image = models.ImageField(upload_to='products/', verbose_name="Rasm", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi", blank=True, null=True)
    description = models.TextField(verbose_name="Tavsifi", blank=True, null=True)
    brand = models.CharField(max_length=100, verbose_name="Brend", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Rangi", blank=True, null=True)
    size = models.CharField(max_length=50, verbose_name="O'lchami", blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Og'irligi", blank=True, null=True)
    material = models.CharField(max_length=100, verbose_name="Materiali", blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, verbose_name="Ishlab chiqarilgan mamlakat", blank=True, null=True)
    warranty = models.CharField(max_length=100, verbose_name="Kafolat", blank=True, null=True)
    availability = models.BooleanField(default=True, verbose_name="Mavjudligi")
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Reyting", blank=True, null=True)
    discount = models.PositiveIntegerField(verbose_name="Chegirma (%)", blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(verbose_name="Soni", default=0)
    tags = models.CharField(max_length=255, verbose_name="Teglar", blank=True, null=True)
    extra_fields = models.JSONField(verbose_name="Qo'shimcha xususiyatlar", blank=True, null=True)  # JSONField Django 3.1+ da mavjud


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100, verbose_name="Ism")
    text = models.TextField(verbose_name="Fikr")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.name}"


