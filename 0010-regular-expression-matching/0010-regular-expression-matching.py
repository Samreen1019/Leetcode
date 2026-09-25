class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = whether s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                # Check if current characters match
                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                # If next pattern character is '*'
                if j + 1 < n and p[j + 1] == '*':
                    # 1. Ignore x*
                    # 2. Consume one character and keep x*
                    dp[i][j] = (
                        dp[i][j + 2] or
                        (first_match and dp[i + 1][j])
                    )

                else:
                    # Normal character or '.'
                    dp[i][j] = (
                        first_match and dp[i + 1][j + 1]
                    )

        return dp[0][0]
