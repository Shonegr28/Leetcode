def longestCommonPrefix(strs):
    prefix = strs[0]

    for i in range(len(prefix)):
        for s in strs:
            
            if i == len(s) or s[i] != prefix[i]:
                #print(i)
                return prefix[:i]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
