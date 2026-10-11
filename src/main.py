import sys

from my_big_number import MyBigNumber


def main():
    if len(sys.argv) == 3:
        stn1, stn2 = sys.argv[1], sys.argv[2]
    else:
        stn1 = input("Nhap so thu nhat: ").strip()
        stn2 = input("Nhap so thu hai: ").strip()

    result = MyBigNumber().sum(stn1, stn2)
    print(f"Kết quả: {stn1} + {stn2} = {result}")


if __name__ == "__main__":
    main()
