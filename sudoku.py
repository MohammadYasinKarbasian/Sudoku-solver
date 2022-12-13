import numpy as np

RESTART = 5
POPULATION_COUNT = 400
GENERATION_COUNT = 300
MUTATION_PROBABILITY = 0.8
PATH = './sample1_easy.txt'

def group_finder(i,j):
    return int(i/3)*3+int(j/3)

def group_base_finder(i):
    return int(i/3)*3,int(i%3)*3

def fitness(sudo):
    total = 0
    for row in range(9):
        counts = np.bincount(sudo[row])
        for i in counts:
            if i>1:total += i-1
    for column in range(9):
        counts = np.bincount(sudo[:,column])
        for i in counts:
            if i>1:total += i-1    
    return 108-total        

def fill(original_sudo,lock):
    sudo = original_sudo.copy()
    for index in range(9):
        diversity = np.arange(1,10)
        filled_div = []
        row,col = group_base_finder(index)
        for i in range(9):
            rowT = row + int(i/3)
            colT = col + int(i%3)
            if lock[rowT][colT] == 1: filled_div.append(sudo[rowT][colT])
        diversity = np.setdiff1d(diversity,filled_div)
        diversity = np.random.permutation(diversity)
        done=0
        for i in range(9):
            rowT = row + int(i/3)
            colT = col + int(i%3)
            if lock[rowT][colT] == 0: 
                sudo[rowT][colT]=diversity[done]
                done += 1
    return sudo

while(RESTART>0):
    sudoko = np.zeros((9,9),dtype=np.int)
    locked = np.zeros((9,9),dtype=np.int)
    with open(PATH) as fd:
        Data = fd.readlines()
        for index in range(9):
            sudoko[index] = np.array(list(map(int,Data[index].split())))
            for i in range(9):
                if sudoko[index][i] != 0:locked[index][i] = 1
    #initial population
    population = np.zeros((POPULATION_COUNT,9,9),dtype=np.int)
    for counter in range(POPULATION_COUNT):
        population[counter] = fill(sudoko,locked)
    pop_fit = np.zeros((POPULATION_COUNT),dtype=np.int)
    for counter in range(POPULATION_COUNT):
        pop_fit[counter] = fitness(population[counter])
    #next generations
    for generation in range(1,GENERATION_COUNT):
        #stop condition
        max_indice = np.argmax(pop_fit)
        max_fitness = pop_fit[max_indice]
        print(f'In generation {generation} MAX was {max_fitness}')
        if max_fitness == 108:
            print('Wow we find solution:\n')
            print(population[max_indice])
            exit(0)
        #parent selection
        parent_num = int(POPULATION_COUNT/2)
        parents = np.random.choice(a=np.arange(POPULATION_COUNT),size=(parent_num*2),replace=True,p=pop_fit/np.sum(pop_fit))
        #generate childs
        childs = np.zeros((parent_num,9,9),dtype=np.int)
        for index in range(0,parent_num):
            mom = index*2
            father = index*2+1
            diverse = np.arange(0,9)
            fatherNum = np.random.randint(1,8)
            fatherChoice = np.random.choice(diverse,size=fatherNum,replace=False)
            for section in range(9):
                row,col = group_base_finder(section)
                if section in fatherChoice:
                    for i in range(9):
                        rowT = row + int(i/3)
                        colT = col + int(i%3)
                        childs[index][rowT][colT] = population[father][rowT][colT]
                else:
                    for i in range(9):
                        rowT = row + int(i/3)
                        colT = col + int(i%3)
                        childs[index][rowT][colT] = population[mom][rowT][colT]
            #mutation
            if np.random.rand() < MUTATION_PROBABILITY:
                section = np.random.randint(0,9)
                row,col = group_base_finder(section)
                stables = []
                for iter in range(9):
                    row1 = row+int(iter/3)
                    col1 = col+int(iter%3)
                    if locked[row1][col1] : stables.append(iter)
                div = np.setdiff1d(np.arange(9),stables)
                data1,data2 = np.random.choice(div,size=2,replace=False)
                row1 = row+int(data1/3)
                col1 = col+int(data1%3)
                row2 = row+int(data2/3)
                col2 = col+int(data2%3)
                temp = childs[index][row1][col1]
                childs[index][row1][col1] = childs[index][row2][col2]
                childs[index][row2][col2] = temp
        child_fit = np.zeros((parent_num),dtype=np.int)
        for counter in range(parent_num):
            child_fit[counter] = fitness(childs[counter])

        #make population update
        temp_population = np.concatenate((population,childs))
        temp_pop_fit = np.concatenate((pop_fit,child_fit))

        #next generation selection
        new_generation = np.argsort(temp_pop_fit)[::-1][:POPULATION_COUNT]
        for i in range(POPULATION_COUNT):
            population[i] = temp_population[new_generation[i]]
            pop_fit[i] = temp_pop_fit[new_generation[i]]

    max_indice = np.argmax(pop_fit)
    max_fitness = pop_fit[max_indice]
    print(f'In generation {generation} MAX was {max_fitness}')
    print(f'sorry but in our {GENERATION_COUNT} generation we don\'t find answer\n')
    RESTART -= 1