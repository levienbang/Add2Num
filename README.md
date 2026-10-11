# Add2Num

Cộng 2 số lớn được biểu diễn dưới dạng chuỗi, theo cách học sinh tiểu học cộng:
duyệt từ phải sang trái, cộng từng chữ số và nhớ sang hàng kế tiếp.

## Cấu trúc thư mục

```
.
├── src/
│   ├── my_big_number.py        # Lớp MyBigNumber, hàm sum(stn1, stn2)
│   └── main.py                 # Chương trình console để chạy thử
└── tests/
    └── test_my_big_number.py   # Unit test
```

## Yêu cầu

- Python 3.8 trở lên
- Không cần cài thêm thư viện (chỉ dùng `unittest` có sẵn)

Kiểm tra phiên bản Python:

```bash
python --version
```

> Trên MacOS/Linux có thể cần dùng `python3` thay cho `python`.

## Lấy source code

```bash
git clone https://github.com/levienbang/Add2Num.git
cd Add2Num
git checkout 0.0.1
```

## Chạy chương trình

Truyền 2 số qua tham số dòng lệnh:

```bash
python src/main.py 1234 897
```

Hoặc chạy không tham số rồi nhập 2 số từ bàn phím:

```bash
python src/main.py
```

Kết quả mẫu (in ra từng bước tính, giống ví dụ trong đề):

```
sum("1234", "897"):
Bước 1: Lấy 4 cộng với 7 được 11.
    Lưu 1 vào kết quả được kết quả mới là "1".
    Ghi nhớ 1.
Bước 2: Lấy 3 cộng với 9 được 12.
    Cộng tiếp với nhớ 1 được 13.
    Lưu 3 vào kết quả được kết quả mới là "31".
    Ghi nhớ 1.
Bước 3: Lấy 2 cộng với 8 được 10.
    Cộng tiếp với nhớ 1 được 11.
    Lưu 1 vào kết quả được kết quả mới là "131".
    Ghi nhớ 1.
Bước 4: Lấy 1 cộng với 0 được 1.
    Cộng tiếp với nhớ 1 được 2.
    Lưu 2 vào kết quả được kết quả mới là "2131".
Kết quả: 1234 + 897 = 2131
```

## Chạy Unit Test

Từ thư mục gốc của project:

```bash
python -m unittest discover -s tests -v
```

## Sử dụng trong project khác

Copy file `src/my_big_number.py` vào project của bạn, sau đó:

```python
from my_big_number import MyBigNumber

result = MyBigNumber().sum("1234", "897")  # "2131"
```

Mỗi lần gọi `sum`, các bước tính sẽ được in ra màn hình.
