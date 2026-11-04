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

* Roshima – Fråga 4 (Genomsnittligt ordervärde och spridning):
    1. Ansvarade för att analysera genomsnittligt ordervärde (AOV) och spridningen i försäljningsdata.
    2. Skapade histogram och boxplot för att visualisera ordervärdenas fördelning och spridning.
    3. Skrev funktionerna `compute_aov`, `find_outliers` och `order_spread`

* Christoffer – Fråga 1 (Vad säljer vi?) och fråga 5 (Topp-listor):
    1. Ansvarade för att analysera försäljningen per kategori och identifiera vilka kategorier som genererar högst intäkter.
    2. Skapa en graf över de tre kategorierna med högst intäkter.
    3. Ansvarade för att sammanställa gruppens olika delar i report.ipynb, integrera funktioner från src, strukturera rapporten och kontrollera att koden fungerar.
    4. Förberedde projektet inför inlämning och arbetade med README.md.

* Wansiri – Fråga 3 (När säljer vi?):
    1. Ansvarade för frågan om tidsmönster i försäljningen (januari–juni 2024).
    2. Kontrollerade datumen, la till månad, veckodag och vecka, och summerade intäkten per månad, vecka och veckodag. Gjorde tre diagram samt snitt och median per dag och vecka
    3. Skrev funktionerna i `src/time_analysis.py` och `src/time_charts.py`.

* Jordan – Fråga 6 (Eventuella avvikelser):
    1. Analysera försäljningsdata för att beräkna avvikelser (anomalier) i dagsintäkter och visualisera i ett diagram.
    2. Skapade klassen `SalesDataAnalyzer` med metoderna `get_revenue_bounds()`, `compute_anomalies()` och `plot_anomalies()`.
    3. Beräknar kvartiler (Q1, Q3) och karterar undre/övre gränser för intäkter. Identifierar avvikande dagsintäkter med hjälp av Z-score (`> 2.5` standardavvikelser). Skapar en graf med Matplotlib som markerar avvikande dagar med blå punkter.

* Felicia - Fråga 2 (Intäktsanalys per stad):
    1. Implementerat kod med pandas för att läsa in försäljningsdata från CSV.
    2. Grupperat data efter stad “city” och summerat de totala intäkterna “revenue”.
    3. Sorterat och presenterat resultatet för att visa vilka städer som genererar störst int