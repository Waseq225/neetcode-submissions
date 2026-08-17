class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        result = []
        for start, end in queries:
            count = 0
            for i in range(start, end + 1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count += 1
            result.append(count)
        return result