# main.py 에서 calculation.py 정의한 함수 불러오기

# import calculation as cal

from arithmetic import plus
from arithmetic import subtract
from dataPreprocessing import processing
from dataPreprocessing import importData

a = 3
b = 4

# def main():
#     print("안녕하세요, main() 입니다.")
#     print("a + b = ", cal.plus(a, b))
#     print("a - b = ", cal.subtract(a, b))
#     print("a * b = ", cal.multiple(a, b))

def main():
    print("안녕하세요, main()입니다. ")
    print("a + b = ", plus.add(a, b))
    print("a - b = ", subtract.minus(a, b))

    # 데이터 전처리 시작
    data = importData.readData()
    processing.process_data(data)

if __name__ == "__main__":
    main()
