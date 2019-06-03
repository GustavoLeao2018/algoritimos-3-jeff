from random import choice


"""

RED BLACK

n = Nó/filho
u = Tio
p = Pai
g = Avo
l = esquerda
r = direita
"""

"""
Regras:

1. Todo nó é b(preto) ou r(vermelho) -> cor // Padrão vermelho
2. A raiz e as folhas são b
3. As folhas são bulas
4. Um nó r pode ter filhos b
5. O número de nós b em qualquer caminho ,
a partir de um nó até as suas folhas contem o mesm número de nós
"""

"""
1. O nó é raiz? finta de b e para
2. O pai é b? para

Sempre o pai é vermelho
3. O tio é R? Procar de cor, p, u, e g. Recomeçare em g (o g passa a ser n)

Sei que o tio é preto
4. N e P estão em lados opostos? 
    Rotaciono p  na direção contraria a n
    Continuo em p

5. Ne P estão no mesmo lado?
    Troco a cor de P e G. Rotaciona o G na direção contraria a P.

"""

