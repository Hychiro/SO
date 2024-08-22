
import numpy as np
import random

def containsPage(page,clock):
    for i in range(len(clock)):
        if clock[i,0] == page:
            return True
    return False
def updateClock(page,clock,clockFrame,pointer,fault):
        if containsPage(page=page,clock=clock):
            for i in range(len(clock)):
                if clock[i,0] == page:
                    clock[i,1] = 1
            return pointer, clock, fault
        else:
            fault = fault + 1
            if clock[pointer,1] == 0:
                clock[pointer,0] = page
                pointer = pointer + 1
                if pointer == clockFrame:
                    pointer = 0
                return pointer, clock, fault
            else:
                print(pointer,page)
                clock[pointer,1] = 0
                pointer = pointer + 1
                if pointer == clockFrame:
                    pointer = 0
                return updateClock(page = page,clock=clock,clockFrame=frame,pointer=pointer,fault= fault)

def startClock(pagelist,clock,frame):
     pointer = 0
     clock_display = ""
     fault = 0
     for each in pagelist:
        pointer, clock, fault = updateClock(page = each,clock=clock,clockFrame=frame,pointer=pointer,fault= fault)

        clock_display = generate_clock_display(clock=clock, pointer=pointer)

        print(clock_display)
     print(f"Houveram {fault} faltas sendo {frame} delas para preencher o frame do Clock")
     print(f"Isso resulta num final de {fault-frame} faltas ocorridas")


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



frame = 5
pageListSize = 60
clock = np.zeros((frame,2))

# exemple = [6, 3, 6, 3, 2, 5, 1, 6]
pageList = [random.randint(1, 6) for _ in range(pageListSize)]
# print(pageList)
startClock(pagelist=pageList,clock=clock,frame=frame)

