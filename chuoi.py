string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
string_double_quotes = "Đây là một chuỗi sử dụng dấu ngoặc kép."
string_triple_quotes = '''Đây là một chuỗi sử dụng dấu ngoặc 3, có thể trải dài nhiều dòng'''

my_string = "Hello, World!"
print(my_string[0])  # In ra ký tự đầu tiên 'H'
print(my_string[7])  # In ra ký tự tại vị trí index 7 'W'

# Cắt chuỗi (Slicing)
print(my_string[7:])  # In ra từ vị trí 7 đến hết: 'World!'
print(my_string[:5])  # In ra 5 ký tự đầu tiên: 'Hello'
print(my_string[3:8])  # In ra từ vị trí 3 đến 7: 'lo, W'

# Nối chuỗi
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2  # 'Hello World'

# Độ dài chuỗi
length = len(my_string)  # Độ dài của chuỗi

# Các phương thức chuỗi
my_string = " Hello World! "
print(my_string.strip())  # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
print(my_string.split(","))  # Chia chuỗi theo dấu phẩy: [' Hello', ' World! ']
print(my_string.replace("hello", "Hi"))  # Thay thế "hello" thành "Hi"
