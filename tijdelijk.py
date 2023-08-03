prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen ["aardbei"] * 0.8
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € "
print(((f"{reclame_tekst}{aanbieding}")[:62]).upper())