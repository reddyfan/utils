"""
@Time ： 2021/1/3 16:44
@Auth ： Reddy
@File ：file_store.py
@Description : 文件存储
"""
import csv
import os

import ujson
import yaml


def to_dict(columns, data):
    """
    将字段和数据组成字典
    :param columns: 字段
    :param data: 序列数据
    :return: 字典
    """
    return [dict(zip(columns, item)) for item in data]


def reader(fun):
    """
    文件读取装饰器
    :param fun:
    :return:
    """
    def load(filename, encoding='utf-8', read=None):
        if os.path.exists(filename):
            with open(filename, 'r', encoding=encoding) as file:
                read = file.read()
                return fun(filename, encoding, read)
        return None

    return load


def read_csv(filename, encoding='utf-8'):
    """
    读取csv文件
    :param filename: 文件名
    :param encoding: 编码
    :return: 读取的文件数据
    """
    if os.path.exists(filename):
        with open(filename, 'r', encoding=encoding) as file:
            read = csv.reader(file)
            return read
    return None


def to_csv(filename, data, columns=None, encoding='utf-8'):
    """
    将数据存储为csv文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    with open(filename, 'a', encoding=encoding, newline='') as file:
        csv_file = csv.writer(file)
        if (not flag) and columns:
            csv_file.writerow(columns)

            csv_file.writerows(data)


def to_csv_dict(filename, data: dict, columns=None, encoding='utf-8'):
    """
    将数据存储为csv文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 字典类型的数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    with open(filename, 'a', encoding=encoding, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        if not flag and columns:
            writer.writeheader()
        for item in data:
            writer.writerow(item)


# def read_json(filename):
#     """
#     读取配置json文件
#     :param filename: 文件名
#     :return: 字典
#     """
#     with open(filename, 'r', encoding='utf-8') as file:
#         loads = ujson.loads(file.read())
#     return loads

@reader
def read_json(filename, encoding='utf-8', read=None):
    """
    读取配置json文件
    :param filename: 文件名
    :return: 字典
    :param encoding:
    :param read:
    :return:
    """

    return ujson.loads(read)


def to_json(filename, data: dict, encoding='utf-8'):
    """
    将数据存储为json文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    print(flag)
    with open(filename, 'a', encoding=encoding) as file:
        file.write(ujson.dumps(data, ensure_ascii=False))


# def read_yml(filename, encoding='utf-8'):
#     if os.path.exists(filename):
#         with open(filename, 'r', encoding=encoding) as file:
#             reader = file.read()
#             return yaml.full_load(reader)


@reader
def read_yml(filename, encoding='utf-8', read=None):
    """
    yml文件读取
    :param filename:
    :param encoding:
    :param read:
    :return:
    """
    return yaml.full_load(read)


if __name__ == '__main__':
    print(read_yml('db.yml'))
    print(read_json('configs.json'))
