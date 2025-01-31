from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, (list, tuple)):
            raise TypeError("Input must be a list or tuple of strings")

        if not strings:
            return ""

        if not all(isinstance(s, str) for s in strings):
            raise TypeError("All elements must be strings")

        if len(strings) == 1:
            return strings[0]

        shortest = min(strings, key=len)

        for i in range(len(shortest)):
            char = strings[0][i]

            if any(s[i] != char for s in strings[1:]):
                return shortest[:i]

        return shortest



if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
