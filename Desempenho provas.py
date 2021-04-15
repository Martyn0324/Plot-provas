import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Disciplinas = ["Matemática", "Física", "Química", "Biologia", "História", "Geografia", "Português", "Inglês", "Filosofia", "Sociologia"]
Desempenho = {'2020 obtida': [8, 9, 9, 9, 9, 9, 17, 7, 4, 4], '2020 máxima': [9, 9, 9, 9, 9, 9, 18, 8, 5, 5],
'2019 obtida': [9, 8, 9, 9, 9, 8, 17, 7, 6, 3], '2019 máxima': [9, 9, 9, 9, 9, 9, 18, 8, 6, 4],
'2018 obtida': [8, 9, 8, 9, 9, 8, 16, 7, 0, 0], '2018 máxima': [9, 9, 9, 9, 9, 9, 18, 8, 0, 0],
'2017 obtida': [9, 9, 7, 9, 8, 7, 14, 8, 0, 0], '2017 máxima': [9, 9, 9, 9, 9, 9, 18, 8, 0, 0],
'2016 obtida': [8, 7, 8, 16, 11, 13, 14, 8, 0, 0], '2016 máxima(adaptações)': [9, 11, 11, 16, 13, 14, 15, 8, 0, 0]}

desempenho = pd.DataFrame(Desempenho, index=Disciplinas)
print(desempenho)

labels = ['2017', '2018', '2019', '2020']
Acertos = [desempenho['2017 obtida'], desempenho['2018 obtida'], desempenho['2019 obtida'], desempenho['2020 obtida']]
Total = [desempenho['2017 máxima'], desempenho['2018 máxima'], desempenho['2019 máxima'], desempenho['2020 máxima']]

Acertos2 = [np.sum([9, 9, 7, 9, 8, 7, 14, 8, 0, 0])+10, np.sum([8, 9, 8, 9, 9, 8, 16, 7, 0, 0])+10, np.sum([9, 8, 9, 9, 9, 8, 17, 7, 6, 3]),
np.sum([8, 9, 9, 9, 9, 9, 17, 7, 4, 4])]
Total2 = [np.sum([9, 9, 9, 9, 9, 9, 18, 8, 0, 0])+10, np.sum([9, 9, 9, 9, 9, 9, 18, 8, 0, 0])+10, np.sum([9, 9, 9, 9, 9, 9, 18, 8, 6, 4]),
np.sum([9, 9, 9, 9, 9, 9, 18, 8, 5, 5])]
Real = [0, 0, 77, 72]

fig, ax = plt.subplots(sharex=False, sharey=False)

def autolabel(data):
    for data in data:
        height = data.get_height()
        ax.annotate('{}'.format(height), xy = (data.get_x() + data.get_width()/2, height), xytext = (0,3), textcoords="offset points",
        ha = 'center', va='bottom')


Anos = ['2016','2017','2018','2019','2020']
Assuntos = {'Cartografia': [3, 2, 2, 1, 1], 'Geopolítica': [1, 2, 2, 2, 6], 'Fontes de energia': [0, 0, 0, 0, 1], 'Fronteiras': [1, 2, 1, 0, 2],
'Meio ambiente': [0, 1, 2, 1, 1], 'Hidrografia': [0, 0, 1, 1, 1], 'Geomorfologia': [2, 0, 0, 1, 0],
'Demografia': [1, 1, 2, 1, 1], 'Urbanização': [1, 1, 2, 1, 1], 'Indústria': [1, 0, 1, 1, 0],
'Climatologia': [1, 1, 0, 1, 0], 'Agricultura': [2, 1, 1, 1, 0], 'Biogeografia': [1, 0, 0, 0, 0], 'Regionalização do Brasil': [1, 1, 0, 0, 1]}

Geografia = pd.DataFrame(Assuntos, index=Anos)
print(Geografia)

Matérias = ('Cartografia', 'Geopolítica', 'Fontes de energia', 'Fronteiras', 'Meio ambiente', 'Hidrografia', 'Geomorfologia', 'Demografia',
'Urbanização', 'Indústria', 'Climatologia', 'Agricultura', 'Biogeografia', 'Regionalização do Brasil')
Proporção = [18, 26, 2, 12, 10, 6, 6, 12, 12, 6, 6, 10, 2, 6]

ax.pie(Proporção, explode=(0.2,0.2, 0,0,0,0,0,0,0,0,0,0,0,0), labels=Matérias, autopct='%1.1f%%', radius=2, shadow=True, startangle=75)
plt.title("Proporção de temas recorrentes em Geografia")
plt.show()
