import inquirer
import search as src

def Energy_Fermi ():
	E_fermi=float(input('Enter the Fermi Energy: '))
	return E_fermi


def DOS_type ():
	question = [
		inquirer.List('answer',
		message='Você quer plotar por átomo ou por orbital?',
		choices=['by atoms', 'by orbital', 'by my way'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

def atoms_choice ():
	question = [
		inquirer.Checkbox('answer',
		message='Selecione os átomos: ',
		choices=src.list_atoms,
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers
	
def spdf_choice ():
	question = [
		inquirer.Checkbox('answer',
		message='Selecione os orbitais a serem plotados',
		choices=src.list_spdf,
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers