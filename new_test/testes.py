import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados (15 vetores de y)
x = np.linspace(0, 10, 100)  # Valores de x para o gráfico

# Criar os 15 vetores de y
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)
y4 = np.sin(4*x)
y5 = np.sin(5*x)



# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Plotar os dados usando as cores padrão do matplotlib
ax.plot(x, y1, label='Série 1')
ax.plot(x, y2, label='Série 2')
ax.plot(x, y3, label='Série 3')
ax.plot(x, y4, label='Série 4')


# Adicionar legenda
ax.legend()

# Exibir o gráfico
plt.show()
