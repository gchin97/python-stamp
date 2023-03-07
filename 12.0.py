# price = int(input())
# coupon_name = input()
# if coupon_name == "Cash3000":
#     price = price-3000

# if coupon_name == "Cash5000":
#     price = price-5000

# print(price)

# if written_test>=80 and coding_test==True:

- 퀴즈


R, M, E, S = map(int, input().split())

if 0<R=<100, and 0<M=<100, and 0<E=<100, and 0<S=<100:
    Average = (R+M+E+S)/4
    if Average>=80:
        print("yes", Average)
    else: 
        print("no")
else: 
    print("no")
