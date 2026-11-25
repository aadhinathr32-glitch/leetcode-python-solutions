class Solution:
    def countOfSubstrings(self, word, k):
        def atMost(k):
            if k < 0:
                return 0

            vowels = set("aeiou")
            last = {v: -1 for v in vowels}

            left = 0
            consonants = 0
            result = 0

            for right in range(len(word)):
                if word[right] in vowels:
                    last[word[right]] = right
                else:
                    consonants += 1

                while consonants > k:
                    if word[left] not in vowels:
                        consonants -= 1
                    left += 1

                if all(pos >= left for pos in last.values()):
                    first_vowel = min(last.values())
                    result += first_vowel - left + 1

            return result

        return atMost(k) - atMost(k - 1)
