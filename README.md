### Deluppgift 2 - Test av inloggningsfunktion på saucedemo.com med Selenium

Denna uppgift innehåller automatiserade tester för att validera inloggningsfunktionen på saucedemo.com.

#### Nödvändig mjukvara:
- Python (rekommenderad Python-tolk: version 3.11)
- IDE (PyCharm rekommenderas men det går med annan IDE med stöd för Python)

#### Installationsguide:
1. Klona ner repot lokalt
2. Starta PyCharm och öppna upp projektet
3. Öppna upp en terminal i PyCharm och utför följande kommandon:
   - `python -m venv .venv` för att skapa en virtuell miljö för projektet
   - `.venv\Scripts\activate` (för Win) alt. `source .venv/bin/activate` (Mac/Linux) för att aktivera miljön
   - `pip install -r requirements.txt` för att installera beroenden
4. Testen är nu redo att köras, antingen direkt i PyCharm eller terminalen med kommandot `pytest -v`