class EmailParser:

    def search(self, s):
        results = []
        n = len(s)
        bitmask = 0
        i = 0
        while i+5 < n:
            if s[i + 5].isdigit():
                bitmask ^= 1
            else:
                bitmask = 0
                i += 6
                continue
            if s[i + 4].isdigit():
                bitmask ^= 1 << 1
            else:
                bitmask = 0
                i += 5
                continue
            if s[i + 3].isdigit():
                bitmask ^= 1 << 2
            else:
                bitmask = 0
                i += 4
                continue
            if s[i + 2].isdigit():
                bitmask ^= 1 << 3
            else:
                bitmask = 0
                i += 3
                continue
            if s[i + 1].isdigit():
                bitmask ^= 1 << 4
            else:
                bitmask = 0
                i += 2
                continue
            if s[i].isdigit():
                bitmask ^= 1 << 5
            else:
                bitmask = 0
                i += 1
                continue

            results.append(s[i:i+6])
            i +=1

        return results



