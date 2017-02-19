# 맛집 고르기
# 한식, 중식, 일식 중 선택하기
# 한가지를 고르면 식당 이름을 임의로 추천
# 리스트 사용, 사용자 입력 필요

list_a = ["덕승재", "경복궁", "고구려", "함흥냉면"]
list_b = ["만리장성", "아방궁", "중림"]
list_c = ["스시가", "미다래", "아소산"]

import random

style = input("한식, 중식, 일식 중 하나를 입력하세요. ")

if style == "한식":
    print(random.choice(list_a))
elif style == "중식":
    print(random.choice(list_b))
else:
    print(random.choice(list_c))
