class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain=[]
        n = int(input())
        for i in range(n):
            x=int(input())
            gain.append(x)
        ans=0
        highest=-101
        for j in gain:
            ans += j
            if ans > highest:
                highest=ans
        return highest
      