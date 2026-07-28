def solve():
    V = int(input())
    W= int(input())
    
   
    if not (W >= 2 and W % 2 == 0 and V< W):
        print("INVALID INPUT")
        return
    
    
    
    FW = (W- 2 * V) / 2
    TW = V- FW
    
    if FW < 0 or TW< 0 or FW != int(FW) or TW != int(TW):
        print("INVALID INPUT")
        return
    
    TW = int(TW)
    FW = int(FW)
    
    print(f"TW ={TW} FW={FW}")

solve()