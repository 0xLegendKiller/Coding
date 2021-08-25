PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
# strip spaces from right side
>>> res = "Adi    "
>>> res.rstrip()
'Adi'
>>>  
>>> res = "     Adi"     
# strip spaces from left side
>>> res.lstrip()     
'Adi'
>>>  
# strip characters
>>> res = "https://adityasrivastava.com"
>>> res.rstrip(".com")
'https://adityasrivastava'
# _m , _co ends with m  and (c then o) respectively, and rstrip removes characters m, c, o, .
>>> res = "https://adityasrivastava_m.com" 
>>> res.rstrip(".com")
'https://adityasrivastava_'
>>> res = "https://adityasrivastava_co.com" 
>>> res.rstrip(".com")
'https://adityasrivastava_'
