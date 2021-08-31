

'''
1、dict查找性能远大于list
2.在list中随着list数据的增大，查找时间会增大
3.在dict中查找元素不会随着dict的增大而增大
dict原理：hash表

1.hash(key)——> hash(key) & int值 = hash_value——> hash_table[hash_value] = {key,value}
2.if hash_value in hash_table:
    冲突
    解决冲突:"abc" -> ('c'+随机数) —>hash_value
            如果继续冲突："abc" -> ('bc'+随机数) —>hash_value

4.不可变对象都是可hash的，str,fronzenset,tuple,
5.dict内存花销大，大量空余表元，查询速度快，自定义对象或者python内部对象都是用dict包装的
6.dict添加数据可能改变已有数据的顺序

'''