def sockMerchant(n, ar):
    pairs_count = [ar.count(i) // 2 for i in set(ar)]
    return sum(pairs_count)
