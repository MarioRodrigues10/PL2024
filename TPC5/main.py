from ply import lex
import csv
import sys

reserved = {
    'LISTAR' : 'LISTAR',
    'MOEDA' : 'MOEDA',
    'SELECIONAR' : 'SELECIONAR',
    'SAIR' : 'SAIR'
}

tokens = [
    'CURRENCY',
    'NUM',
    'DELIMITER',
    'RESERVED'
] + list(reserved.values())

t_DELIMITER = r','

# A regular expression rule with some action code
def t_CURRENCY(t):
    r'\d+[ecEC]' 
    value_type = t.value[-1:]
    if value_type == 'e':
        t.value = int(t.value[:-1]) * 100
    else:
        t.value = int(t.value[:-1])
    return t

# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RESERVED(t):
    r'(?i)LISTAR|MOEDA|SELECIONAR|SAIR'
    t.type = reserved.get(t.value.upper(),'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Valid coin value (in cents)
valid_coins =[5,10,20,50,100,200]

def read_items():
    items = []
    with open("items.csv",'r') as file:
        reader = csv.DictReader(file,delimiter=';')
        for row in reader:
            items.append(row)
    return items

def calc_change(balance):
    change = {200:0,
          100:0,
          50:0,
          20:0,
          10:0,
          5:0}
    while balance >= 200:
        change[200] += 1
        balance -= 200
    while balance >= 100:
        change[100] += 1
        balance -= 100
    while balance >= 50:
        change[50] += 1
        balance -= 50
    while balance >= 20:
        change[20] += 1
        balance -= 20
    while balance >= 10:
        change[10] += 1
        balance -= 10
    while balance >= 5:
        change[5] += 1
        balance -= 5
    return change       

def print_change(change):
    print("Troco:")
    for coin,ammount in change.items():
        if ammount > 0:
            if coin >= 100:
                coin /= 100
                print(str(ammount) + "x " + str(coin)+"€")
            else:
                print(str(ammount) + "x " + str(coin)+"c")

def main():
    items = read_items()
    line = sys.stdin.readline()
    running = True
    balance = 0
    while line and running:
        coin_mode, select_mode = False, False
        # Give the lexer some input
        lexer.input(line)
        while True:
            tok = lexer.token() #has 4 fields, value, type, lineno e lexpos
            if not tok:
                return
            if tok.type == 'LISTAR' : 
                print("ID Nome  Preço")
                for item in items:
                    print(item['id'] + " " + item['name'] + " " + item['price'])
            elif tok.type == 'MOEDA':
                coin_mode = True
            elif tok.type == 'CURRENCY' and coin_mode:
                if tok.value in valid_coins:
                    balance += tok.value
                else:
                    print("Apenas aceitamos moedas reais com valor superior a 5 cêntimos!")
            elif tok.type == 'SELECIONAR':
                select_mode = True
            elif tok.type == 'NUM' and select_mode:
                if balance >= float(items[tok.value-1]['price']) * 100:
                    print("Produto " + items[tok.value-1]['name'] + " selecionado!")
                    balance -= float(items[tok.value-1]['price']) * 100
                else:
                    print("Saldo insuficiente!")
            elif tok.type == 'SAIR':
                print_change(calc_change(balance))
                running = False
            else: 
                if tok.type != 'DELIMITER':
                    print("Comando não reconhecido!")
            
        line = sys.stdin.readline()
        
if __name__ == '__main__':
    main()
