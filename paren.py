class Solution:
    def isValid(string):
        
        # 檢查字串的長度(constraints_1)
        if len(string) < 1 or len(string) > 10000:
            return False
        
        # 記錄未關的括號
        openBrackets = []

        for char in string:
            
            # 若為左括號則記下來
            if char in ["(", "[", "{"]:
                openBrackets.append(char)
            
            # 若為右括號
            elif char in [")", "]", "}"]:
                
                # 檢查是否有未關之左括號
                if len(openBrackets) == 0:
                    return False
                
                # 檢查是否有依照順序
                if ( openBrackets[-1] == "(" and char == ")" ) or ( openBrackets[-1] == "[" and char == "]" ) or ( openBrackets[-1] == "{" and char == "}" ):
                    openBrackets = openBrackets[:-1]

                else:
                    return False
            
            # 剩餘非括號字元無效: 不符constraints_2
            else:
                return False
        
        # 若無未關閉之括號，則該字串有效
        if len(openBrackets) == 0:
            return True

while True:

    string = input("Enter a string: ")
    
    if Solution.isValid(string):
        print("Valid")
    
    else:
        print("Invalid")
