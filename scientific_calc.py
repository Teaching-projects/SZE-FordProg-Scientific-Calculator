import ply.lex as lex
import ply.yacc as yacc
import sys
import math


def sin(s):
    sin = math.sin(s)
    return sin

def cos(s):
    cos = math.cos(s)
    return cos

def tan(s):
    if cos(s)==0:
        return p_error_arc(s)
    else:
        return sin(s)/cos(s)    
def asin(s):
    sinh = math.asin(s)
    return sinh

def acos(s):
    cosh = math.acos(s)
    return cosh

def atan(s):
    tanh = math.atan(s)
    return tanh


tokens=['INT','FLOAT','PLUS','MINUS','MULTIPLY','DIVIDE','LPAREN','RPAREN','SIN','COS','TAN','ASIN','ACOS','ATAN','LOG2','LOG','LOG10','POW','COMMA','SQRT','ABS']

t_PLUS=r'\+'
t_MINUS=r'\-'
t_MULTIPLY=r'\*'
t_DIVIDE=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_SIN=r'sin|SIN'
t_COS=r'cos|COS'
t_TAN=r'tan|TAN'
t_ASIN=r'asin|ASIN'
t_ACOS=r'acos|ACOS'
t_ATAN=r'atan|ATAN'
t_LOG2=r'LOG2|log2'
t_LOG=r'LOG[0-9]*|log[0-9]*'
t_LOG10=r'LOG10|log10'
t_POW=r'pow|POW'
t_COMMA=r'\,'
t_SQRT=r'SQRT|sqrt'
t_ABS=r'abs|ABS'
t_ignore = r' '
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_error(t):
    print("Wrong characters!")
    t.lexer.skip(1)
    return t

lexer = lex.lex()
precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE'),
    ('right','UMINUS')
)

def p_main(p):
    '''
    main : expression
         | empty
    '''
def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression 
               | expression PLUS expression
               | expression MINUS expression
               | empty
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]      
        
    print(p[0])
def p_expression_spec(p):
    '''
    expression : POW LPAREN expression COMMA expression RPAREN
               | SQRT LPAREN expression RPAREN
               | ABS LPAREN expression RPAREN 
    '''
    if p[1].upper() == 'POW':
        p[0] = math.pow(p[3],p[5])
    elif p[1].upper() == 'SQRT':
        p[0] = math.sqrt(p[3])
    elif p[1].upper() == 'ABS':
        p[0] = abs(p[3])
    print(p[0])
def p_expression_trig(p):
    '''    
    expression : SIN LPAREN expression RPAREN
               | COS LPAREN expression RPAREN 
               | TAN LPAREN expression RPAREN
               | ASIN LPAREN expression RPAREN
               | ACOS LPAREN expression RPAREN
               | ATAN LPAREN expression RPAREN
    '''
    if p[1].upper() == 'SIN':
        p[0] = sin(p[3])
    elif p[1].upper() == 'COS':
        p[0] = cos(p[3])
    elif p[1].upper() == 'TAN':
        p[0] = tan(p[3])
    elif p[1].upper() == 'ASIN':
        if -1 <= float(p[3]) <= 1:
            p[0] = asin(p[3])
        else:
            p[0] = p_arc_error(p[1])
    elif p[1].upper() == 'ACOS':
        if -1 <= float(p[3]) <= 1:
            p[0] = acos(p[3])
        else:
            p[0] = p_arc_error(p[1])
    elif p[1].upper() == 'ATAN':
        if -1 <= float(p[3]) <= 1:
            p[0] = atan(p[3])
        else:
            p[0] = p_arc_error(p[1])
    print(p[0])
def p_expression_log(p):
    '''
    expression : LOG2 LPAREN expression RPAREN 
               | LOG10 LPAREN expression RPAREN
               | LOG LPAREN expression RPAREN
    '''
    if p[1].upper() == 'LOG2':
        p[0] = math.log2(p[3])
    elif p[1].upper() == 'LOG10':
        p[0] = math.log10(p[3])
    else:
        s = p[1]
        if s[3:] != '': 
            p[0] = math.log(p[3],int(s[3:]))
    print(p[0])
def p_expression_uminus(p):
    '''
    expression : MINUS expression %prec UMINUS
    '''
    p[0] = -p[2]

def p_expression_int_float(p):
    '''
    expression : FLOAT
               | INT
    '''
    p[0] = p[1]


def p_error(p):
  if p:
      print("Syntax error at '%s'" % p.value)
  else:
      print("Syntax error at EOF")
def p_arc_error(p2):
    p = "The adjusted value ('%s') must be between -1 and 1!" % (p2)
    return p
def p_error_arc(p):
  if p:
      print("Syntax error at '%s'" % p)
  else:
      print("Syntax error at EOF")
def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None
parser = yacc.yacc()

while True:
    try:
        s = input('>>>> ')
    except EOFError:
        break
    parser.parse(s)
