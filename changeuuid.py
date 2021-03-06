#! /usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import readjson
import writejson

print("当前UUID为：%s") % str(readjson.ConfUUID)
print("是否要随机生成一个新的UUID (Y/n)：")
genUUID = raw_input()

if genUUID == "y" or genUUID == '':
    newuuid = uuid.uuid1()
    print "新的UUID为：{}".format(newuuid)
    writejson.WriteUUID(newuuid)
elif genUUID == "n":
    print("已取消生成新的UUID,未执行任何操作")
else:
    print("输入不正确，请输入 y 或 n")
