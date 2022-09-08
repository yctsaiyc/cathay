class Solution:

    def longestCommonPrefix(strings):
        
        commonPrefix = ""

        # 檢查第一個字串的第i個字元
        for i, char in enumerate(strings[0]):
        
            # 和其他字串的第i個字元比對
            for string in strings:
                
                # 若有字串無第i個字元
                # 或有相異字元出現，則回傳
                if i == len(string) or char != string[i]:
                    return commonPrefix

            # 若無相異字元，代表所有字串的第i個字元都相同，即為common prefix
            commonPrefix += char

        return commonPrefix
            


strings = []
while True:
    string = input("Enter a string: ")
    if len(string) == 0:
        break
    strings.append(string)
print("Longest common prefix: ", Solution.longestCommonPrefix(strings))
