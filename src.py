'''
TITLE: CONVERT REGULAR GRAMMAR TO NFA
'''
# MODULES USED
from graphviz import *

#1. GRAPH INITIALIZATION
gra=Digraph()
gra.attr(rankdir='LR')

#2. INPUT 
print("Regular grammar to Finite Automata: here's λ. Enter -1 for end of input")
s=0;i=0;l=list()
while(1):
    s=input()
    if(s=='-1'):
        break
    l.append(s)    
c=0

#3. CREATION OF THE BASIC DIGRAPH STRUCTURE BY ANALYSIS OF START, INTERMEDIATE AND FINAL STATES
for i in l:
    e=i[3:]
    x=e.split('|')
    if(c==0):
        gra.attr('node',style='invisible')
        gra.node('I','I')
    gra.attr('node',style='solid',shape='circle')
    for k in x:
        if(k=='λ'):
            gra.attr('node',style='solid',shape='doublecircle')
    
    gra.node(i[0],i[0])
    if(c==0):
        gra.edge('I',i[0])
        c=1
r='0'
counter1=0
counter2=0
p=0

#4. TRAVERSING THROUGH THE GRAMMAR AND CREATING EDGES BETWEEN NODES
gra.attr('node',style='solid',shape='doublecircle')
for i in l:
    e=i[3:]
    x=e.split('|')    
    for k in x:
        if(len(k)==1):
            if(k[0].isupper()):
                gra.edge(i[0],k[0],label='λ')
            else:
                if(k[0]!='λ'):
                    gra.node(r,'')
                    gra.edge(i[0],r,label=k[0])
                    r+='0'
        elif(len(k)==2 and k[1].isupper()):
            gra.edge(i[0],k[1],label=k[0])
        else:
            y=''
            gra.attr('node',style='solid',shape='circle')
            if(k[-1].isupper()):
                for j in k:
                    if(j.isnumeric() or j.islower()):
                        #y=j if(k[0]==j) else y+','+j
                        
                        if(p==len(k)-2):
                            gra.edge(r[:-1],k[-1],label=j)
                            #r+='0'
                        elif(counter1==0):
                            gra.node(r,'')
                            gra.edge(i[0],r,label=j)
                            r+='0'
                            counter=1
                        else:
                            gra.node(r,'')
                            gra.edge(r[:-1],r,label=j)
                            r+='0'
                    p+=1
                counter1=0
                p=0
            else:
                for j in k:
                    if(p!=len(k)-1):
                        gra.node(r,'')
                        if(counter2==0):
                            gra.edge(i[0],r,label=j)
                            counter2=1
                        else:
                            gra.edge(r[:-1],r,label=j)
                        r+='0'
                    else:
                        gra.attr('node',style='solid',shape='doublecircle')
                        gra.node(r,'')
                        gra.edge(r[:-1],r,label=j)
                        r+='0'
                    p+=1
                counter2=0
                p=0

#5. RENDERING THE GRAPH AS A PDF FILE
gra.render('NFA', view=True)

'''
OUTPUT PROCEDURE:
1. ENTER THE CORRECT REGULAR GRAMMAR AS WRITTEN ON PAPER, EVEN THE SLIGHTEST ALTERATION CAN CAUSE AN ERROR
2. WAIT FOR THE FILE TO RENDER
3. OUTPUT FILE SHOWN

OUTPUT:
Regular grammar to Finite Automata: here's λ. Enter -1 for end of input
A->aB|bA|b
B->aC|bB
C->aA|bC|a
-1
<RENDERED PDF OPENS>
'''
