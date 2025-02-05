class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        ls1, ls2 = len(s1), len(s2)

        if ls1 != ls2:
            return False

        count = 0

        for i in range(0, ls1):
            if s1[i] != s2[i]:
                count += 1

        if Counter(s1) != Counter(s2):
            return False

        return count == 2 or count == 0
