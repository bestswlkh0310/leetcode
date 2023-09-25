class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        before = ""
        for i in range(len(chars) - 1):
            if before != chars[i] and str(type(chars[i])) == "<type 'unicode'>":
                before = chars[i]
            if chars[i] == chars[i + 1]:
                before = chars[i]
                chars[i + 1] = 2
            elif before == chars[i + 1]:
                chars[i + 1] = chars[i] + 1
                chars[i] = None
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == None:
                del chars[i]
            elif str(chars[i]).isdigit():
                lst = list(map(str, list(str(chars[i]))))
                del chars[i]
                for j in range(len(lst)):
                    chars.insert(i + j, lst[j])
        
        print(chars)
        return len(chars)