class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        let = []
        n_let = 0
        for i in s:
            if i in let:
                let = let[let.index(i) + 1:]
            let.append(i)
            n_let = max(n_let, len(let))
        return n_let