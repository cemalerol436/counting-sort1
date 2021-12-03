# it counts and return each element and shows it in an array to sort the list.

def countingSort(arr):

    big_number = max(arr)
    listr = []

    #Loop creates a list of zeros according to biggest number

    for number in range(big_number+1):
        listr.append(0)

    #Loop sends elements where they belong.

    for count in arr:
        listr[count]=listr[count]+1
        f_result = listr[0:(big_number+1)]

    return print(f_result)

#given array could include some integers.

given_array = [0,1,86,45,20,3,2,1,56,85,0,58,68,56,80]

countingSort(given_array)
