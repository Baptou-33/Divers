from random import *
from time import *

# Inputs
number_of_data = int(input("Please enter the lenght of the random list to be sorted : "))
min_random = int(input("Please enter the number min : "))
max_random = int(input("Please enter the number max : "))

# One list for all the algorithms to be equal
First_list = []
List = []

#Change the common list
def RNG():
    First_list.clear()
    for rng in range(1, number_of_data):
        First_list.append(randint(min_random, max_random))
        if number_of_data > 100000 and rng % (round(number_of_data/50)) == 0:
            print("Creating list : ", 100 * rng / number_of_data, "%")
    print("\nList to sort : ", First_list)



# Sorting algorithms
def Bauble_sort():
    for list_index in range(len(List)):
        is_sorted = True
        for list_index2 in range(len(List) - list_index - 1):
            if List[list_index2 + 1] < List[list_index2]:
                List[list_index2 + 1], List[list_index2] = List[list_index2], List[list_index2 + 1]
                is_sorted = False
        if is_sorted :
            break

def Selection_sort():
    for list_index2 in range(len(List)) :
        Memory = list_index2
        for list_index in range(list_index2 + 1, len(List)):
            if List[list_index] < List[Memory]:
                Memory = list_index
        List[Memory], List[list_index2] = List[list_index2], List[Memory]

def Insertion_sort():
    for list_index in range(1, len(List)):
        swap_memory = List[list_index]
        Memory = list_index - 1
        while Memory >= 0 and List[Memory] > swap_memory:
            List[Memory + 1] = List[Memory]
            Memory -= 1
        List[Memory + 1] = swap_memory



#All the actions you can do
Actions = ['RNG()', 'run("Bauble_sort()")', 'run("Selection_sort()")', 'run("Insertion_sort()")']

#Check if the List is realy sorted
def Check_list(L):
    for check in range(len(L) - 1):
        if L[check + 1] < L[check]:
            return False
            break
    return True

#Test all the algorithms
def All():
    print("")
    for z in range(1, len(Actions)):
        eval(Actions[z])

#Take the runnig time of the algorithm
def run(algorithm):
    List.clear()
    for reset in range(len(First_list)):
        List.append(First_list[reset])
    start_time = perf_counter()
    eval(algorithm)
    end_time = perf_counter()
    execution_time = end_time - start_time
    print(algorithm, execution_time, ", sorted=", Check_list(List), "" if Check_list(List) else List)



#Main code
RNG()
while True :
    act = int(input("\n-1=Test all the algorithms\n0=New list to sort\n1=Bauble sort\n2=Selection sort\n3=Insertion sort\n4=        \nChoose your next action : "))
    if act == -1:
        All()
    else:
        eval(Actions[act])
