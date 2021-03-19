from typing import List


def main():
    str1 = "barfoofoobarthefoobarman"
    words = ["foo", "bar", "the"]

    print(findSubstring(str1, words))


def findSubstring(s: str, words: List[str]) -> List[int]:
    result = []
    if s == None or words == None or len(words) == 0 or s.strip() == "":
        return result

    wordLen = len(words[0])
    total = wordLen * len(words)

    i = 0
    while i <= len(s):
        m = i
        tmpWords = words.copy()
        while m <= len(s):
            index = s[m:m + wordLen]
            if index in tmpWords:
                tmpWords.remove(index)
                print(index)
                m = m + wordLen
            else:
                if len(tmpWords) == 0:
                    result.append(i)
                    i = i + total
                    break
                else:
                    i = i + 1
                    break
        print("i-- " + str(i))

    return result


if __name__ == '__main__':
    main()
