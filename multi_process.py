#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : multi_process.py
# @Author: Calex
# @Date  : 2020/12/30
# @Desc  :

import signal
from multiprocessing import Pool, cpu_count


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def multi_process_map_async(func, items):
    """
    python多进程
    :param func: 目标函数
    :param items: 迭代数据, list
    :return: 目标函数的输出
    """

    pool = Pool(processes=cpu_count() - 1, initializer=init_worker, maxtasksperchild=400)
    ret = pool.map_async(func, items)
    pool.close()
    pool.join()

    return ret.get() if ret.successful() else []


def func(x):
    """
    python多进程测试函数
    :param x:
    :return:
    """
    return x * x


if __name__ == '__main__':
    result = multi_process_map_async(func, [1, 2, 3, 4, 5, 6])
    print(result)
