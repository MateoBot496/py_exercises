def longestSubstring(str) -> int:
    window = set()
    longest = 0
    l = 0

    #USAREMOS R Y L COMO POINTERS DE LA VENTANA     

    for r in range(len(str)):   

        while str[r] in window: #MIENTRAS HAYA UN S EN WINDOW MOVEMOS EL LEFT +1
            window.remove(str[l])
            l += 1

        window.add(str[r])
        longest = max(longest, r - l +1)


    return longest






string = "asdfagnbfhgdgdfh"
print(longestSubstring(string))