num_str = 125
numStr = str(num_str)

message = 'Hi, my name is Python!'
message_1 = message.replace('y', '0')
print(message_1)
message_1 = message_1.replace('i', '1')
print(message_1)

split_test = 'This is a split test' 
split_test = split_test.split()
print(split_test)
string_join = ' '.join(split_test)
print(string_join)
print(len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))
print(len(list_extend))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
print(dict_test['car'], dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())
