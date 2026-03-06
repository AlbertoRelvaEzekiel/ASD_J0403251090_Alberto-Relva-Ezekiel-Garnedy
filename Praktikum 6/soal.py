def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]<data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
unsorted = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
bubbleSort(data)

#Nomor 1
print("Nilai 5 kandidat terbaik adalah ",data[:5])
#Nomor 2
def ranking(data,unsorted) :
    i=0
    j=0
    for i in range(len(data)) :
        for j in range(len(unsorted)) :
            if i >= 5 :
                break
            elif data[i] == unsorted[j] :
                print("Peringkat ke-",i+1,"adalah kandidat ke-",j+1)
ranking(data,unsorted)
