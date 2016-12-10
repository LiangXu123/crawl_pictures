# coding=utf-8
# 徐亮的自定义全局变量模块
import  global_var_model as gl
#可以实现对全局变量的修改

def fun1():
    gl.gl_int_i += 4
    return gl.gl_int_i
a=fun1()
print a
def fun2():
    gl.gl_int_i += 400
    return gl.gl_int_i
b=fun2()
print b
