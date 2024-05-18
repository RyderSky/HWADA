ll1_table = {
    'S': {'f': 'S -> A B', 'c': 'S -> A B'},
    'A': {'f': 'A -> f S f', 'c': 'A -> c b B d'},
    'B': {'c': 'B -> c', 'd': 'B -> ε', 'f': 'B -> ε', '$': 'B -> ε'}
}

start_symbol = 'S'

def tokenize(input_string):
    valid_tokens = {'f', 'c', 'b', 'd'}  
    tokens = []
    current_token = ""
    
    for char in input_string:
        current_token += char
        if current_token in valid_tokens:
            tokens.append(current_token)
            current_token = ""
    
    if current_token:
        raise SyntaxError("El token: \"{}\" no es parte de la gramatica".format(current_token))
    
    tokens.append('$')
    return tokens

def parse(symbol, tokens):
    if symbol in {'f', 'c', 'b', 'd', '$'}:
        if tokens and symbol == tokens[0]:
            return tokens[1:]
        else:
            expected_tokens = [symbol]
            raise SyntaxError("Error de sintaxis: se esperaba {}, pero se encontró {}".format(expected_tokens, tokens[0]))

    if symbol in ll1_table:
        current_token = tokens[0] if tokens else '$'
        if current_token not in ll1_table[symbol]:
            expected_tokens = list(ll1_table[symbol].keys())
            raise SyntaxError("Error de sintaxis: para '{}' se esperaba uno de {}, pero se encontró '{}'".format(symbol, expected_tokens, current_token))

        production = ll1_table[symbol][current_token]
        _, production_rhs = production.split("->")
        production_rhs = production_rhs.strip().split()

        for prod_symbol in production_rhs:
            tokens = parse(prod_symbol, tokens)

    return tokens 

input_string = "cbd" 
try:
    tokens = tokenize(input_string) 
    remaining_tokens = parse(start_symbol, tokens) 
    if remaining_tokens == ['$']: 
        print("Cadena aceptada")
    else:
        print("Cadena no aceptada")
except SyntaxError as e:
    print("Error de análisis:", str(e))
