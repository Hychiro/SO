from plotting import generate_clock_display
import time 
# Função para verificar se a página já está presente no relógio
def containsPage(page, clock):
    for i in range(len(clock)):
        if clock[i, 0] == page:
            return True
    return False

# Função para atualizar o relógio e lidar com faltas de página
def updateClock(page, clock, clockFrame, pointer, fault, found):
    if containsPage(page=page, clock=clock):
        for i in range(len(clock)):
            if clock[i, 0] == page:
                clock[i, 1] = 1
        found += 1
        return pointer, clock, fault, found
    else:
        fault += 1
        if clock[pointer, 1] == 0:
            clock[pointer, 0] = page
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            return pointer, clock, fault, found
        else:
            clock[pointer, 1] = 0
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            return updateClock(page=page, clock=clock, clockFrame=clockFrame, pointer=pointer, fault=fault, found=found)
        
def updateClock(page, clock, clockFrame, pointer, fault, found):
    if containsPage(page=page, clock=clock):
        for i in range(len(clock)):
            if clock[i, 0] == page:
                clock[i, 1] = 1
        found += 1
        
        return pointer, clock, fault, found
    else:
        fault += 1
        if clock[pointer, 1] == 0:
            clock[pointer, 0] = page
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            
            return pointer, clock, fault, found
        else:
            clock[pointer, 1] = 0
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            
            return updateClock(page=page, clock=clock, clockFrame=clockFrame, pointer=pointer, fault=fault, found=found)
        

def updateClock2(page, clock, clockFrame, pointer, fault, found):
    if containsPage(page=page, clock=clock):
        for i in range(len(clock)):
            if clock[i, 0] == page:
                clock[i, 1] = 1
        found += 1
        clock_display = generate_clock_display(clock=clock, pointer=pointer)
        print("PAGE FOUND")
        print(clock_display)
        time.sleep(1)
        return pointer, clock, fault, found
    else:
        fault += 1
        if clock[pointer, 1] == 0:
            clock[pointer, 0] = page
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            clock_display = generate_clock_display(clock=clock, pointer=pointer)
            print("PAGE NOT FOUND")
            print(clock_display)
            time.sleep(1)
            return pointer, clock, fault, found
        else:
            clock[pointer, 1] = 0
            pointer += 1
            if pointer == clockFrame:
                pointer = 0
            clock_display = generate_clock_display(clock=clock, pointer=pointer)
            print("PAGE BITR RESET")
            print(clock_display)
            time.sleep(1)
            return updateClock2(page=page, clock=clock, clockFrame=clockFrame, pointer=pointer, fault=fault, found=found)

# Função para iniciar o processo de substituição de páginas usando o algoritmo de relógio
def startClock(pagelist, clock, frame):
    pointer = 0
    fault = 0
    found = 0
    for each in pagelist:
        pointer, clock, fault, found = updateClock(page=each, clock=clock, clockFrame=frame, pointer=pointer, fault=fault, found=found)
    return fault, found

def startClockWithDisplay(pagelist, clock, frame):
    pointer = 0
    fault = 0
    found = 0
    for each in pagelist:
        pointer, clock, fault, found = updateClock2(page=each, clock=clock, clockFrame=frame, pointer=pointer, fault=fault, found=found)
    print(f"Houveram {fault} faltas sendo {frame} delas para preencher o frame do Clock")
    print(f"Isso resulta num final de {fault-frame} faltas ocorridas")
    print(f"Isso resulta num final de {found} founds ocorridos")
    return fault, found