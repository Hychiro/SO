import numpy as np
import random
import time as t
from clock_algorithm import startClock

# Função para rodar a simulação e gerar os dados
def run_simulation(pageListCasesOfAnalysis, variabilityOfPages, frameValues):
    random.seed(10)
    resultList = []

    for eachCase in pageListCasesOfAnalysis:
        pageListSize = eachCase
        print(f"pageListSize {pageListSize}")
        perInter = []

        for eachvariability in variabilityOfPages:
            pageMaxVariab = int(eachvariability * pageListSize)
            pageList = [random.randint(1, pageMaxVariab) for _ in range(pageListSize)]
            
            for eachFrameVal in frameValues:
                frame = int(eachFrameVal * eachCase)
                clock = np.zeros((frame, 2))
                timeBefore = t.time()
                faultR, foundR = startClock(pagelist=pageList, clock=clock, frame=frame)
                timeAfter = t.time()
                
                perInter.append([faultR, foundR, eachFrameVal, pageListSize, eachvariability, float(timeAfter - timeBefore)])

        resultList.append(perInter)

    return resultList
