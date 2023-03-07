# price = int(input())
# coupon_name = input()
# if coupon_name == "Cash3000":
#     price = price-3000

# if coupon_name == "Cash5000":
#     price = price-5000

# print(price)

# if written_test>=80 and coding_test==True:

R = int(input())
M = int(input())
E = int(input())
S = int(input())

if R >= 80 and M >= 80 and E >= 80 and S >= 80:
    print("Qualified")
else R, M, E, S < 0 or R, M, E, S > 100:
    print("no")
