class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # base case
        if (len(s) == 0):
            return True

        # get first letter from s
        letter = s[0]

        # check if letter is in t
        if (letter in t):
            # find index of letter in t
            for i in range(len(t)):
                if (letter == t[i]):
                    # check the next letter in S and the rest of the T string
                    return self.isSubsequence(s[1:], t[i+1:])

        return False


if __name__ == "__main__":
    solution = Solution()

    # test 1
    result1 = solution.isSubsequence(
        'abac', 'ahbbgdac')
    print(result1)
    assert (result1 == True), 'first test should be true'

    # test 2
    result2 = solution.isSubsequence('axc', 'ahbgdc')
    print(result2)
    assert (result2 == False), 'second test should be false'

    # test 3
    result3 = solution.isSubsequence('acb', 'ahbgdc')
    print(result3)
    assert (result3 == False), 'third test should be false'

    # test 4
    result4 = solution.isSubsequence('aaaaaa', 'bbaaaa')
    print(result4)
    assert (result4 == False), 'fourth test should be false'
