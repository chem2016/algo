


def kDistinctCharacters(s, k):
        left = 0
        cnt = {}
        ans = 0
        
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            while left <= i and len(cnt) >= k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            
            if len(cnt) == k - 1 and left > 0 and s[left - 1] not in cnt:
                ans += left
            print("ans: ", ans)
        return ans

s = 'abcabcabcabc'
k = 3

result = kDistinctCharacters(s, k)
print(result)