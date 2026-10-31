# Extraits réels courts : découpe des enregistrements de calibrage aux pauses naturelles (>=150 ms),
# morceaux de 0,8 à 3,5 s, une coupe au milieu de la pause. Aucune transformation du signal.
import json, numpy as np, soundfile as sf, librosa, os
E=[json.loads(l) for l in open('calib/entrees.jsonl')]
out=[]
for e in E:
    x,sr=sf.read(e['f'],dtype='float32',always_2d=True); x=x.mean(1)
    h=int(sr*0.01); n=len(x)//h
    db=20*np.log10(np.sqrt(np.mean(x[:n*h].reshape(n,h)**2,1))+1e-9)
    act=db>max(np.percentile(db,95)-40,-55)
    # pauses
    P=[];i=0
    while i<n:
        if not act[i]:
            j=i
            while j<n and not act[j]: j+=1
            if i>0 and j<n and j-i>=15: P.append((i+j)//2)
            i=j
        else: i+=1
    bornes=[0]+P+[n]
    k=0
    for a,b in zip(bornes,bornes[1:]):
        d=(b-a)*0.01
        if 0.8<=d<=3.5:
            f=f"court/{e['id']}.{k}.wav"; sf.write(f,x[a*h:b*h],sr,subtype='PCM_16')
            out.append({"id":f"{e['id']}.{k}","f":f,"accent":e['accent'],"voix":e.get('voix'),"d":round(d,2)}); k+=1
open('court/entrees.jsonl','w').write(''.join(json.dumps(o)+'\n' for o in out))
print(len(out))
