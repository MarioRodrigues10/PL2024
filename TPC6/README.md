Descrição do Problema
Queremos desenvolver uma gramática independente de contexto (GIC) simples para o seguinte exemplo:
```
?a
b = a*2 / (27-3)
!a+b
c = a*b / (a/b)
```

**Definições**
Terminais (T): {'?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}
Não-terminais (N): {S, Exp1, Exp2, Exp3, Op1, Op2}
Símbolo inicial (S): S

Produções (P)

```
S    -> '?' id                // Lookahead = {'?'}
     | '!' Exp1               // Lookahead = {'!'}
     | id '=' Exp1            // Lookahead = {id}

Exp1 -> Exp2 Op1              // Lookahead = {'(', num, id}

Op1  -> '+' Exp1              // Lookahead = {'+'}
     | '-' Exp1               // Lookahead = {'-'}
     | ε                      // Lookahead = {')', ε}

Exp2 -> Exp3 Op2              // Lookahead = {'(', num, id}

Op2  -> '*' Exp2              // Lookahead = {'*'}
     | '/' Exp2               // Lookahead = {'/'}
     | ε                      // Lookahead = {'+', '-', ')', ε}

Exp3 -> '(' Exp1 ')'          // Lookahead = {'('}
     | num                    // Lookahead = {num}
     | id                     // Lookahead = {id}
```

**Verificação de Conflitos**
A gramática foi projetada para ser livre de conflitos LL(1). Aqui está a verificação para cada produção:

```
S

S -> '?' id Lookahead = {'?'}
S -> '!' Exp1 Lookahead = {'!'}
S -> id '=' Exp1 Lookahead = {id}
Não há interseção entre os conjuntos de lookaheads.

Exp1

Exp1 -> Exp2 Op1 Lookahead = {'(', num, id}
Op1

Op1 -> '+' Exp1 Lookahead = {'+'}
Op1 -> '-' Exp1 Lookahead = {'-'}
Op1 -> ε Lookahead = {')', ε}
Não há interseção entre os conjuntos de lookaheads.

Exp2

Exp2 -> Exp3 Op2 Lookahead = {'(', num, id}
Op2

Op2 -> '*' Exp2 Lookahead = {'*'}
Op2 -> '/' Exp2 Lookahead = {'/'}
Op2 -> ε Lookahead = {'+', '-', ')', ε}
Não há interseção entre os conjuntos de lookaheads.

Exp3

Exp3 -> '(' Exp1 ')' Lookahead = {'('}
Exp3 -> num Lookahead = {num}
Exp3 -> id Lookahead = {id}
Não há interseção entre os conjuntos de lookaheads.
```