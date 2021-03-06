# -----------------------------
# Program by Samodelkin
# -----------------------------

import re

mytext = 'Расчеты по сделке купли-продажи Объекта недвижимости производятся с использованием ' \
         'номинального счёта  с ограниченной ответственностью «Центр недвижимости от Сбербанка»' \
         '(ООО «ЦНС»), ИНН 7736249247, открытого в Операционном управлении Московского банка ПАО Сбербанк' \
         'г. Москва, к/счет 30101810400000000225, БИК 044525225. Бенефициаром в отношении денежных средств,' \
         'размещаемых на номинальном счёте, является Продавец'

"""
\d - any digit 0-9
\D -any non digit
\w -any alphabet symbol [A-Z a-z]
\W - any non alphabet
\s - breakspace
\S - non breakspase
[0-9]{3}
[A-Z][a-z]+ - любое слово с большой буквы, вторая буква и далее - маленькие
@\w+\.\w+ - все домены
"""

textlookfor = r"ИНН"
textlookfor2 = r"[0-9]{3}"
allresults = re.findall(textlookfor, mytext)
allresults2 = re.findall(textlookfor2, mytext)
print(allresults)
print(allresults2)