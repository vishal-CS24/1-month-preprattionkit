def filledOrders(order, k):
    order.sort()
    ans = 0
    for x in order:
        if x <= k:
            ans += 1
            k -= x
        else:
            break
    return ans
