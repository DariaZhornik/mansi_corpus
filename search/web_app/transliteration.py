import re
from transliterators.adyghe import adyghe_translit_ipa, adyghe_input_normal
from transliterators.khinalug import khinalug_input_normal
from transliterators.beserman import beserman_translit_cyrillic
from transliterators.udmurt import udmurt_translit_upa
from transliterators.erzya import erzya_translit_upa
from transliterators.albanian import albanian_input_normal
from transliterators.uralic_simple import uralic_input_simplified, uralic_input_simplified_cyr


def trans_IPA_baseline(text, lang):
    if lang == 'adyghe':
        return adyghe_translit_ipa(text)
    return text


def trans_UPA_baseline(text, lang):
    if lang == 'udmurt':
        return udmurt_translit_upa(text)
    elif lang == 'erzya':
        return erzya_translit_upa(text)
    return text


def trans_cyrillic_baseline(text, lang):
    if lang == 'beserman':
        return beserman_translit_cyrillic(text)
    return text


def input_method_normal(field, text, lang):
    if lang == 'adyghe':
        return adyghe_input_normal(field, text)
    elif lang == 'khinalug':
        return khinalug_input_normal(field, text)
    elif lang == 'albanian':
        return albanian_input_normal(field, text)
    return text


def input_method_simplified(field, text, lang):
    if lang in ('selkup', 'kamas', 'nganasan'):
        return uralic_input_simplified(field, text)
    elif lang in ('udmurt', 'komi', 'komi-zyrian', 'komi-permyak',
                  'meadow_mari', 'hill_mari',
                  'tatar', 'bashkir', 'chuvash'):
        return uralic_input_simplified_cyr(field, text)
    return text


