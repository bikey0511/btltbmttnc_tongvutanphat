# Câu lệnh if-else
x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

# Vòng lặp qua các loại trái cây
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Vòng lặp while
count = 0
while count < 5:
    print(count)
    count += 1  # Tăng biến count bên trong vòng lặp

# Số chia hết cho 5 đầu tiên trong dãy từ 1 đến 100
for i in range(1, 101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là:", i)
        break

# Dùng continue để bỏ qua số lẻ
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)  # Chỉ in ra số chẵn

# Dùng pass khi không làm gì cả
x = 5
if x > 10:
    print("x lớn hơn 10")
else:
    pass  # Không làm gì, chỉ là chỗ giữ chỗ
