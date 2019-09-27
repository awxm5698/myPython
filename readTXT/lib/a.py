import re

a = "### 第五1232****章 ####"
re_compile = r'.*[第].{1,4}[章|节]'

r = re.compile(re_compile)

if r.findall(a):
    print(a)


print(re.sub(r'[#]|[*]', "", a))