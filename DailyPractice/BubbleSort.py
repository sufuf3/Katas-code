def bubble_sort(list):
    for i in range(0,len(list)-1): #有n-1回合(n為數字個數)
        for j in range(0,len(list)-1-i): #每回合進行比較的範圍
            if list[j] > list[j+1]: #是否需交換
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
        print("pass",i+1,": ", list)
    for i in list:
        print(str(i), end=" ")
    print(" ")

list = [2, 4, 1, 7, 5, 6, 9, 8]
bubble_sort(list)
