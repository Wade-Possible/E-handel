## Projektbeskrivning

I den här gruppuppgiften har vi arbetat med försäljningsdata från en fiktiv e-handel. Målet har varit att undersöka vad som säljer bäst, var försäljningen är störst och om det finns några tydliga mönster eller avvikelser.

Vi har använt Python 3.14.7 för att analysera datan och skapat tabeller och diagram för att visa resultaten. Utifrån analyserna har vi även tagit fram några rekommendationer.

## Projekt/mappstruktur

* data/ – Innehåller CSV-filen som vi analyserar.

* notebooks/report.ipynb – Här finns vår rapport med analyser och diagram.

* src/ – Innehåller funktioner som används i rapporten.

* requirements.txt – Bibliotek som behövs för att köra projektet.

## Så kör du projektet

* Ladda ner projektet från GitHub.

* Öppna projektet i Visual Studio Code.

* Installera biblioteken med pip install -r requirements.txt.

* Öppna notebooks/report.ipynb och kör cellerna uppifrån och ned.

## Gruppmedlemmar
* Christoffer
* Felicia
* Jordan
* Roshima
* Wansiri

## Roller och ansvar

* Roshima: Fråga 4, genomsnittligt ordervärde (AOV) och spridning, inklusive histogram, boxplot och funktionerna `compute_aov`, `find_outliers` och `order_spread`

* Christoffer: Ansvarat för fråga 1 (Vad säljer vi?) och fråga 5 (Topp-listor), där jag tagit fram försäljningen per kategori och visualiserat de tre kategorier som har högst intäkter. Jag har även ansvarat för att förbereda projektet inför inlämning genom att sammanställa gruppens olika delar i report.ipynb, lägga in funktioner från src, strukturera rapporten och kontrollera att koden fungerar.

* Wansiri – Fråga 3 (När säljer vi?):
            1. Ansvarade för frågan om tidsmönster i försäljningen (januari–juni 2024).
            2. Kontrollerade datumen, la till månad, veckodag och vecka, och summerade intäkten per månad, vecka och veckodag. Gjorde tre diagram samt snitt och median per dag och vecka
            3. Skrev funktionerna i `src/time_analysis.py` och `src/time_charts.py`.