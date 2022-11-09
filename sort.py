import numpy as np

### Some relatively hack-y code to sort bib files
### Highly suggest backing up your work before running this.
### If you have stray "\newline" commands hanging around in your latex file, this won't work
### (but also may not raise an error). Follow formatting from the sample file as closely as possible.


with open('mybib.bib') as f:
    lines = f.readlines()
lines = np.array(lines)

### Isolate all bib entries
start = np.array([ind for ind, i in enumerate(lines) if i[0]=="@"])
end = np.append(start[1:]-1,len(lines))

### If you would rather sort by entries first, change this to false
### e.g. if True, @article{BBB} will be listed before @book{AAA}
ignore_entry_types = True

### Create dictionary with keys as the bib references
if ignore_entry_types:
    d = {lines[s][lines[s].find("{")+1:lines[s].find(",")]: np.append(lines[s:e+1][lines[s:e+1]!='\n'],'\n') for s,e in zip(start,end)}
else:
    d = {lines[s]: lines[s:e+1][lines[s:e+1]!='\n'] for s,e in zip(start,end)}
    
### Save while sorting on these keys
with open('mybib.bib', 'w') as f:
    for line in [i for s in [list(d[key]) for key in sorted(d.keys())] for i in s]:
        f.write(line)
        
        
        
### Repeat the above but for a .tex file     
with open('lit_review.tex') as f:
    lines = f.readlines()
lines = np.array(lines)

start = np.array([ind for ind, i in enumerate(lines) if i[:10]=="\def \sect"])
end = np.array([ind+start[0] for ind, i in enumerate(lines[start[0]:]) if i[:8]=="\\newpage"])
intro = lines[:start[0]]
outro = lines[end[-1]+1:]
d = {lines[s][lines[s].find("{")+1:lines[s].find("}")]: np.append(lines[s:e+1][lines[s:e+1]!='\n'],['\n','\n','\n']) for s,e in zip(start,end)}

with open('lit_review.tex', 'w') as f:
    for line in list(intro)+[i for s in [list(d[key]) for key in sorted(d.keys())] for i in s]+list(outro):
        f.write(line)