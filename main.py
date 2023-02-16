from module import Jatekos

jatekosok:list[Jatekos] = []
file = open(file='juventus.csv', mode='r', encoding='utf-8')
for r in file: jatekosok.append(Jatekos(r))

print(f'jatekosok szama: {len(jatekosok)}')

sm:int = 0
for j in jatekosok:
    sm += j.mag
print(f'atlagmagassag: {round(sm / len(jatekosok), 2)} cm')

gs:int = 0
for j in jatekosok:
    gs += j.gol
print(f'szerzett golok szama osszesen: {gs}')

slaposak:list[str] = []
for j in jatekosok:
    if j.sarga > 0:
        slaposak.append(j.nev)
print(f'sargalapos jatekosok: {slaposak}')

for j in jatekosok:
    if j.piros > 0:
        print('volt, aki piros lapot szerzett')
        break
else: print('senki sem szerzett piros lapot')

for i in range(len(jatekosok) - 1):
    for j in range(i + 1, len(jatekosok)):
        if jatekosok[i].perc < jatekosok[j].perc:
            (jatekosok[i], jatekosok[j]) = (jatekosok[j], jatekosok[i])
print('legtobbet volt palyan:')
for i in range(3):
    print(f'\t{i+1}.: {jatekosok[i].nev} ({jatekosok[i].perc} perc)')

kevesetj:list[str] = []
for j in jatekosok:
    if j.perc <= 20:
        kevesetj.append(j.nev)
print(f'max 20 percet voltak palyan. {kevesetj}')

mgi:int = 0
for i in range(1, len(jatekosok)):
    if jatekosok[i].gol > jatekosok[mgi].gol:
        mgi = i
print(f'legtobb golt rgta: {jatekosok[mgi].nev} ({jatekosok[mgi].gol} db)')