class Solution:
    def trap(self, height: List[int]) -> int:
        vol=0
        leftmax,rightmax,left,right=height[0],height[len(height)-1],0,len(height)-1

        while left<right:
            if height[left]<=height[right]:
                if height[left]<=leftmax:
                    vol+=(leftmax-height[left])

                else:
                    leftmax=height[left]

                left+=1
            else:
                if height[right]<=rightmax:
                    vol+=(rightmax-height[right])

                else:
                    rightmax=height[right]

                right-=1
            # print(vol)
            

        return vol
