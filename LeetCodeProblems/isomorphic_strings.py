from typing import List


class Solution:
    def _recreateTWithIsomorphicMap(self, isomorphicMap, s):
        recreateT = ''
        for letter in s:
            recreateT += isomorphicMap[letter]
        return recreateT

    def _createIsomorphicMap(self, s: str, t: str):
        isomorphicMap = {}
        for (i, letter) in enumerate(s):
            isomorphicMap[letter] = t[i]
        return isomorphicMap

    def isIsomorphic(self, s: str, t: str) -> bool:
        assert len(s) == len(t), "Input strings not the same length"
        isomorphicMap = self._createIsomorphicMap(s, t)
        recreateT = self._recreateTWithIsomorphicMap(isomorphicMap, s)

        if recreateT != t:
            return False

        isomorphicMap = self._createIsomorphicMap(t, s)
        recreateS = self._recreateTWithIsomorphicMap(isomorphicMap, t)
        if recreateS != s:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()

    # test 1
    result1 = solution.isIsomorphic('add', 'egg')
    assert (result1 == True), 'first test should be true'

    # test 2
    result2 = solution.isIsomorphic('age', 'egg')
    assert (result2 == False), 'second test should be false'

    # test 3
    try:
        result3 = solution.isIsomorphic('ages', 'egg')
    except:
        print('should throw assert')
