class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        min_exist = [float('inf')] *26  # the first time the character appear
        max_exist = [float('-inf')] *26  # the last time
        #two lists for every character in the alphabet
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            min_exist[index] = min(min_exist[index], i)
            max_exist[index] = max(max_exist[index], i)
        # put in data to the lists
        count = 0
        for i in range(26):
            if min_exist[i] == float('inf') or max_exist[i] == float('-inf'):
                continue
            # the character didn't show up in the string
            between = set()

            for j in range(min_exist[i]+1, max_exist[i]):
                between.add(s[j])
            # add characters between the first appear and the last appear
            
            count += len(between)
            # calclulate the count 
        return count
