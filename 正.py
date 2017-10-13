# coding=utf-8

import re

# mezmun='<img class="avatar-lg" src="/files/2017/07-05/190205dc3688190666.png">'
# reg=re.compile(r'.*?src="(.+?|\.png|\.jpg)"')
mezmun = "xahidin bilan mihrigiya mihrigiye"
reg = re.compile(r'.* (.*a)| (.*e)')
m = reg.match(mezmun)
if m:
    m1 = reg.findall(mezmun)
    print(m1)
else:
    print("yoq eyna")
