def fibonachicken(n):
    fibo,ans = [1,1],0
    while fibo[-1] < n:
        fibo+= [fibo[-1]+fibo[-2]]
    i = -2
    while n != 0:
        if fibo[i] <= n:
            n -= fibo[i]
            ans += fibo[i-1]
        else:
            i -= 1
    return ans
