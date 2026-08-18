class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row = [1]
        # for i in range(rowIndex):
        #     next_row = [0] * (len(row) + 1)
        #     for j in range(len(row)):
        #         next_row[j] += row[j]
        #         next_row[j+1] += row[j]
        #     row = next_row
        # return row 
        res = [[1]]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+ 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res[rowIndex]