from simulation import run_simulation
from plotting import plot_3d_graphs, save_figures, plot_time_graphs
import numpy as np
from clock_algorithm import startClockWithDisplay
# Definição dos parâmetros de simulação
pageListCasesOfAnalysis = [100, 500, 1000]
variabilityOfPages = [0.1 * i for i in range(1, 51)]
frameValues = [0.05 * i for i in range(1, 21)]

# Executar a simulação
resultList = run_simulation(pageListCasesOfAnalysis, variabilityOfPages, frameValues)

# Gerar e salvar os gráficos 3D
figures = plot_3d_graphs(resultList, pageListCasesOfAnalysis)
save_figures(figures)

# Gerar e salvar os gráficos de Frame vs. Time e Variabilidade vs. Time
plot_time_graphs(resultList, pageListCasesOfAnalysis, variabilityOfPages, frameValues)

# Exemplo com iteração a cada segundo.
# frame = 3
# clock = np.zeros((frame,2))
# exemplePageList = [6, 3, 6, 3, 2, 5, 1, 6]
# print(f"lista de paginas a ser acessada: {exemplePageList}")
# startClockWithDisplay(exemplePageList,clock,frame)