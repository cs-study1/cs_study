# https://github.com/cs-study1/cs_study.git


# binary prefix 제거
def del_prefix(bin_num):
    return bin_num[2:]


# 8비트로 나타낼 때
def bit_8(bin_num):
    bin_num = del_prefix(bin_num)
    return bin_num.zfill(8)


a = int('101101', 2)
b = int('010010', 2)
print("AND : ", a & b, bit_8(bin(a & b)))
print("OR : ", a | b, bit_8(bin(a | b)))
print("XOR : ", a ^ b, bit_8(bin(a ^ b)))

# python에서 NOT operator는 binary로 나타낼 때 (-) 기호가 들어감
print("NOT : ", ~a, bin(~a))
print("<< : ", a << 1, bit_8(bin(a << 1)))
print(">> : ", a >> 1, bit_8(bin(a >> 1)))
