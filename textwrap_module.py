import textwrap 
  
value = """bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd"""
  
# Wrap this text. 
# wrapper = textwrap.TextWrapper(width=10) 
  
word_string = textwrap.fill(text=value,width=9) 
  
# Print each line. 
print(word_string)
list_string = word_string.split("\n")
for item in list_string:
    print(len(item))