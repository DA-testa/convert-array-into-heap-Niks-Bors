# python3
def sift_down(data, swaps, i):
    n= len(data)
    maz=i
    labais=(2*i)+2
    kreisais=(2*i)+1
    if kreisais<n and data[kreisais]<data[maz]:
        maz=kreisais
    if labais<n and data[labais]<data[maz]:
        maz=labais
    if maz !=i:
        swaps.append((i, maz))
        data[i], data[maz] = data[maz],data[i]
        sift_down(data, swaps, maz)
    return swaps

def build_heap(data):
    swaps = []
    n = len(data) 
    for i in range(n//2-1,-1,-1):
        sift_down(data, swaps, maz)
    return swaps

    
    

    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    


def main():
    text = input("Ievadat: ")
    if "I" in text:
        n = int(input())
        
        data= list(map(int,input().split()))
       
    elif "F" in text: # ja lietotājs ir ievadījis F, tad nolasa mezglu daudzumu un vecāku masīvu no faila, pēcāk pāŗbauda vai faila nosaukumā nav a burts
        fileName = str(input())
        try:
            fileName="test/" + str(fileName)
            with open(fileName,'r') as jaunsf:
                 n = int(jaunsf.readline())
            return
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
        assert len(data) == n

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))
    

    # checks if lenght of data is the same as the said lenght
    

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for swap in swaps:
        print(*swap)

if __name__ == "__main__":
    main()
