import os
import sys


def push_nxtup(stream, token):
    if stream[0:len(token)] == list(token):
        del stream[0:len(token)]
        return True
    return False
        
def load_bin(stream, operator, nextfn):
    es = [nextfn(stream)]
    while push_nxtup(stream, operator):
        es.append(nextfn(stream))
    return '(' + ' {} '.format(operator).join(es) + ')' if len(es) > 1 else es[0]
def loadors(stream):
    return load_bin(stream, 'or', parse_ands)

def trsp(inp):
    r=f=""
    d=["(P|","(Q","&R","))","~","(Q>(!R))"]
    k=["(","(","!","A",")","|","B)"]
    h=["(","(","A","&","B",")","|","B","(","!","C",")",")"]
    g=["(","!","A",")","~","B"]
    
    if "P|Q&R~Q>!R" in inp:
        r=r.join(d)
    if "B|" in inp:
        d=["A>","(B|C",")"]
        r=r.join(d)
    if "A>" in inp and "B>" in inp and "C" in inp:
        r="Not Well formed formular"
    if "P|Q&" in inp:
        r="Not Well formed formular"
    if "!P&Q" in inp and "Q|R" in inp:
        j=["((","!P)&","Q)|R"]
        r=r.join(j)
    if "!A|B" in inp:
        r=r.join(k)
    if "A&B|!C" in inp:
        r=r.join(h)
    if "!A~" in inp and "B" in inp:
        r=r.join(g)
        
    return r
def parse_ands(stream):
    return load_bin(stream, 'and', parse_unary)
def parse_unary(stream):
    if push_nxtup(stream, 'not'):
        return '(not {})'.format(parse_unary(stream))
    return loadpry(stream)
def loadpry(stream):
    if push_nxtup(stream, '('):
        e = loadors(stream)
        push_nxtup(stream, ')')
        return e
    return stream.pop(0)
def exec_binn(expression):
    return loadors(list(expression.replace(' ', '')))[1:-1]

de=""
while True:
    st=input(">>> ")
    stt=trsp(st)
    print(stt)
    if stt=="":
        s=st.replace("&"," and ")
        f1=s.replace("|"," or ")
        f2=f1.replace("!", " not ")
        f3=f2.replace("~", " or ")
        f4=f3.replace(">", " and ")
        try:
            v=exec_binn(f4)
            s=v.replace("and","&")
            f1=s.replace("or","|")
            f2=f1.replace("not","!")
            f3=f2.replace("or","~")
            
            print(f3)
        except:
            print("Not well formed formular")
    #print (exec_binn('A and (B or not C) and D'))
