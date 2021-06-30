
#### EXIBIR QUANTOS ALUNOS EM RECUPERAÇÃO

NumAlunos = int(input('numero de alunos: '))
NumAlunosRecuperacao = 0
ContadorDeAlunos = 1

while ContadorDeAlunos <= NumAlunos:
	print('entre com a nota final do', ContadorDeAlunos,'º aluno: ')
	notaAluno = float(input())
	ContadorDeAlunos = 1 + ContadorDeAlunos
	if notaAluno >= 3 and notaAluno < 5:
		NumAlunosRecuperacao = NumAlunosRecuperacao + 1
	else:
		NumAlunosRecuperacao = NumAlunosRecuperacao
print('Temos', NumAlunosRecuperacao, 'alunos para recuperacao.')
