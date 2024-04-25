## Grafico de linhas
# import matplotlib.pyplot as plt
# meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
# valores=[111,222,333,444,555,666,777,888,999,101010,111111,121212]

# plt.plot(meses,valores) 
# plt.xlabel('Meses')
# plt.ylabel('Valores')
# plt.title('Valores de venda 2023')
# plt.show()  

## Grafico de colunas
# import matplotlib.pyplot  as plt
# meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
# valores=[2938,495,807,1832,2555,666,1777,888,999,1010,111,121]


# bars=plt.bar(meses,valores)
# plt.bar_label(bars,labels=valores,label_type='center')
# plt.xlabel('Meses')
# plt.ylabel('Valores')
# plt.title('Valores de venda 2023')
# plt.show()  

## grafico pizza 
### site matplotlib.org > examples
# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# recipe = ["375 g flour",
#           "75 g sugar",
#           "250 g butter",
#           "300 g berries"]

# data = [float(x.split()[0]) for x in recipe]
# ingredients = [x.split()[-1] for x in recipe]


# def func(pct, allvals):
#     absolute = int(np.round(pct/100.*np.sum(allvals)))
#     return f"{pct:.1f}%\n({absolute:d} g)"


# wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
#                                   textprops=dict(color="w"))

# ax.legend(wedges, ingredients,
#           title="Ingredients",
#           loc="center left",
#           bbox_to_anchor=(1, 0, 0.5, 1))

# plt.setp(autotexts, size=8, weight="bold")

# ax.set_title("Matplotlib bakery: A pie")

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]

N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)

cmap = plt.colormaps["plasma"]
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")

plt.show()