import matplotlib.pyplot as plt
import numpy as np
# Função para criar gráficos 3D para taxa de falhas e acertos
def plot_3d_graphs(resultList, pageListCasesOfAnalysis):
    figures = []
    for eachCase in pageListCasesOfAnalysis:
        fig = plt.figure(figsize=(1280/96, 720/96))
        ax = fig.add_subplot(111, projection='3d')
        x_data, y_data, z_data, dz, dz2 = [], [], [], [], []

        for result in resultList:
            for entry in result:
                faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
                if pageListSize == eachCase:
                    x_data.append(frame)
                    y_data.append(pageMaxVariab)
                    z_data.append(0)
                    dz.append(faultR / pageListSize)
                    dz2.append(foundR / pageListSize)
        
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        z_data = np.array(z_data)
        dz = np.array(dz)
        x_width, y_depth = 0.05, 0.1

        # Plotar gráficos de falhas
        ax.bar3d(x_data, y_data, z_data, x_width, y_depth, dz, shade=True)
        ax.set_xlabel('Frame')
        ax.set_ylabel('Max Page Variability')
        ax.set_zlabel('Fault Rate')
        ax.set_title(f'3D Graph for Fault Rate by Page List Size = {eachCase}')
        figures.append(fig)

        # Plotar gráficos de acertos
        fig = plt.figure(figsize=(1280/96, 720/96))
        ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(y_data, x_data, z_data, y_depth, x_width, dz2, shade=True)
        ax.set_ylabel('Frame')
        ax.set_xlabel('Max Page Variability')
        ax.set_zlabel('Found Rate')
        ax.set_title(f'3D Graph for Found Rate by Page List Size = {eachCase}')
        figures.append(fig)

    return figures

# Função para salvar os gráficos em arquivos
def save_figures(figures):
    figures[0].savefig('100Fault.png')
    figures[1].savefig('100Found.png')
    figures[2].savefig('500Fault.png')
    figures[3].savefig('500Found.png')
    figures[4].savefig('1000Fault.png')
    figures[5].savefig('1000Found.png')

# Função para plotar gráficos de Frame vs Tempo e Variabilidade vs Tempo
def plot_time_graphs(resultList, pageListCasesOfAnalysis, variabilityOfPages, frameValues):
    for eachCase in pageListCasesOfAnalysis:
        fig = plt.figure(figsize=(1280/96, 720/96))
        x_dataFrame, timeY1 = [], []
        x_dataPageMaxVariab, timeY2 = [], []
        
        # Gera dados para plotagem de frame vs tempo
        for variability in variabilityOfPages:
            timeData, x_data = [], []
            for result in resultList:
                for entry in result:
                    faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
                    if pageListSize == eachCase and variability == pageMaxVariab:
                        x_data.append(frame)
                        timeData.append(time)
            x_dataFrame.append(x_data.copy())
            timeY1.append(timeData.copy())

        # Plotar o gráfico Frame vs. Tempo
        for i in range(0, len(x_dataFrame), 6):
            plt.plot(x_dataFrame[i], timeY1[i], marker='o', linestyle='-', label=f'Conjunto Variabilidade {i+1}')
        
        plt.title('Múltiplos Plots: Frame vs. Time')
        plt.xlabel('Frame')
        plt.ylabel('Time')
        plt.legend()
        plt.grid(True)
        plt.savefig(f"FrameTime{eachCase}.png")

        fig = plt.figure(figsize=(1280/96, 720/96))
        
        # Gera dados para plotagem de variabilidade vs tempo
        for frameVal in frameValues:
            timeData, x_data = [], []
            for result in resultList:
                for entry in result:
                    faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
                    if pageListSize == eachCase and frameVal == frame:
                        x_data.append(pageMaxVariab)
                        timeData.append(time)
            x_dataPageMaxVariab.append(x_data.copy())
            timeY2.append(timeData.copy())
        
        # Plotar o gráfico Variabilidade vs. Tempo
        for i in range(0, len(x_dataPageMaxVariab), 4):
            plt.plot(x_dataPageMaxVariab[i], timeY2[i], marker='o', linestyle='-', label=f'Conjunto Frame {i+1}')
        
        plt.title('Múltiplos Plots: Page Variability vs. Time')
        plt.xlabel('Variability')
        plt.ylabel('Time')
        plt.legend()
        plt.grid(True)
        plt.savefig(f"VariabilityTime{eachCase}.png")

def generate_clock_display(clock, pointer):
    clock_display = "+---+---+\n"
    
    for i in range(len(clock)):
        if pointer == i:  # Check if pointer is at the first column of the current row
            clock_display += f"-->|{clock[i,0]} | {clock[i,1]} |\n"
        else:
            clock_display += f"|{clock[i,0]} | {clock[i,1]} |\n"
        
        clock_display += "+---+---+\n"
    
    # Adding the * marker
    clock_display += "   *\n"
    
    return clock_display