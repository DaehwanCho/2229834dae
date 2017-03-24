#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)



class MyUserManager(BaseUserManager):
    def create_user(self, email,username,Nationality,Mother_language,Wish_language,Profile_image,status_message,password=None):
        
        if not email:
            raise ValueError('Users must have an email address')
       

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            Profile_image=Profile_image,
            Nationality=Nationality,
            Mother_language=Mother_language,
            Wish_language=Wish_language,
            status_message=status_message,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,Nationality,Mother_language,Wish_language,password,status_message,Profile_image):
       
        user = self.create_user(email,
            password=password,
            username=username,
            Profile_image=Profile_image,
            Nationality=Nationality,
            Mother_language=Mother_language,
            Wish_language=Wish_language,
            status_message=status_message,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
Language_list=( ("","Please Select"),
('AFRIKAANS','Afrikaans'),
('ALBANIAN','Albanian'),
('AMHARIC','Amharic'),
('ARABIC','Arabic'),
('ARAMAIC','Aramaic'),
('ARMENIAN','Armenian'),
('ASSAMESE','Assamese'),
('AYMARA','Aymara'),
('AZERBAIJANI','Azerbaijani'),
('BALOCHI','Balochi'),
('BAMANANKAN','Bamanankan'),
('BASHKORT','Bashkort'),
('BASQUE','Basque'),
('BELARUSAN','Belarusan'),
('BENGALI','Bengali'),
('BHOJPURI','Bhojpuri'),
('BISLAMA','Bislama'),
('BOSNIAN','Bosnian'),
('BRAHUI','Brahui'),
('BULGARIAN','Bulgarian'),
('BURMESE','Burmese'),
('CANTONESE','Cantonese'),
('CATALAN','Catalan'),
('CEBUANO','Cebuano'),
('CHECHEN','Chechen'),
('CHEROKEE','Cherokee'),
('CROATIAN','Croatian'),
('CZECH','Czech'),
('DAKOTA','Dakota'),
('DANISH','Danish'),
('DARI','Dari'),
('DHOLUO','Dholuo'),
('DUTCH','Dutch'),
('ENGLISH','English'),
('ESPERANTO','Esperanto'),
('ESTONIAN','Estonian'),
('FINNISH','Finnish'),
('FRENCH','French'),
('GEORGIAN','Georgian'),
('GERMAN','German'),
('GIKUYU','Gikuyu'),
('GREEK','Greek'),
('GUARANI','Guarani'),
('GUJARATI','Gujarati'),
('HAITIAN CREOLE','Haitian Creole'),
('HAUSA','Hausa'),
('HAWAIIAN','Hawaiian'),
('HAWAIIAN CREOLE','Hawaiian Creole'),
('HEBREW','Hebrew'),
('HILIGAYNON','Hiligaynon'),
('HINDI','Hindi'),
('HUNGARIAN','Hungarian'),
('ICELANDIC','Icelandic'),
('IGBO','Igbo'),
('ILOCANO','Ilocano'),
('INDONESIAN','Indonesian'),
('INUIT/INUPIAQ','Inuit/Inupiaq'),
('IRISH GAELIC','Irish Gaelic'),
('ITALIAN','Italian'),
('JAPANESE','Japanese'),
('JARAI','Jarai'),
('JAVANESE','Javanese'),
('KABYLE','Kabyle'),
('KANNADA','Kannada'),
('KASHMIRI','Kashmiri'),
('KAZAKH','Kazakh'),
('KHMER','Khmer'),
('KHOEKHOE','Khoekhoe'),
('KOREAN','Korean'),
('KURDISH','Kurdish'),
('KYRGYZ','Kyrgyz'),
('LAO','Lao'),
('LATIN','Latin'),
('LATVIAN','Latvian'),
('LINGALA','Lingala'),
('LITHUANIAN','Lithuanian'),
('MACEDONIAN','Macedonian'),
('MAITHILI','Maithili'),
('MALAGASY','Malagasy'),
('MALAY','Malay'),
('MALAYALAM','Malayalam'),
('MANDARIN','Mandarin'),
('MARATHI','Marathi'),
('MENDE','Mende'),
('MONGOLIAN','Mongolian'),
('NAHUATL','Nahuatl'),
('NAVAJO','Navajo'),
('NEPALI','Nepali'),
('NORWEGIAN','Norwegian'),
('OJIBWA','Ojibwa'),
('ORIYA','Oriya'),
('OROMO','Oromo'),
('PASHTO','Pashto'),
('PERSIAN','Persian'),
('POLISH','Polish'),
('PORTUGUESE','Portuguese'),
('PUNJABI','Punjabi'),
('QUECHUA','Quechua'),
('ROMANI','Romani'),
('ROMANIAN','Romanian'),
('RUSSIAN','Russian'),
('RWANDA','Rwanda'),
('SAMOAN','Samoan'),
('SANSKRIT','Sanskrit'),
('SERBIAN','Serbian'),
('SHONA','Shona'),
('SINDHI','Sindhi'),
('SINHALA','Sinhala'),
('SLOVAK','Slovak'),
('SLOVENE','Slovene'),
('SOMALI','Somali'),
('SPANISH','Spanish'),
('SWAHILI','Swahili'),
('SWEDISH','Swedish'),
('TAIWANESE','Taiwanese'),
('TACHELHIT','Tachelhit'),
('TAGALOG','Tagalog'),
('TAJIKI','Tajiki'),
('TAMIL','Tamil'),
('TATAR','Tatar'),
('TELUGU','Telugu'),
('THAI','Thai'),
('TIBETIC LANGUAGES','Tibetic languages'),
('TIGRIGNA','Tigrigna'),
('TOK PISIN','Tok Pisin'),
('TURKISH','Turkish'),
('TURKMEN','Turkmen'),
('UKRAINIAN','Ukrainian'),
('URDU','Urdu'),
('UYGHUR','Uyghur'),
('UZBEK','Uzbek'),
('VIETNAMESE','Vietnamese'),
('WARLPIRI','Warlpiri'),
('WELSH','Welsh'),
('WOLOF','Wolof'),
('XHOSA','Xhosa'),
('YAKUT','Yakut'),
('YIDDISH','Yiddish'),
('YORUBA','Yoruba'),
('YUCATEC','Yucatec'),
('ZAPOTEC','Zapotec'),
('ZULU','Zulu'),

)
Country_choice=(("","Please Select"),
('AFGHANISTAN','Afghanistan'),
('ALBANIA','Albania'),
('AMHARIC','Amharic'),
('ALGERIA','Algeria'),
('ANDORRA','Andorra'),
('ANGOLA','Angola'),
('ANTIGUA','Antigua'),
('ARGENTINA','Argentina'),
('ARMENIA','Armenia'),
('AUSTRALIA','Australia'),
('AUSTRIA','Austria'),
('AZERBAIJAN','Azerbaijan'),
('BAHAMAS','Bahamas'),
('BAHRAIN','Bahrain'),
('BANGLADESH','Bangladesh'),
('BARBADOS','Barbados'),
('BELARUS','Belarus'),
('BELGIUM','Belgium'),
('BELIZE','Belize'),
('BENIN','Benin'),
('BHUTAN','Bhutan'),
('BOLIVIA','Bolivia'),
('BOSNIA','Bosnia'),
('BOTSWANA','Botswana'),
('BRAZIL','Brazil'),
('BRUNEI','Brunei'),
('BULGARIA','Bulgaria'),
('BURKINA FASO','Burkina Faso'),
('BURUNDI','Burundi'),
('CABO VERDE','Cabo Verde'),
('CAMBODIA','Cambodia'),
('CAMEROON','Cameroon'),
('CANADA','Canada'),
('CENTRAL AFRICAN REPUBLIC (CAR)','Central African Republic (CAR)'),
('CHAD','Chad'),
('CHILE','Chile'),
('CHINA','China'),
('COLOMBIA','Colombia'),
('COMOROS','Comoros'),
('COSTA RICA','Costa Rica'),
('CROATIA','Croatia'),
('CUBA','Cuba'),
('CYPRUS','Cyprus'),
('CZECH REPUBLIC','Czech Republic'),
('DEMOCRATIC REPUBLIC OF THE CONGO','Democratic Republic of the Congo'),
('DENMARK','Denmark'),
('DJIBOUTI','Djibouti'),
('DOMINICA','Dominica'),
('DOMINICAN REPUBLIC','Dominican Republic'),
('ECUADOR','Ecuador'),
('EGYPT','Egypt'),
('EL SALVADOR','El Salvador'),
('EQUATORIAL GUINEA','Equatorial Guinea'),
('ERITREA','Eritrea'),
('ESTONIA','Estonia'),
('ETHIOPIA','Ethiopia'),
('FIJI','Fiji'),
('FINLAND','Finland'),
('FRANCE','France'),
('GABON','Gabon'),
('GAMBIA','Gambia'),
('GEORGIA','Georgia'),
('GERMANY','Germany'),
('GHANA','Ghana'),
('GREECE','Greece'),
('GRENADA','Grenada'),
('GUATEMALA','Guatemala'),
('GUINEA','Guinea'),
('GUINEA-BISSAU','Guinea-Bissau'),
('GUYANA','Guyana'),
('HAITI','Haiti'),
('HONDURAS','Honduras'),
('HUNGARY','Hungary'),
('ICELAND','Iceland'),
('INDIA','India'),
('INDONESIA','Indonesia'),
('IRAN','Iran'),
('IRAQ','Iraq'),
('IRELAND','Ireland'),
('ISRAEL','Israel'),
('ITALY','Italy'),
('JAMAICA','Jamaica'),
('JAPAN','Japan'),
('JORDAN','Jordan'),
('KAZAKHSTAN','Kazakhstan'),
('KENYA','Kenya'),
('KIRIBATI','Kiribati'),
('KOSOVO','Kosovo'),
('KUWAIT','Kuwait'),
('KYRGYZSTAN','Kyrgyzstan'),
('LAOS','Laos'),
('LATVIA','Latvia'),
('LEBANON','Lebanon'),
('LESOTHO','Lesotho'),
('LIBERIA','Liberia'),
('LIBYA','Libya'),
('LIECHTENSTEIN','Liechtenstein'),
('LITHUANIA','Lithuania'),
('LUXEMBOURG','Luxembourg'),
('MACEDONIA','Macedonia'),
('MADAGASCAR','Madagascar'),
('MALAWI','Malawi'),
('MALAYSIA','Malaysia'),
('MALDIVES','Maldives'),
('MALI','Mali'),
('MALTA','Malta'),
('MARSHALL ISLANDS','Marshall Islands'),
('MAURITANIA','Mauritania'),
('MAURITIUS','Mauritius'),
('MEXICO','Mexico'),
('MICRONESIA','Micronesia'),
('MOLDOVA','Moldova'),
('MONACO','Monaco'),
('MONGOLIA','Mongolia'),
('MONTENEGRO','Montenegro'),
('MOROCCO','Morocco'),
('MOZAMBIQUE','Mozambique'),
('MYANMAR (BURMA)','Myanmar (Burma)'),
('NAMIBIA','Namibia'),
('NAURU','Nauru'),
('NEPAL','Nepal'),
('NETHERLANDS','Netherlands'),
('NEW ZEALAND','New Zealand'),
('NICARAGUA','Nicaragua'),
('NIGER','Niger'),
('NIGERIA','Nigeria'),
('NORTH KOREA','North Korea'),
('NORWAY','Norway'),
('OMAN','Oman'),
('PAKISTAN','Pakistan'),
('PALAU','Palau'),
('PALESTINE','Palestine'),
('PANAMA','Panama'),
('PAPUA NEW GUINEA','Papua New Guinea'),
('PARAGUAY','Paraguay'),
('PERU','Peru'),
('PHILIPPINES','Philippines'),
('POLAND','Poland'),
('PORTUGAL','Portugal'),
('QATAR','Qatar'),
('REPUBLIC OF THE CONGO','Republic of the Congo'),
('ROMANIA','Romania'),
('RUSSIA','Russia'),
('RWANDA','Rwanda'),
('SAINT KITTS','Saint Kitts'),
('SAINT LUCIA','Saint Lucia'),
('SAINT VINCENT','Saint Vincent'),
('SAMOA','Samoa'),
('SAN MARINO','San Marino'),
('SAO TOME','Sao Tome'),
('SAUDI ARABIA','Saudi Arabia'),
('SENEGAL','Senegal'),
('SERBIA','Serbia'),
('SEYCHELLES','Seychelles'),
('SIERRA LEONE','Sierra Leone'),
('SINGAPORE','Singapore'),
('SLOVAKIA','Slovakia'),
('SLOVENIA','Slovenia'),
('SOLOMON ISLANDS','Solomon Islands'),
('SOMALIA','Somalia'),
('SOUTH AFRICA','South Africa'),
('SOUTH KOREA','South Korea'),
('SOUTH SUDAN','South Sudan'),
('SPAIN','Spain'),
('SRI LANKA','Sri Lanka'),
('SUDAN','Sudan'),
('SURINAME','Suriname'),
('SWAZILAND','Swaziland'),
('SWEDEN','Sweden'),
('SWITZERLAND','Switzerland'),
('SYRIA','Syria'),
('TAIWAN','Taiwan'),
('TAJIKISTAN','Tajikistan'),
('TANZANIA','Tanzania'),
('THAILAND','Thailand'),
('TIMOR-LESTE','Timor-Leste'),
('TOGO','Togo'),
('TONGA','Tonga'),
('TRINIDAD','Trinidad'),
('TUNISIA','Tunisia'),
('TURKEY','Turkey'),
('TURKMENISTAN','Turkmenistan'),
('TUVALU','Tuvalu'),
('UGANDA','Uganda'),
('UKRAINE','Ukraine'),
('UNITED ARAB EMIRATES (UAE)','United Arab Emirates (UAE)'),
('UNITED KINGDOM (UK)','United Kingdom (UK)'),
('UNITED STATES OF AMERICA (USA)','United States of America (USA)'),
('URUGUAY','Uruguay'),
('UZBEKISTAN','Uzbekistan'),
('VANUATU','Vanuatu'),
('VATICAN CITY (HOLY SEE)','Vatican City (Holy See)'),
('VENEZUELA','Venezuela'),
('VIETNAM','Vietnam'),
('YEMEN','Yemen'),
('ZAMBIA','Zambia'),
('ZIMBABW','Zimbabw'),

)



class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,null = False
    )
    username = models.CharField(max_length = 30, null = False)
   
    Nationality =models.CharField(max_length = 30,choices= Country_choice,null = False )
    Mother_language = models.CharField(max_length = 30,choices= Language_list,null = False)
    Wish_language =models.CharField(max_length = 30,choices= Language_list,null = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    Profile_image = models.ImageField(upload_to='profile_images',blank=True, )
    status_message=models.CharField(max_length = 500,null = True)
    objects = MyUserManager()
    
   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','Nationality','Mother_language','Wish_language','Profile_image','status_message']
        
   
    
    def set_Profile_image(self):
       self.has_Profile_image = True
    
    def get_full_name(self):
       
        return self.email
  
    def get_short_name(self):
       
        return self.email
    
    def __str__(self):             
        return self.email

    def has_perm(self, perm, obj=None):
       
        return True

    def has_module_perms(self, app_label):
        
        return True

    @property
    def is_staff(self):
       
        return self.is_admin

    
