#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
#  4 January 2019
# 26 December 2018
#
import re
def main():
    '''Extract 33 Sg case statements.'''
    # open works even if filename has spaces
    string = open('../Sg Hypothetical.txt', 'r').read()
    # preprocess file
    # remove page numbers
    string = re.sub(r'\(\d{1,3}[a|b]\)', '', string)
    # make MHE editorial substitutions using capturing groups
    # escape special characters even in raw strings
    string = re.sub(r'plubicum \[(.+?)\]', r'\1', string) # C.5
    string = re.sub(r'commitatus \[(.+?)\]', r'\1', string) # C.10
    string = re.sub(r'asscribi \[(.+?)\]', r'\1', string) # C.21
    string = re.sub(r'sotios \[(.+?)\]', r'\1', string) # C.23
    string = re.sub(r'set \[(.+?)\]', r'\1', string) # C.32
    # remove MHE editorial comments
    string = re.sub(r'\[se representavit\?\]', '', string)
    string = re.sub(r'\[et\]', '', string)
    string = re.sub(r"\[final 'i' appears written over 'o'\]", '', string)
    string = re.sub(
        r'\[Sg\. om: unus relicta propria.+?cenobio se contulit\.\]', '', string
    )
    string = re.sub(r'\[black paragraph symbol\]', '', string)
    # remove square brackets around interlinear readings
    string = re.sub(r'\[(.+?)\]', r'\1', string)
    #
    patterns = [
        # r'Laicus quidam litteratus.*?sit in episcopum\?', # C.Prima
        r'Obtulit quidam filium.*?dignitate sit recipiendus\?', # C.1
        r'Quidam igitur episcopus.*?an sine scripto\?', # C.2
        # r'Quidam episcopus deiectus.*?in accusatorem retorquere\?', # C.3
        r'In excommunicatione quidam.*?sit amplius admittendus\?', # C.4
        r'Ad episcopum quondam.*?obiecit probare nequit\?', # C.5
        r'Fornicatores quidam et.*?probatione suae innocentiae\?', # C.6
        r'Episcopus quidam infirmitate.*?intercessione propria intercepit\?',
        r'Quidam episcopus in.*?ecclesiam redire debeat\?', # C.8
        r'Notatus quidam archiepiscopus.*?vel dampnatos absolvere\?', # C.9
        r'Laicus quidam ecclesiam.*?sacerdotibus exigere valeat\?', # C.10
        r'Adversus clericum clericus.*?inreparabiliter oporteat deponi\?',
        r'Non nulli clericorum.*?eis conficere liceat\?', # C.12
        r'Quidam ecclesiae baptismalis.*?et funerandi tollatur\?', # C.13
        r'Movent adversus quosdam.*?male acceperunt restituant\.', # C.14
        r'In crimine carnis.*?exequi sibi liceat\?', # C.15
        r'Abbas quidam parrochitanam.*?possit eam tenere\?', # C.16
        r'Gravatus infirmitate presbiter.*?effectu petere possit\?', # C.17
        r'Monachus quidam in.*?fratribus sit instituendus\?', # C.18
        r'Volunt duo clerici.*?eis esset concedendus\?', # C.19
        r'Annos pueritiae duo.*?districtius transire liceat\?', # C.20
        r'Cuiusdam ecclesiae archipresbiter.*?iudicem transire possint\?',
        r'Episcopus quidam falsum.*?suum ire conpellit\?', # C.22
        r'Cum plebe sibi.*?arma movere liceat\?', # C.23
        r'Quidam votum castitatis.*?et alii copulari\?', # C.27
        r'Nobili cuidam mulieri.*?illo discedere possit\?', # C.29
        r'Impeditus quidam populi.*?desponsatio manifeste preiudicet\?', # C.30
        r'Quidam alterius uxorem.*?alii nubere possit\?', # C.31
        r'Meretricem quandam pro.*?in coniugem ducere\?', # C.32
        r'Impeditus quidam maleficiis.*?ea extorquere valeat\?', # C.33
        r'Quidam cum ab.*?primum redire cogatur\?', # C.34
        r'Uxore cuiusdam defuncta.*?cognatione prioris viri\?', # C.35
        r'Cuiusdam filiam patre.*?patre assensum praestante\?', # C.36
    ]
    for pattern in patterns:
        result = re.search(re.compile(pattern, re.S), string)
        print(fixString(result.group()))

def fixString(string):
    string = re.sub('\s+', ' ', string)
    string = re.sub(r'(\w+) \.', r'\1.', string)
    return string

if __name__ == '__main__':
    main()
