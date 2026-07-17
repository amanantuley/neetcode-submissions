class Solution:
    def validWordSquare(self, words):

        n = len(words)

        for i in range(n):
            for j in range(len(words[i])):

                # boundary check
                if j >= n or i >= len(words[j]):
                    return False

                # compare row vs column
                if words[i][j] != words[j][i]:
                    return False

        return True
