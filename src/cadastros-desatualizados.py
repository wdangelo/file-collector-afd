
import pyautogui as p

p.sleep(2)
#print(p.position())
p.click(x=357, y=997)
p.sleep(2)
p.write(f'https://sisbranalitico.sisbr.coop.br/sisbranalitico/bi/')

p.press('enter')
p.sleep(4)

p.click(x=572, y=327)
p.write('roborh5042_00')

p.sleep(4)
p.click(x=541, y=406)
p.write('@sicoob22')

p.sleep(2)
p.click(x=524, y=488)

p.sleep(2)
p.click(x=644, y=608)

p.sleep(8)
print(p.position())


