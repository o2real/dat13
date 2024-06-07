############DEBUGGING#####################
"""머릿속으로 문제 그려보기"""
# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
"""버그 재현하기"""
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
"""컴퓨터 입장에서 생각해보기"""
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
"""오류 수정하기 - 빨간줄 주목"""
# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#  print(f"You can drive at age {age}.")
"""프린트와 친해지기"""
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])


"""휴식도 디버깅팁중 하나 """

"""친구한테도 물어봐라 """

"""코드를 자주 실행해보는 것(단계마다)"""

"""스택오버플로우에 물어보는것"""
"""ㅇㅋ?"""
