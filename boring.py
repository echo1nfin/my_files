import re

text = r""" 
Торт 
с вишней1 
вишней2 
""" 

print(re.findall(r'виш\w+', text)) 