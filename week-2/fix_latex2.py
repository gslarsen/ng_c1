import json

with open('C1_W2_Lab02_Multiple_Variable_Soln_BROKEN.ipynb', 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        for i in range(len(cell['source'])):
            cell['source'][i] = cell['source'][i].replace('f*{', 'f_{')
            cell['source'][i] = cell['source'][i].replace('w*0', 'w_0')
            cell['source'][i] = cell['source'][i].replace('w*{n-1}', 'w_{n-1}')
            cell['source'][i] = cell['source'][i].replace('x*{n-1}', 'x_{n-1}')

with open('C1_W2_Lab02_Multiple_Variable_Soln.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print('Created fresh fixed file!')
