# # 변수 만들기
# x, y= 10, 20
# x, y= y, x  #변수의 자리를 바꿔줌
# x= None #빈 변수를 만들 때 할당 값
# d= d+5 #항상 d라는 변수를 줘야함
#
# split 은 공백을 기준으로 분리하여 변수에 차례대로 저장함
#a, b = map(int, input("?").split())
# a = int(a)
# b = int(b)
#print(a)
#print(b)
# map 은 정수로 변환해줌
limit = 155
    # limit = 166

    # 입력 : 신장(키) 목록
height_list = [189, 154, 145, 178, 164, 150]
    # height_list = [183, 155, 145, 187, 166, 180]

count = 0
    ####### 구현 시작 ################

for i in range(0,height_list+1):
    if height_list[i] > limit: 
        count = count + 1
    print(count)
    ########구현 끝 #####