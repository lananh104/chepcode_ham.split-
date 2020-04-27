#khai báo hàm long_words với 2 tham số là n và str
def long_words(n, str):
    #khai báo list rỗng
    word_len=[]
    #gán list mới bằng cách tách các từ trong str( mỗi chữ cách nhau bởi dấu cách sẽ biến thành một phần tử của list)
    txt=str.split(" ")
    for x in txt:
        #nếu số ký tự của chuỗi x trong list txt lớn hơn n thì thêm vào cuối list word_len chuỗi x
        if len(x)>n:
            word_len.append(x)
    # trả về gía trị của list word_len
    return word_len
# hàm long_words được truyền tham số n = 3 và str =  "The quick brown fox jumps over the lazy dog" và in
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

