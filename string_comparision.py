import difflib
d = difflib.Differ()
str = '#any string'
str_2 = '#any seconf string'
str_2 = str_2.lower()
str = str.split(' ')
str_2 = str_2.split(' ')
i=0
# comaprision between string B and string A
# tells what has to be deleted and added in string B to make it as String A with the positions defined as 'i'
result = list(d.compare(str, str_2))
result =  [v for v in result if v[0] != '?']
for l in range(0,len(result)):
    print i,result1[l]
    if result[l][0] == '-' and len(result[l])>2:
          if result[l+1][0] == '+' or result[l-1][0] == '+' and l>0:
            if result[l-1][0] == '+' and result[l+1][0] == '-' :
                i=i+1
    if result[l][0] == '-' :
        i=i-1
    i=i+1
 

