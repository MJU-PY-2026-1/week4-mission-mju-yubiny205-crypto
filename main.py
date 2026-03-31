# 파일이름 : main.py
# 작 성 자 : 주유빈, 3.31
# 하는 일: 도장깨기: 맛집 버킷 리스트

# 1. 비어있는 리스트 만들기 
bucket_list = []

# 2. 입력 받고 리스트에 추가 하기 : 3번
restaurant = input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant = input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant = input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

# 3. 리스트 출력
print(f'리스트: {bucket_list}')

# 4. 맛집을 입력 받아 리스트 0 에 삽입
vip_restaurant = input('맛집 리스트 추가: ')
bucket_list.insert(0, vip_restaurant)

# 5. 리스트 출력
print(f'리스트: {bucket_list}')

# 6. 도장 깬 맛집을 입력 받아, 리스트에서 삭제
visited = input("도장 깨기: ")
bucket_list.remove(v성시isited)

#7. 리스트 출력
print(f'리스트: {bucket_list}')