def sub_str_max(_str: str) -> int:
    def helper(_str: str) -> int:
        arr = []
        if len(_str) == 0:
            return 0
        if len(_str) == 1:
            return 1
        else:
            for i in range(len(_str)):
                if _str[i] not in arr:
                    arr.append(_str[i])
                else:
                    return max(len(arr), helper(_str[i:len(_str)]))
            return len(arr)
        
    _max = 0
    for i in range(len(_str)):
        _max = max(_max, helper(_str[i: len(_str)]))
            
    return _max

# def sub_str_max(_str: str) -> int:
#     _max = 0
#     store = {}
#     i = 0
#     while(i < len(_str)):
#         if _str[i] not in store:
#             store[_str[i]] = i
#         else:
#             if len(store) > _max:
#                 _max = len(store)
#             i = store[_str[i]]
#             store = {}
#         i = i + 1
#     return max(_max, len(store))

if __name__ == "__main__":
    str = """avak"""
    # print(str[0: 1])
    # print(max(len(str), 0))

    # print(len(str))
    print(sub_str_max(str))
        