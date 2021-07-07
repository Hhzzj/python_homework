# 作为Apple Store App独立开发者，你要搞限时促销，为你的硬用生成激活码（或者优惠券），使用python如何生成200个激活码（或者优惠券）？

import random

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
def get_a_activation_codes(len):
    activation_code = ''
    for l in range(len):
        activation_code += random.choice(CHARS)
    return activation_code

def get_200_activation_codes(len):
    all_activation_codes = []
    for i in range(200):
        activation_code = get_a_activation_codes(len)
        all_activation_codes.append(activation_code)
    return all_activation_codes

if __name__ == '__main__':
    keys = get_200_activation_codes(16)
    print(keys)
