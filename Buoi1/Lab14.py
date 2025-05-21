def truy_cap_phan_tu(tuple_data):
    fist_element = tuple_data[0]
    last_element = tuple_data[-1]
    return fist_element,last_element

input_tuple = eval(input("Nhap phan tu ,vi du(1,2,3)"))
fist,last = truy_cap_phan_tu(input_tuple)

print("Phan tu dau tien la ",fist)
print("phan tu cuoi la ",last)