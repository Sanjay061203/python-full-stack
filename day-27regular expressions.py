"""
REGULAR EXPRESSION
==================
--->regex is an sequence of char that can searching patter
--->to use regex we have import re module....

1.findall()
-----------
it will find all the char that are in the string...
eg
--
import re
txt = 'sanjay rocky loves kgf'
print(re.findall('a',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))



2.search()
----------
it will find the char, but it will be at the first sequence that found in the string...

eg
--
import re
txt = 'sanjay rocky loves kgf'
print(re.search('[a]',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))


3.split()
---------
eg
--
import re
txt = 'sanjay rocky loves kgf'
print(re.split(' ',txt))

4.sub()
-------
eg
--
import re
txt = 'sanjay rocky loves kgf'
print(re.sub(' ','&',txt))

5.full match()
--------------



metachar
--------
[]
-------------------------------------
EG
--
'import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

^
---------------------------------------
eg
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('^sanjay',txt))
print(re.search('^rocky',txt))

$
---------------------------------------
eg
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('4$',txt))
print(re.search('^rocky$',txt))
.
---------------------------------------
eg
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('r..',txt))
print(re.search('r....',txt))

*
--------------------------------------
eg
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.*4',txt))
print(re.search('r.*1',txt))


+
-------------------------------------
eg
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.+4',txt))
print(re.findall('r.+4',txt))


{}
-------------------------------------
Eg:
--
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.{20}',txt))
print(re.findall('r.{22}',txt))




"""
import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('^sanjay',txt))
print(re.search('^rocky',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('r..',txt))
print(re.search('r....',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.*4',txt))
print(re.search('r.*1',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.+4',txt))
print(re.findall('r.+4',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('s.{20}',txt))
print(re.findall('r.{22}',txt))





