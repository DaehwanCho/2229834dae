import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LanguageExchange')
import django
django.setup()

from LanguageExchange.models import Language

def inputing():
    lan = ['Afrikaans', 'Albanian', 'Amharic','Arabic','Aramaic','Armenian','Assamese','Aymara','Azerbaijani','Balochi','Bamanankan','Bashkort','Basque','Belarusan','Bengali','Bhojpuri','Bislama','Bosnian','Brahui','Bulgarian','Burmese','Cantonese','Catalan','Cebuano','Chechen','Cherokee','Croatian','Czech','Dakota','Danish','Dari','Dholuo','Dutch','English','Esperanto','Estonian','Ewe','Finnish','French','Georgian','German','Gikuyu','Greek','Guarani','Gujarati','Haitian Creole','Hausa','Hawaiian','Hawaiian Creole','Hebrew','Hiligaynon','Hindi','Hungarian','Icelandic','Igbo','Ilocano','Indonesian','Inuit','Irish Gaelic','Italian','Japanese','Jarai','Javanese','K’iche’','Kabyle','Kannada','Kashmiri','Kazakh','Khmer','Khoekhoe','Korean','Kurdish','Kyrgyz','Lao','Latin','Latvian','Lingala','Lithuanian','Macedonian','Maithili','Malagasy','Malay','Malayalam','Mandarin','Marathi','Mende','Mongolian','Nahuatl','Navajo','Nepali','Norwegian','Ojibwa','Oriya','Oromo','Pashto','Persian','Polish','Portuguese','Punjabi','Quechua','Romani','Romanian','Russian','Rwanda','Samoan','Sanskrit','Serbian','Shona','Sindhi','Sinhala','Slovak','Slovene','Somali','Spanish','Swahili','Swedish','Tachelhit','Tagalog','Tajiki','Tamil','Tatar','Telugu','Thai','Tibetic languages','Tigrigna','Tok Pisin','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Warlpiri','Welsh','Wolof','Xhosa','Yakut','Yiddish','Yoruba','Yucatec','Zapotec','Zulu']
    for i in range(lan.length):
        add_language(lang)

def add_language(language):
    l = Language.objects.get_or_create(language = lan)[0]
    l.lan = language
    l.save()
    return l


inputing()