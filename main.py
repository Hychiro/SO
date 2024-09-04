import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import pandas as pd
import time as t

random.seed(10)

def containsPage(page,clock):
    for i in range(len(clock)):
        if clock[i,0] == page:
            return True
    return False

def updateClock(page,clock,clockFrame,pointer,fault,found):
        if containsPage(page=page,clock=clock):
            for i in range(len(clock)):
                if clock[i,0] == page:
                    clock[i,1] = 1
            found = found + 1
            return pointer, clock, fault, found
        else:
            fault = fault + 1
            if clock[pointer,1] == 0:
                clock[pointer,0] = page
                pointer = pointer + 1
                if pointer == clockFrame:
                    pointer = 0
                return pointer, clock, fault, found
            else:
                # print(pointer,page)
                clock[pointer,1] = 0
                pointer = pointer + 1
                if pointer == clockFrame:
                    pointer = 0
                return updateClock(page = page,clock=clock,clockFrame=frame,pointer=pointer,fault= fault,found=found)

def startClock(pagelist,clock,frame):
     pointer = 0
     clock_display = ""
     fault = 0
     found = 0
     for each in pagelist:
        pointer, clock, fault, found = updateClock(page = each,clock=clock,clockFrame=frame,pointer=pointer,fault = fault, found=found)

    #     clock_display = generate_clock_display(clock=clock, pointer=pointer)

    #     print(clock_display)
    #  print(f"Houveram {fault} faltas sendo {frame} delas para preencher o frame do Clock")
    #  print(f"Isso resulta num final de {fault-frame} faltas ocorridas")
    #  print(f"Isso resulta num final de {found} founds ocorridos")
     return fault, found


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



frame = 3
pageListSize = 60
clock = np.zeros((frame,2))

exemple = [6, 3, 6, 3, 2, 5, 1, 6]
pageList = [random.randint(1, 6) for _ in range(pageListSize)]
# print(pageList)
startClock(pagelist=exemple,clock=clock,frame=frame)

pageListCasesOfAnalysis = [100,500,1000]

variabilityOfPages = np.arange(0.1, 5.1, 0.1)
frameValues = np.arange(0.05, 1.05, 0.05)
count1 = 0
resultList = []
while count1 < 1:
    perInter = []
    for eachCase in pageListCasesOfAnalysis:
        pageListSize = eachCase
        print(f"pageListSize {pageListSize}")

        for eachvariability in variabilityOfPages:
            pageMaxVariab = int(eachvariability*pageListSize)
            pageList = [random.randint(1, pageMaxVariab) for _ in range(pageListSize)]
            for eachFrameVal in frameValues:
                frame = int(eachFrameVal*eachCase)
                clock = np.zeros((frame,2))
                timeBefore = t.time()
                faultR, foundR= startClock(pagelist=pageList,clock=clock,frame=frame)
                timeAfter = t.time()
                
                perInter.append([faultR, foundR, eachFrameVal, pageListSize, eachvariability, float(timeAfter - timeBefore) ])
    resultList.append(perInter)
    count1=count1+1

# df = pd.DataFrame({'faultR':resultList[0,1], 'foundR':resultList, "eachFrameVal": resultList, "pageListSize":resultList, 'eachvariability':resultList})
# df.to_csv('out.csv', index=False) 
figures = []
for eachCase in pageListCasesOfAnalysis:
    fig = plt.figure(figsize = (1280/96, 720/96))
    ax = fig.add_subplot(111, projection='3d')

    # Filter data for the current pageListSize
    x_data = []
    y_data = []
    z_data = []
    dz = []
    dz2 = []
    for result in resultList:
        for entry in result:
            faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
            if pageListSize == eachCase:
                x_data.append(frame)
                y_data.append(pageMaxVariab)
                z_data.append(0)  # Base of each bar is zero
                dz.append(faultR/pageListSize)
                dz2.append(foundR/pageListSize)
    # Convert lists to numpy arrays for bar3d plotting
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    z_data = np.array(z_data)
    dz = np.array(dz)

    # Set width and depth of the bars
    x_width =  0.05
    y_depth =  0.1

    # Plot the bars
    ax.bar3d(x_data, y_data, z_data, x_width, y_depth, dz, shade=True)

    # Set axis labels
    ax.set_xlabel('Frame')
    ax.set_ylabel('Max Page Variability')
    ax.set_zlabel('Fault Rate')

    # Title for each subplot based on the pageListSize
    ax.set_title(f'3D Graph for Fault Rate by Page List Size = {eachCase}')

    figures.append(fig)

    fig = plt.figure(figsize = (1280/96, 720/96))
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(y_data, x_data, z_data, y_depth,x_width, dz2, shade=True)

    # Set axis labels
    ax.set_ylabel('Frame')
    ax.set_xlabel('Max Page Variability')
    ax.set_zlabel('Found Rate')

    ax.set_title(f'3D Graph for Found Rate by Page List Size = {eachCase}')

    figures.append(fig)

# Show all figures
figures[0].savefig('100Fault.png')
figures[1].savefig('100Found.png')
figures[2].savefig('500Fault.png')
figures[3].savefig('500Found.png')
figures[4].savefig('1000Fault.png')
figures[5].savefig('1000Found.png')
# figures[6].savefig('2000Fault.png')
# figures[7].savefig('2000Found.png')



figures = []
for eachCase in pageListCasesOfAnalysis:
    fig = plt.figure(figsize = (1280/96, 720/96))
    # Filter data for the current pageListSize
    x_dataFrame = []
    
    x_dataPageMaxVariab = []
    timeY1 = []
    timeY2 = []

   
    for _ in variabilityOfPages:
        timeData = []
        x_data = []
        for result in resultList:
            for entry in result:
                faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
                if pageListSize == eachCase and _ == pageMaxVariab:
                    x_data.append(frame)
                    timeData.append(time)
                    print(x_data,timeData)          
        x_dataFrame.append(x_data.copy())
        timeY1.append(timeData.copy())

 
    for _ in frameValues:
        timeData = []
        x_data = []
        for result in resultList:
            for entry in result:
                faultR, foundR, frame, pageListSize, pageMaxVariab, time = entry
                if pageListSize == eachCase and _ == frame:
                    x_data.append(pageMaxVariab)
                    timeData.append(time)
        x_dataPageMaxVariab.append(x_data.copy())
        timeY2.append(timeData.copy())
    # Convert lists to numpy arrays for bar3d plotting
    

    # Criar o gráfico 2D
    for i in range(0,len(x_dataFrame),6):
        plt.plot(x_dataFrame[i], timeY1[i], marker='o', linestyle='-', label=f'Conjunto Variabilidade {i+1}')

    # Adicionar título e rótulos aos eixos
    plt.title('Múltiplos Plots: Frame vs. Time')
    plt.xlabel('Frame')
    plt.ylabel('Time')
    plt.legend()
    # Adicionar legenda

    # Exibir a grade
    plt.grid(True)
    plt.savefig(f"FrameTime{eachCase}.png")

    # Mostrar o gráfico

    fig = plt.figure(figsize = (1280/96, 720/96))
   
    for i in range(0,len(x_dataPageMaxVariab),4):
        plt.plot(x_dataPageMaxVariab[i], timeY2[i], marker='o', linestyle='-', label=f'Conjunto Frame {i+1}')

    # Adicionar título e rótulos aos eixos
    plt.title('Múltiplos Plots: Page Variability vs. Time')
    plt.xlabel('Variability')
    plt.ylabel('Time')

    # Adicionar legenda
    plt.legend()

    # Exibir a grade
    plt.grid(True)
    plt.savefig(f"VariabilityTime{eachCase}.png")
    # Mostrar o gráfico
