from collections import defaultdict, Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        counter = Counter(chars)
        for word in words:
            curr_word = defaultdict(int)
            good = True
            for char in word:
                curr_word[char] += 1
                if char not in counter or curr_word[char] > counter[char]:
                    good = False
                    break
            if good:
                res += len(word)
        return res