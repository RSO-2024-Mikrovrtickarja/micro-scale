# Micro Scale
### *Skupina 16 - Mikrovrtičkarja*

## Opis
Projekt Micro Scale je v osnovi oblačna storitev, oblikovana s principi mikrostoritvene arhitekture, katere namen in cilj je omogočiti enostaven in hiter način nalaganja, pretvorbe, deljenja in prenosa obdelanih fotografij. Registriranim uporabnikom zelo različnih tehnoloških zmožnosti tako omogoča enostaven in hiter način tako pretvorbe fotografij v drug, bolj podprt, tip datoteke, kot tudi zmanjševanje le teh. S tem med drugim rešujemo problem deljenja fotografij, ki se izkažejo kot prevelike za določeno komunikacijsko platformo, na primer od klasične omejitve dvajsetih megabajtov e-poštnih priponk.

## Mikrostoritve
### Čelni del aplikacije
Ta mikrostoritev bo imela eno samo nalogo: uporabniku izpostaviti uporabniški vmesnik,
oblikovan v ogrodju Django ali React. Sama funkcionalnost preostale storitve ne bo potekala preko te mikrostoritve.

Na voljo bodo vsaj tri funkcionalnosti: nalaganje in prenos fotografije, pretvarjanje fotografije in generiranje javnega URL-ja. V kolikor bo čas, bova temu dodala recimo še galerijo, kjer so vidne naložene in pretvorjene fotografije danega uporabnika.

### Avtentikacija
Ta mikrostoritev bo skrbela za avtentikacijo uporabnikov na podlagi Json Web Token standarda. Nadgradnja avtentikacije, v kolikor se v to spustiva, bo zajemala večfaktorsko aventikacijo *(2FA)*.
Odjemalci bodo uporabljali to mikrostoritev za registracijo, prijavo in odjavo.

### Hramba fotografij
Ta mikrostoritev bo skrbela za možnost nalaganja in varne hrambe fotografij na strežnikih naše storitve. Prijavljeni uporabniki bodo lahko fotografije nalagali in dostopali do tistih, do katerih imajo dostop (bodisi preko generiranega URL-ja kot tudi na podlagi lastništva fotografije v privatni galeriji). Mikrostoritev bo omogočala izdajanje zahtevka, da se naložena fotografija pretvori (se ji zmanjša velikost, kvaliteta, format, itd.). Pri tem bo preko sporočilnega sistema (najverjetneje ZeroMQ) to delo naložila mikrostoritvi za procesiranje fotografij. Vsak uporabnik bo imel omejeno število razpoložljivega prostora za fotografije.

Poleg nalaganja bo mikrostoritev po zahtevku izbrano fotografijo prenesla na uporabnikovo napravo v enakem formatu in velikosti, kot je shranjena v hrambi oblaka.

Na voljo bo tudi brisanje fotografije in generiranje javnih URL-jev, s katerimi lahko tudi neprijavljeni uporabniki dostopajo do določenih procesiranih fotografij.

### Procesiranje fotografij
Ta mikrostoritev bo skrbela za vse procesiranje, ki se bo dogajalo nad fotografijami (spreminjanje velikosti, formata, kvalitete, itd.). Mikrostoritev bo delovna navodila prejemala preko sporočilnega sistema od mikrostoritve za hrambo. Na podlagi navodil bo naložila fotografijo, izvedla ustrezne operacije nad njo, in jo shranila na ustrezno mesto nazaj v oblaku, zopet z uporabo mikrostoritve za hrambo.

## Uporabljena orodja

## Shema

## Namestitev

