class Professor: 
    def __init__(self,nome,cpf,rg,materia):
        self._nome=nome
        self._cpf=cpf
        self._rg=rg
        self._materia=materia
    # def __str__(self):
    #     return f'Professor(a) {self.nome}, CPF: {self.cpf}, rg:{self.rg}'
usuario=Professor('joana','44444','12313','portugues')

print(usuario._nome, usuario._cpf, usuario._rg, usuario._materia)
