#!/usr/bin/env python
# coding: utf-8

# In[177]:


import numpy as np
Sbox =[ ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
        ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
        ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
        ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
        ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
        ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
        ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
        ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
        ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
        ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
        ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
        ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
        ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
        ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
        ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
        ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

Rcon =[ ['01', '01', '04', '08', '10', '20', '40', '80', '1B', '36'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00']]

def aesEncryption(plain_text,key):
    expanded_key=keyExpansion(key)
    supplyKey(keys,round_num)
    
def rotWord(my_word,size=4):
    new_word=[]
    for x in range(1,size+1):
        new_word.append(my_word[x%size])
    return new_word

def subWord(byte):
    my_indexes=[0,0]
    if len(byte)==1:
        byte+='0'
        byte=rotWord(byte,2)
    for x in range(2):
        if byte[x] in ['A','B','C','D','E','F']:
            my_indexes[x]=ord(byte[x])-55  
        else :
            my_indexes[x]=int(byte[x]) 
    print(byte,my_indexes)
    return Sbox[my_indexes[0]][my_indexes[1]]

def decimalToHexadecimal(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',4: '4', 5: '5', 6: '6', 7: '7',8: '8', 9: '9', 10: 'A', 11: 'B',12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if(decimal <= 0):
        return ''
    remainder = decimal % 16
    return decimalToHexadecimal(decimal//16) + conversion_table[remainder]

def hexadecimalTobinary(hexdecnum):
    binnum=''
    hexlen = len(hexdecnum)
    if hexlen<2:
        binnum = binnum + "0000"
    i = 0
    while i<hexlen:
        if hexdecnum[i] == '0':
            binnum = binnum + "0000"
        elif hexdecnum[i] == '1':
            binnum = binnum + "0001"
        elif hexdecnum[i] == '2':
            binnum = binnum + "0010"
        elif hexdecnum[i] == '3':
            binnum = binnum + "0011"
        elif hexdecnum[i] == '4':
            binnum = binnum + "0100"
        elif hexdecnum[i] == '5':
            binnum = binnum + "0101"
        elif hexdecnum[i] == '6':
            binnum = binnum + "0110"
        elif hexdecnum[i] == '7':
            binnum = binnum + "0111"
        elif hexdecnum[i] == '8':
            binnum = binnum + "1000"
        elif hexdecnum[i] == '9':
            binnum = binnum + "1001"
        elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
            binnum = binnum + "1010"
        elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
            binnum = binnum + "1011"
        elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
            binnum = binnum + "1100"
        elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
            binnum = binnum + "1101"
        elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
            binnum = binnum + "1110"
        elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
            binnum = binnum + "1111"
        i = i+1
    return binnum

def binaryToHexadecimal(bnum):
    b = int(bnum, 2)
    hdnum = hex(b)
    return hdnum[2:].upper()

def asci2hex(x):
    return decimalToHexadecimal(ord(x))

def cvtMatrix2String(matrix):
    key=''
    for x in range(4):
        for y in range(4):
            key+=matrix[y][x]
    return key

def cvtString2Matrix(key,hexa=0):
    matrix=[['','','',''],['','','',''],['','','',''],['','','','']]  
    for x in range(4):
        for y in range(4):
            if hexa==1 :
                matrix[y][x]=asci2hex(key[4*x+y])
            else :
                matrix[y][x]=key[4*x+y]

    return matrix

def getColumn(matrix,col_num):
    column=[]
    rows=len(matrix)
    cols=len(matrix[0])
    for x in range(rows):
        for y in range(cols):
            if y==col_num :
                column.append(matrix[x][y])
    return column

def test(a,b,n=8):
    ans=""
    for i in range(n):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

def concatColumns(sub_0,sub_1,sub_2,sub_3):
    matrix=[['','','',''],['','','',''],['','','',''],['','','','']]  
    for x in range(4):
        for y in range(4):
            if y==0 :
                matrix[x][y]=sub_0[x]
            elif y==1:
                matrix[x][y]=sub_1[x]
            elif y==2:
                matrix[x][y]=sub_2[x]  
            else :
                matrix[x][y]=sub_3[x]
    return matrix

def xorOperation3(first_column,last_column,Rcon):
    my_xor=[]
    for x in range(4):
        res=test(hexadecimalTobinary(first_column[x]),hexadecimalTobinary(last_column[x]))
        res=test(res,hexadecimalTobinary(Rcon[x]))
        my_xor.append(binaryToHexadecimal(res))
    return my_xor

def xorOperation2(first_column,last_column):
    my_xor=[]
    for x in range(4):
        res=test(hexadecimalTobinary(first_column[x]),hexadecimalTobinary(last_column[x]))
        my_xor.append(binaryToHexadecimal(res))
    return my_xor


def keyExpansion(key):
    expanded_key=''
    init_key=cvtString2Matrix(key,1)
    expanded_key+=cvtMatrix2String(init_key)
    print(init_key)
    for x in range(10):
        last_column=getColumn(init_key,3)
        last_column=rotWord(last_column)
        for y in range(4):
            last_column[y]=subWord(last_column[y])
        first_column=getColumn(init_key,0)
        sub_0=xorOperation3(first_column,last_column,getColumn(Rcon,x))
        sub_1=xorOperation2(sub_0,getColumn(init_key,1))
        sub_2=xorOperation2(sub_1,getColumn(init_key,2))
        sub_3=xorOperation2(sub_2,getColumn(init_key,3))
        key_generated=concatColumns(sub_0,sub_1,sub_2,sub_3)
        init_key=key_generated
        print(key_generated)
        expanded_key+=cvtMatrix2String(key_generated)
    return expanded_key

def supplyKey(keys,round_num):
    return keys[16*round_num:16*(round_num+1)]
    
def roundOperations(state,key,round_num):
    if round_num>0 and round_num<10:
        print()
    elif round_num==10:
        print()
    else :
        print()


# In[178]:


matrix=keyExpansion('TEAMSCORPIAN1234')
print(matrix)


# In[ ]:




