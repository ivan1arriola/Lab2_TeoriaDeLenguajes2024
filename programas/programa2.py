# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl

#ssl._create_default_https_context = ssl._create_unverified_context
#nltk.download('punkt')


grammarInfija = """
S -> S Operador S | '(' S ')' | Numero
Operador -> '+' | '-' | '*' | '/'
Numero -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
"""

def parse(s, grammarInfija):
        
    # parser
    grammarInfija = nltk.CFG.fromstring(grammarInfija)
    parser = nltk.ChartParser(grammarInfija)

    # tokenize // Tokeniza la cadena de entrada // obtiene una lista de terminales
    s_tokenized = nltk.word_tokenize(s)

    # parse
    parses = list(parser.parse(s_tokenized)) # obtiene una lista todos de arboles de derivacion posibles
    if len(parses) == 0:
        return None # si no hay arboles de derivacion posibles, retorna None
    tree = parses[0] # obtiene el primer arbol de derivacion
    return tree
  
# recibe un arbol de derivacion de la gramatica infija y lo traduce a otro arbol de derivacion de la gramatica prefija
def traducir(tree):
    if tree.label() == 'S':
        if tree.productions()[0].__str__() == 'S -> S Operador S':
          # Convertir regla "S -> S Operador S" a regla "S -> Operador '(' S ',' S ')'""
          S1Tree = traducir(tree[0])
          OperadorTree = tree[1]
          S2Tree = traducir(tree[2])

          nuevoTree = nltk.Tree('S', []) # crea un nuevo arbol de derivacion que representa la regla "S -> Operador '(' S ',' S ')'"
          nuevoTree.append(OperadorTree)
          nuevoTree.append('(')
          nuevoTree.append(S1Tree)
          nuevoTree.append(',')
          nuevoTree.append(S2Tree)
          nuevoTree.append(')')

          return nuevoTree
        
        elif tree.productions()[0].__str__() == 'S -> Numero':
            # Convertir regla "S -> Numero" a regla "S -> Numero" // no hace nada en realidad
            return tree[0]
        
        elif tree.productions()[0].__str__() == "S -> '(' S ')'":
            # Convertir regla "S -> "(" S ")" a regla "S -> S " // saca los parentesis
            return traducir(tree[1])
    
    elif tree.label() == 'Operador': # no hace nada, estan por completitud
        return tree[0]
    elif tree.label() == 'Numero': # no hace nada, estan por completitud
        return tree[0]

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read().strip()
  
    try:
      tree = parse(s, grammarInfija)
      
      if tree:
          arbolTraducido = traducir(tree) # convierte un arbol de derivacion de la gramatica infija a un arbol de derivacion de la gramatica prefija
          salida = "".join(arbolTraducido.leaves()) # obtiene las hojas del arbol de derivacion prefija y las concatena
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
    # f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    # f.write(salida)
    # f.close()
    with io.open(archivo_salida, 'w', newline='\n', encoding='utf-8') as f:
        f.write(salida)
