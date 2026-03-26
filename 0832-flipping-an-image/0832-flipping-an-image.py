class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        j=0
        for i in image:
            image[j]=i[::-1]
            j+=1
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j]^=1
        return image

        



