# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:18:58 2021

@author: gtxnn
"""
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):   
    print('Found "%s"' % match)
