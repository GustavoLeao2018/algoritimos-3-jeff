from arvore-rubro-negra import Arvore
from random import randint

arvore = Arvore()
for i in range(0, randint(10, 100)):
    arvore.inserir(chave=i, valor=randint(0, 1000))

arvore.mostrar()

