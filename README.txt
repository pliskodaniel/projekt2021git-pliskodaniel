Ide o full-stack single-page aplikáciu.
Je to grafické prostredie ktoré používa webovú stránku, prostredníctvom ktorej používateľ vie zobraziť VES súbor ako obrázok.
Táto webová stránka prostredníctvom JavaScriptu komunikuje s webovým serverom používajúcim Flask ktorý je naprogramovaný v Pythone. Ten spracuje HTTP požiadavku a vráti hotový PNG obrázok.

Frontend:
HTML+CSS+JavaScript
Obsahuje textové pole, tlačidlo a obrázok. Do textového poľa používateľ vloží obsah .ves súboru, po stlačení tlačidla sa hotový obrázok zobrazí na stránke.

Backend:
Webserver v Python využívajúci Flask príjma POST požiadavky na ceste /render obsahujúce "ves" a "width". Podľa nich vyrenderuje obrázok a ten vráti ako odpoveď.

Obsah repozitáru je potrebné stiahnuť z tejto lokality.
Potrebné je dostať sa do priečinku v ktorom sú stiahnuté súbory a zadaním týchto príkazov do príkazového riadku(cmd) dokažeme spustiť lokálny webový server:


 py -3 -m venv venv
 venv\Scripts\activate
 pip install Flask
 python -m pip install --upgrade Pillow

 set FLASK_APP=main.py
 flask run

Kresliť možme v tejto aplikácii nasledovnými príkazmi:

HEADER version width height		VES v1.0 600 300
CLEAR color (set canvas)		CLEAR #FAFAFA
LINE A B thichness color		LINE 349 206 344 207 2 #FEDCBA
TRIANGLE A B C thichness color		TRIANGLE 50 100 200 300 150 200 1 #00FF00
FILL_TRIANGLE A B C color		FILL_TRIANGLE 200 100 400 300 300 300 #0000FF
RECT A B thichness color		RECT 200 100 500 300 1 #000000
FILL_RECT A B color			FILL_RECT 400 100 550 300 #00FF00
CIRCLE S radius thichness color		CIRCLE 300 200 100 1 #FFFFFF
FILL_CIRCLE S radius color		FILL_CIRCLE 200 100 50 #00FF00
CURVE A B C D thichness color		CURVE 20 500 50 11 476 480 604 26 3 #00148f


