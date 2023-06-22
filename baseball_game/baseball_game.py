from random import *

print("숫자 야구 게임을 시작합니다!")


class BaseballGame:

    def __init__(self):

        # 맞춰야 할 정답 뽑기
        number = list(range(0, 10))
        self.quest_num = sample(number, 3)
        self.user_num = []
        
        print("정답: " + str(self.quest_num))

    def get_user_num(self):

        # 사용자가 입력하는 숫자
        self.user_num = list(input("0~9까지 숫자 중 중복되지 않게 3개를 고르세요"))

        # 숫자 외 입력 방지
        if self.user_num != int:
            print("숫자만 입력하세요!")
            self.user_num = list(input("다시 입력하세요!"))
        
        # 숫자 3개 이상 입력했을때
        if len(self.user_num) != 3:
            print("숫자 3개만 입력하세요!")
            self.user_num = list(input("다시 입력하세요!"))

        # 중복 제거
        if len(set(self.user_num)) !=3:
            print("중복 없이 입력하세요!")
            self.user_num = list(input("다시 입력하세요!"))
    
        # 정답과 같은지 체크하기 위해 quest_num과 user_num 같은 형식으로 만들기
        temp = [] 
        for i in self.user_num:
            temp.append(int(i))
        self.user_num = temp      

    # 정답인지 체크 하는 함수
    def check_num(self):
        while True:
            self.get_user_num()
            
            self.strike_cnt = 0
            self.ball_cnt = 0
            
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.quest_num[i] == self.user_num[j] and i == j):
                        self.strike_cnt += 1
                        continue

                    elif(self.quest_num[i] == self.user_num[j] and i != j):
                        self.ball_cnt += 1
                        continue


            # 3strike가 되면 종료, 그렇지 않으면 반복 실행           
            if self.strike_cnt == 3:
                print("정답입니다!!!")
                break
            elif self.strike_cnt == 0 and self.ball_cnt == 0:
                print("out : 다시 입력하세요!")
                continue
            else:
                print("땡! [{0} strike, {1} ball] 다시 입력하세요!".format(self.strike_cnt, self.ball_cnt))


def main():
    my_game = BaseballGame()
    my_game.check_num()


if __name__ == "__main__":
    main()
