import re

error = False
#Regex definition
blank = [" ", "\r", "\n", "\t"]
regEx = {
    "Exponencial" : "[0-9]+\\.[0-9]+E[+-][0-9]+",
    "Flotante" : "[0-9]+\\.[0-9]+",
    "Entero" : "[0-9]+",
    "Suma" : "\\+",
    "parI" : "\\(",
    "parD" : "\\)"
}

def scanner(input_string):
    string = input_string
    while(len(string) != 0):
        if string[0] in blank:
            string = string[1:]
            continue
        for key in regEx:
            if re.search(regEx[key], string) and 0 in (re.search(regEx[key], string).span()):
                tokens.append(key)
                string = re.sub(regEx[key], "", string, 1)
                error = False
                break
            else: error = True
        if error == True:
            print("No existe token definido para caso: ", string)
            exit()
         
tokens = []
scanner("(143+45.5) 156.6E+78+78")
print(tokens)
