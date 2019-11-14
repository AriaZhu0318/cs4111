#!/usr/bin/env python
# encoding: utf-8
import datetime, random, string


def get_curr_day():
    return datetime.date.today()

def get_random_str(length=62):
    # print(string.ascii_letters + string.digits)
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 超过62会报错
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


if __name__ == '__main__':
    print(get_curr_day())