import inquirer
import search as src

def Energy_Fermi ():
	E_fermi=float(input('Enter the Fermi Energy: '))
	return E_fermi

def Energy_graphx ():
	ab = input("Enter the x interval (a,b): ")
	a_b = ab.split(',')
	a_b = [float(num) for num in a_b]
	return a_b


def DOS_type ():
	question = [
		inquirer.List('answer',
		message='Você quer plotar por átomo ou por orbital?',
		choices=['by atoms', 'by orbital'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

def atoms_choice (list_atoms):
	question = [
		inquirer.Checkbox('answer',
		message='Selecione os átomos',
		choices=list_atoms,
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers
	
def spdf_choice (list_spdf):
	question = [
		inquirer.Checkbox('answer',
		message='Selecione os orbitais a serem plotados',
		choices=list_spdf,
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

def yn ():
	question = [
		inquirer.List('answer',
		message='Você quer plotar componentes dos orbitais?',
		choices=['yes', 'no'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

def pdos_tot ():
	question = [
		inquirer.List('answer',
		message='Você quer plotar a PDOS total?',
		choices=['yes', 'no'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

# Escolha de orbitais p
def orbital_component_p ():
	question = [
		inquirer.Checkbox('answer',
		message='Selecione as componentes do orbital p',
		choices=['px', 'py', 'pz'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers

# Escolha de orbitais d
def orbital_component_d ():
	question = [
		inquirer.Checkbox('answer',
		message='Selecione as componentes do orbital d',
		choices=['dz2', 'dzx', 'dzy', 'dx2-y2', 'dxy'],
		carousel=True
		)
	]

	# Executa a pergunta e obtém a resposta do usuário
	answers = inquirer.prompt(question)
	return answers