def aanbieding_1(smaak, prijs, korting):
    lager = prijs - prijs * korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {lager}0 euro"
#print (aanbieding_1("aardbei", 4, 0.1))
def inkomsten_totaal(inkomsten):
    weektotaal = 0
    for dag in inkomsten:
        weektotaal += dag
    return weektotaal
#print(inkomsten_totaal([220,430,125,160,205,90,345]))