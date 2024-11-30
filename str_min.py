def str_min(s_one, s_two):
    return s_one if s_one < s_two else s_two

def str_min3(s_one, s_two, s_three):
    return str_min(str_min(s_one, s_two), s_three)

def str_min4(s_one, s_two, s_three, s_four):
    return str_min(str_min3(s_one, s_two, s_three), s_four)

print(str_min4('hello', 'world', 'he', 'h'))