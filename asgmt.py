def computepay(h,r):
    if h > 40:
        pa = 40 * r + (h-40)*1.5*r
    else:
        pa = h * r
    return pa

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
p = computepay(h,r)

print("Pay",p)
