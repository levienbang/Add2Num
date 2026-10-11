class MyBigNumber:
    def sum(self, stn1, stn2):
        print(f"sum(\"{stn1}\", \"{stn2}\"):")

        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        result = ""
        step = 1

        while i >= 0 or j >= 0:
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0

            print(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}.")
            total = digit1 + digit2 + carry
            if carry > 0:
                print(f"    Cộng tiếp với nhớ {carry} được {total}.")

            digit = total % 10
            carry = total // 10
            result = str(digit) + result
            print(f"    Lưu {digit} vào kết quả được kết quả mới là \"{result}\".")
            if carry > 0:
                print(f"    Ghi nhớ {carry}.")

            i -= 1
            j -= 1
            step += 1

        # Con nho o hang cuoi cung thi ghi them vao dau ket qua.
        if carry > 0:
            result = str(carry) + result
            print(f"Bước {step}: Còn nhớ {carry}, ghi {carry} vào đầu kết quả được \"{result}\".")

        return result
