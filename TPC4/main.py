import ply.lex as lex
import sys

# Define token names
tokens = (
    'ALIAS',
    'FROM',
    'COMMAND',
    'WHERE',
    'SIGNALS',
    'NUM',
    'LOGIC',
    'IN',
    'DELIMITER',
    'FUNCTION',
    'LEFT_P',
    'RIGHT_P',
    'FIELDS',
    'COMMAND_END',
    'IGNORE',
)

t_ALIAS = r'AS'
t_FROM = r'FROM'
t_COMMAND = r'(SELECT|CREATE TABLE|CREATE INDEX|DROP TABLE|DROP INDEX|DELETE|ALTER TABLE)'
t_WHERE = r'WHERE'
t_SIGNALS = r'>=|<=|\+|-|>|<|='
t_LOGIC = r'AND|OR'
t_IN = r'IN'
t_DELIMITER = r','
t_FUNCTION = r'(AVG|MIN|COUNT|MAX)'
t_LEFT_P = r'\('
t_RIGHT_P = r'\)'
t_FIELDS = r'\w+'
t_COMMAND_END = r';'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def create_lexer():
    return lex.lex()

def main():
    lexer = create_lexer()
    text = sys.stdin.read()
    lexer.input(text)
    while True:
        tok = lexer.token()
        if not tok:
            break      
        print(tok)

if __name__ == '__main__':
    main()
