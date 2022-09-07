class Solution:

    def longestCommonPrefix(strings):
        
        prefixCounts = {}
        
        for string in strings:
            if string[0] not in prefixCounts:
                prefixCounts[string[0]] = 1
            else:
                prefixCounts[string[0]] += 1
        
        ans = "a"
        
        for prefix in prefixCounts:
            if prefixCounts[prefix] > prefixCounts[ans]:
                ans = prefix

        print("prefixCounts: ", prefixCounts)
        print("CommonPrefix: ", ans)

        return 0


strings = []
            
while True:
    string = input("Enter a string: ")

    if len(string) > 0:
        strings.append(string)
    else:
        break

Solution.longestCommonPrefix(strings)
