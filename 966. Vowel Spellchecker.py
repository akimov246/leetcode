class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        vowels = 'aeiou'

        def replace_vowels(word: str):
            return ''.join(char if char not in vowels else '*' for char in word)

        words = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            word_lower = word.lower()
            words_cap.setdefault(word_lower, word)
            words_vow.setdefault(replace_vowels(word_lower), word)

        def solve(query: str):
            if query in words:
                return query
            query = query.lower()
            if result := words_cap.get(query, ''):
                return result
            return words_vow.get(replace_vowels(query), '')

        answer = []

        for q in queries:
            answer.append(solve(q))

        return answer

print(Solution().spellchecker(wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))