# Kabely

*Nejdříve úlohu vyřešíme pro konkrétní velikost, potom zkusíme výsledek zobecnit.*

# Zadání

## Úvod

Mezi 10. patrem a přízemím vede v budově osm kabelů (každý kabel vede z 10. patra do přízemí). Neví se, které konce kabelů k sobě patří. Podívejte se na obrázek, na kterém jsou už konce kabelů v každém patře označené (10. patro čísla `1-8`, přízemí `a-h`). Naším úkolem je zjistit, jaké konce patří k jednomu kabelu (například, konec kabelu číslo 3 v 10. patře patří ke konci c. v přízemí). 

## Co budeme používat

K párování kabelů budeme používat elektrický proud a žárovku. V přízemí i v 10. patře je zdroj. Když ke zdroji připojíme kabely, poteče nimi proud. Když potom sejdeme dolů nebo nahorů, ke kabelům potom přiložíme žárovku. Pokud nimi teče proud, tak se žárovka rozsvítí. Můžeme předpokládat, že když kabely v přízemí napojíme na zdroj, v 10. patře zdroj přestane fungovat (zdroj v 10. patře znovu začne fungovat, až na něj začneme napojovat kabely).

## Co vyřešit

Můžeme vidět, že s dostupnými prostředky napárování kabelů dosáhneme jen, když uděláme cestu mezi patry. Budeme hledat minimální počet cest, jak napárovat všech 8 kabelů. Popište postup, který napáruje kabely v log(N) cestách, kde N = 2^k (mocniny dvojky) je počet kabelů.

## Naivní přístup

Za jeden sestup nahorů nebo dolů vždy spárujeme jeden kabel. Použili bychom takový algoritmus (předpokládejme, že začínáme nahoře):

1. Připojím kabel `č. 1` v 10. patře ke zdroji
2. Sejdu dolů (`1. cesta`) a začnu ke kabelům připojovat žárovku (která se rozsvítí, třeba `e.`, patří k `č. 1`)
3. Připojím ještě nenapárovaný kabel (třeba `a.`) ke zdroji
4. Vyjdu nahoru (`2. cesta`) ... pokračuji v párování, začínám od kroku 1 pro jiný nenapárovaný kabel

Pro 8 kabelů potřebuju udělat 7 cest (7 napárování kabelů - zbývající nenapárovaný je poslední pár). Hledaným postupem je ale možné 8 kabelů spárovat jen po 3 cestách.
