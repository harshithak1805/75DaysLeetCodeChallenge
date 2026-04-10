class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]  # first row is always [1]

        for i in range(1, numRows):
            prev = res[-1]  # previous row
            row = [1]       # first element is 1
            # middle elements = sum of two numbers above
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)   # last element is 1
            res.append(row)

        return res