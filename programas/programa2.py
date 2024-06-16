# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# grammar definition
grammar = """
S -> S X S | '(' S ')' | N
X -> '+' | '-' | '*' | '/'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
"""

grammar2 = """
S -> X '(' S ',' S ')' | '(' S ')' | N
X -> '+' | '-' | '*' | '/'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
"""


def parse(s, grammar):
        
    # parser
    grammar = nltk.CFG.fromstring(grammar)
    # parser = nltk.LeftCornerChartParser(grammar)
    parser = nltk.ChartParser(grammar)

    # tokenize
    s_tokenized = nltk.word_tokenize(s)

    # parse
    # tree =  #[:1]
    tree = list(parser.parse(s_tokenized))[:1]
    return tree
  
# recibe un string perteneciente al lenguaje de grammar1 y lo traduce en un string perteneciente a grammar2 y lo retorna
def traducir(tree):

    if tree.label() == 'S':
      if len(tree) == 3:
        left = traducir(tree[0])
        right = traducir(tree[2])
        op = traducir(tree[1])
        return f"{op}({left},{right})"
    elif len(tree) == 1:
      return traducir(tree[0])
    elif tree.label() == 'N':
      return tree[0]
    elif tree.label() in ['+', '-', '*', '/']:
      return tree[0]
  
    return None

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read().strip()
  
    try:
      tree = parse(s, grammar)
      
      if tree:
          tree = tree[0] # primer árbol de parseo
          salida = traducir(tree)
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
    # f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    # f.write(salida)
    # f.close()
    with io.open(archivo_salida, 'w', newline='\n', encoding='utf-8') as f:
        f.write(salida)
