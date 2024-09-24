import subprocess
from datetime import datetime

temp_output = f"{datetime.now().strftime('output-%Y%m%d%H%M%S.txt')}"

with open('wallets.txt', 'r', encoding='utf-8') as f:
  wallets = [x.strip() for x in f.readlines() if x]

# 1 or 2 or 3
SAVE = 1 
# SAVE = 2 
# SAVE = 3 

output = []

for wallet in wallets:
  convert_output = subprocess.check_output(['sui', 'keytool', 'convert', wallet], encoding='utf-8')
  line = convert_output.split('\n')[SAVE].split('  ')[1]
  output.append(line)

with open(temp_output, 'w', encoding='utf-8') as f:
  f.write('\n'.join(output))