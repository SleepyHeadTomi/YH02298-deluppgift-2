### Deluppgift 2 - Test av inloggningsfunktion på saucedemo.com med Selenium

Denna uppgift innehåller automatiserade tester för att validera inloggningsfunktionen på saucedemo.com.

Projektet har utvecklats med Python-version 3.11.7, men fungerar med valfri 3.11-version.

#### Krav:
Följande behöver installerat på datorn:
- Python 3.11
- Chrome
- (IDE, tex PyCharm)

#### Installationsguide (via `cmd`, System: Windows):
1. Öppna kommandotolk och klona ner repot från GitHub, `git clone https://github.com/SleepyHeadTomi/YH02298-deluppgift-2.git`
2. Gå in i projekt-mappen: `cd YH02298-deluppgift-2`
3. Skapa virtuell miljö: `py -3.11 -m venv .venv`
4. Aktivera miljö: `.venv\Scripts\activate`
5. Installera paket: `pip install -r requirements.txt`
6. Kör test med: `pytest -v`
7. Deaktivera miljön efter körning: `deactivate`

Det går även bra att utföra denna procedur i en IDE (PyCharm). Notera att steg 3-5 också behövs med detta utförande. 
Öppna en terminal i IDE:n och kör steg 3 t.o.m steg 5 för att skapa och aktivera en virtuell miljö, samt för att 
installera nödvändiga paket.