class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        ln=len(flowerbed)
        for i in range(ln):
            if flowerbed[i]==0:
                if i==0 or flowerbed[i-1]==0:
                    left=True
                else:
                    left=False
                
                if i==ln-1 or flowerbed[i+1]==0:
                    right=True
                else:
                    right=False


                if left and right:
                    flowerbed[i]=1
                    count+=1
                    if count>=n:
                        return True
        
        if count>=n:
            return True
        else:
            return False
