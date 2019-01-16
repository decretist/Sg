#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
# 26 December 2018
#
import re
def main():
    string = open('../hand/Gratian3.txt', 'r').read()
    # 154 words in Sg case statements not in Fr.
    string = re.sub('v', 'u', string)
    # 56 words in Sg case statements not in Fr.
    string = re.sub('elymosina', 'elemosina', string)
    string = re.sub('epystolam', 'epistolam', string)
    string = re.sub('presbyterum', 'presbiterum', string)
    string = re.sub('synodalem', 'sinodalem', string)
    string = re.sub('synodali', 'sinodali', string)
    # 51 words in Sg case statements not in Fr.
    string = re.sub("praestandum", "prestandum", string)
    string = re.sub("praestante", "prestante", string)
    string = re.sub("praestitisse", "prestitisse", string)
    string = re.sub("praestitit", "prestitit", string)
    string = re.sub("praestituta", "prestituta", string)
    string = re.sub("praesumit", "presumit", string)
    #
    string = re.sub("benefitio", "beneficio", string)
    string = re.sub("indutias", "inducias", string)
    string = re.sub("indutiis", "induciis", string)
    string = re.sub("licenciam", "licentiam", string)
    string = re.sub("puditiciam", "pudicitiam", string)
    string = re.sub("renuntians", "renuncians", string)
    string = re.sub("restitucionis", "restitutionis", string)
    # 39 words in Sg case statements not in Fr.
    string = re.sub("commissa", "conmissa", string)
    string = re.sub("commitatus", "conmittatus", string)
    string = re.sub("concedende", "concedendae", string)
    string = re.sub("impugnare", "inpugnare", string)
    string = re.sub("optulit", "obtulit", string)
    string = re.sub("parochiam", "parrochiam", string)
    string = re.sub("seperare", "separare", string)
    string = re.sub("seperari", "separari", string)
    string = re.sub("xiiii", "xiv", string)

    print(string)

if __name__ == '__main__':
    main()
