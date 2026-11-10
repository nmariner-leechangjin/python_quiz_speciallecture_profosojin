print("===== 조선시대 퀴즈 게임 =====")
print("1. 퀴즈시작")
print("2. 퀴즈설명")
print("3. 퀴즈종료")
print("==============================")
choice = input("번호를 선택하세요")
if choice == "1":
    answer = input("조선을 건국한 king은 누구인가요? ")
    if answer == "이성계":
        print("정답입니다!")
    else:
        print("틀렸습니다. 정답은 '이성계'입니다.")
    print("퀴즈를 시작합니다.")
if choice == "2":
    print("퀴즈 설명: 조선시대에 관련된 퀴즈를 풀어보세요.")
if choice == "3":
    print("퀴즈를 종료합니다.")
