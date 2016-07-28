class Solution(object):
    def maxEnvelopes(self, envelopes):
        if envelopes == []:
            return 0
        def noContain(a,b):
            if a[0] > b[0]:
                return 1
            if a[0] < b[0]:
                return -1
            if a[0] == b[0]:
                if a[1] > b[1]:
                    return -1
                else:
                    return 1
        envelopes.sort(noContain)
        size = len(envelopes)
        # dp = []
        dp_ = []
        for x in range(size):
            low = bisect.bisect_left(dp_, envelopes[x][1])
            # low, high = 0, len(dp) - 1
            # while low <= high:
            #     mid = (low + high) / 2
            #     if dp[mid][1] < envelopes[x][1]:
            #         low = mid + 1
            #     else:
            #         high = mid - 1
            if low < len(dp_):
                # dp[low] = envelopes[x]
                dp_[low] = envelopes[x][1]
            else:
                dp_.append(envelopes[x][1])
            # print dp
        return len(dp_)