# # # palindrome 판별식
# # word = input()
# # is_palindrome = True

# # for i in range(len(word)//2 == 0):
# #     if word[i] == word[-1-i]:
# #         is_palindrome = False
# #         break
# # print(is_palindrome)

# # print(word == word[::-1])
# # # 리스트의 경우 문자 하나하나가 다 요소로 들어가게 됨
# # # ["a","b","c"]등
# # list(word) = list(reversed(word))

# text = "hello"

# # for i in range(len(text)-1):
# #     print(text[i], text[i+1], sep="")

# # sentence = "this is python script"
# # split = sentence.split()

# # for i in range(len(split)-1):
# #     print(split[i], split[i+1], sep=" ")

# two_gram = zip(text, text[1:])
# for i in two_gram:
#     print(i[0], i[1], sep="")

# text = "hello"
# print([text[i:] for i in range(3)])


# n= int(input())
# text= input()
# words= text.split()
# if len(words)<n:
#     print("wrong")
# else:
#     n_gram= [text[i:i+7] for i in range(len(text))]
#     for i in n_gram:
#         print(i)
# zip(*[words[i:] for i in range(n)])


with open("words.txt", "r") as file:
    is_pali = True
    word = input().split("\n")

    for i in range(len(word)//2 == 0):
        if word[i] == word[-1-i]:
            is_pali = False
    print(word)
