prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen ["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[0:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
reclame_tekst5 = reclame_tekst2.lower()
reclame_tekst6 = reclame_tekst5.split()
el = reclame_tekst6
for item in el:
    print(item)
# status per opdracht 9 van lesdeel 7.15