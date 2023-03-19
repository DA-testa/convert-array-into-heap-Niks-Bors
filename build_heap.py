# python3
def sift_down(data, swaps, i):# šī funkcija izmantojot rekursiju maina vietās elementus ar indeksu i, liidz tas sasniedz apakšu
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
    

def build_heap(data): # šī funkcija ņem un izveidoto koku izmantojot sift_ down pārliek elementus tā, lai visi bērni būtu lielāki par vecākiem
    swaps = []
    n = len(data) 
    for i in range(n//2-1,-1,-1):
        sift_down(data, swaps, i)
    return swaps

    
    

    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    


def main(): # pārbauda vai ir I va F
    text = input("Ievadat: ")
    if "I" in text:
        n = int(input())
        
        data= list(map(int,input().split()))
        assert len(data) == n
    elif "F" in text: # ja lietotājs ir ievadījis F
        print("Input filename please: ")

        fileName = input()
        path = "./test/"
        with open(path + fileName, 'r') as jaunsf:
            n = int(jaunsf.readline())
            data = list(map(int, jaunsf.readline().split()))
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
        

    # input from keyboard
    
    
    

    # checks if lenght of data is the same as the said lenght
    

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
