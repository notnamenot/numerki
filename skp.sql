--------2.1---------------
SELECT nazwa, ulica, miejscowosc FROM klienci ORDER BY nazwa;

SELECT nazwa, ulica, miejscowosc FROM klienci ORDER BY miejscowosc DESC, nazwa;

SELECT nazwa, ulica, miejscowosc FROM klienci 
WHERE miejscowosc = 'Kraków' or miejscowosc = 'Warszawa' ORDER BY miejscowosc DESC, nazwa;
--lub
SELECT nazwa, ulica, miejscowosc FROM klienci WHERE miejscowosc in('Kraków', 'Warszawa') ORDER BY miejscowosc DESC, nazwa;

SELECT * FROM klienci ORDER BY miejscowosc DESC;

SELECT * FROM klienci WHERE miejscowosc = 'Kraków' ORDER BY nazwa;

--------2.2---------------

SELECT nazwa, masa FROM czekoladki WHERE masa > 20;

SELECT nazwa, masa, koszt FROM czekoladki WHERE masa > 20 and koszt > 0.25;

SELECT nazwa, masa, CAST(koszt*100 AS INT) AS "koszt [gr]" FROM czekoladki 
WHERE masa > 20 and koszt > 0.25;
--lub
SELECT nazwa, masa, ROUND(koszt*100,0) AS "koszt [gr]" FROM czekoladki 
WHERE masa > 20 and koszt > 0.25;

SELECT nazwa, czekolada, nadzienie, orzechy FROM czekoladki 
WHERE (czekolada = 'mleczna' AND nadzienie = 'maliny') OR (czekolada = 'mleczna' AND 
nadzienie = 'truskawki') OR (ORZECHY = 'laskowe' AND czekolada != 'gorzka'); 

SELECT nazwa, koszt FROM czekoladki WHERE koszt > 0.25;

SELECT nazwa, czekolada FROM czekoladki WHERE czekolada in ('biała','mleczna');
--lub
SELECT nazwa, czekolada FROM czekoladki WHERE czekolada = 'biała' OR czekolada = 'mleczna';

--------2.3---------------

SELECT 124*7+45;

SELECT 2^20;

SELECT sqrt(3);

SELECT pi();

--------2.4---------------

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24; --włącznie

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.25 AND 0.35;

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE (masa BETWEEN 25 AND 35) 
OR  (koszt BETWEEN 0.15 AND 0.24);

--------2.5---------------

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE orzechy IS NOT NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE orzechy IS NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE orzechy IS NOT NULL AND nadzienie IS NOT NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE czekolada IN ('mleczna', 'biała') AND orzechy IS NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE czekolada NOT IN ('mleczna', 'biała') AND (orzechy IS NOT NULL OR nadzienie IS NOT NULL);

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nadzienie IS NOT NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nadzienie IS NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nadzienie IS NULL AND orzechy IS NULL;

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE czekolada IN ('mleczna', 'biała') AND nadzienie IS NULL;

--------2.6---------------

SELECT nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24 OR koszt BETWEEN 0.15 AND 0.24;

SELECT nazwa, masa, koszt FROM czekoladki WHERE (masa BETWEEN 15 AND 24 AND koszt BETWEEN 0.15 AND 0.24) OR (masa BETWEEN 25 AND 35 AND koszt BETWEEN 0.25 AND 0.35);

SELECT nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24 AND koszt BETWEEN 0.15 AND 0.24;

SELECT nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 25 AND 35 AND koszt NOT BETWEEN 0.25 AND 0.35;

SELECT nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 25 AND 35 AND koszt NOT BETWEEN 0.15 AND 0.34 AND koszt NOT BETWEEN 0.25 AND 0.35;

--\i [FILE]	execute commands from file

--------2.7---------------

SELECT * FROM klienci;
--\a	  	toggle between unaligned and aligned output mode
--\f ' '	show or set field separator for unaligned query output
--\H		toggle HTML output mode
--\o [FILE]	send all query results to file or |pipe

--------2.8---------------

--zapytanie1.sql:
SELECT idczekoladki, nazwa, opis FROM czekoladki;
--\H				zamiana na html
--\o zapytanie1.html		wysyłanie do pliku następnych instrukcji
--SELECT idczekoladki, nazwa, opis FROM czekoladki;
--\o				koniec wysyłania

--------3.1---------------

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE datarealizacji BETWEEN '2013-11-12' AND '2013-11-20';

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE datarealizacji BETWEEN '2013-12-01' AND '2013-12-06' OR datarealizacji BETWEEN '2013-12-15' AND '2013-12-20';

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE datarealizacji BETWEEN '2013-12-01' AND '2013-12-31';

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE DATE_PART('month',datarealizacji) = 11 AND EXTRACT(YEAR FROM datarealizacji) = 2013;

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE DATE_PART('month',datarealizacji) = 11 OR EXTRACT(MONTH FROM datarealizacji) = 12;

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE DATE_PART('day',datarealizacji) = 17 OR EXTRACT(DAY FROM datarealizacji) = 18 OR EXTRACT(DAY FROM datarealizacji) = 19;
--lub
SELECT idzamowienia, datarealizacji FROM zamowienia WHERE DATE_PART('day',datarealizacji) IN (17,18,19);

SELECT idzamowienia, datarealizacji FROM zamowienia WHERE EXTRACT(WEEK FROM datarealizacji) IN (46, 47);

--------3.2---------------

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE SUBSTR(nazwa,1,1) = 'S';
--lub
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa LIKE 'S%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa LIKE 'S%i';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa LIKE 'S% m%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa SIMILAR TO '(A|B|C)%';
--lub
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa SIMILAR TO '[ABC]%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa SIMILAR TO '%[Oo]rzech%';
--LUB
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa ILIKE '%orzech%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa LIKE 'S%m_%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa SIMILAR TO '%(maliny|truskawki)%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa NOT SIMILAR TO '([D-K]|S|T)%';
--lub
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa NOT SIMILAR TO '[D-KST]%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa LIKE 'Słod%';
--lub
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa SIMILAR TO 'Słod%';

SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa NOT SIMILAR TO '% %';
--lub
SELECT idczekoladki, nazwa, czekolada, orzechy, nadzienie FROM czekoladki WHERE nazwa NOT SIMILAR TO '%( %)+';

--------3.3---------------

SELECT miejscowosc FROM klienci WHERE  miejscowosc LIKE '_% %_';

SELECT nazwa, telefon FROM klienci WHERE telefon LIKE '___ ___ __ __';
--lub
SELECT nazwa, telefon FROM klienci WHERE telefon SIMILAR TO '(___ ){2}(__ |__){2}';
--lub
SELECT nazwa, telefon FROM klienci WHERE telefon SIMILAR TO '(___ ){2}(__ ?){2}';

SELECT nazwa, telefon FROM klienci WHERE telefon SIMILAR TO '((___) ?){3}';
--lub
SELECT nazwa, telefon FROM klienci WHERE telefon SIMILAR TO '([[:digit:]]{3} ?){3}';
--lub
SELECT nazwa, telefon FROM klienci WHERE telefon SIMILAR TO '([[:digit:]]{3} ?)+';

--------3.4---------------

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24 
UNION SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.15 AND 0.24;

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 25 AND 35 
EXCEPT 
SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.25 AND 0.35;

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24 
INTERSECT 
SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.15 AND 0.24 
UNION 
(SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 25 AND 35 
INTERSECT 
SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.25 AND 0.35);

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 15 AND 24 
INTERSECT 
SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.15 AND 0.24;

SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 25 AND 35 
EXCEPT 
(SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE koszt BETWEEN 0.15 AND 0.24 UNION 
SELECT idczekoladki, nazwa, masa, koszt FROM czekoladki WHERE masa BETWEEN 0.29 AND 0.35);

--------3.5---------------

SELECT idklienta FROM klienci 
EXCEPT 
SELECT idklienta FROM zamowienia;

SELECT idpudelka FROM pudelka 
EXCEPT 
SELECT idpudelka FROM artykuly; --?

SELECT nazwa FROM klienci WHERE nazwa SIMILAR TO '%[Rr]z%'
UNION 
SELECT nazwa FROM czekoladki WHERE nazwa SIMILAR TO '%[Rr]z%' 
UNION 
SELECT nazwa FROM pudelka WHERE nazwa SIMILAR TO '%[Rr]z%';	--'%(Rz|rz)%'

SELECT idczekoladki FROM czekoladki 
EXCEPT 
SELECT idczekoladki FROM zawartosc;

--------3.6---------------

--set search_path to public, siatkowka;

SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM statystyki;

SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM statystyki 
WHERE gospodarze[5] IS NOT NULL AND (gospodarze[5] > 15 OR goscie[5] > 15);
--lub
SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM statystyki 
WHERE gospodarze[5] > 15 OR goscie[5] > 15;

SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości", 
	(case when(gospodarze[1] > goscie[1])then 1 else 0 end +
	case when(gospodarze[2] > goscie[2]) then 1 else 0 end +
	case when(gospodarze[3] > goscie[3]) then 1 else 0 end + 
	case when(gospodarze[4] > goscie[4]) then 1 else 0 end + 
	case when(gospodarze[5] > goscie[5]) then 1 else 0 end) 
	|| ':' ||	--konkatencja(łączenie)
	(case when(gospodarze[1] < goscie[1])then 1 else 0 end +
	case when(gospodarze[2] < goscie[2]) then 1 else 0 end +
	case when(gospodarze[3] < goscie[3]) then 1 else 0 end + 
	case when(gospodarze[4] < goscie[4]) then 1 else 0 end + 
	case when(gospodarze[5] < goscie[5]) then 1 else 0 end) AS "wynik" FROM statystykiset search_path to public, siatkowka;;
 
SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM statystyki 
WHERE gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		 COALESCE(gospodarze[5], 0) > 100; 


SELECT idmeczu, gospodarze[1] AS "I set", gospodarze[1] + gospodarze[2] + gospodarze[3] + 	 COALESCE(gospodarze[4],0) + COALESCE(gospodarze[5],0) AS "Suma gospodarzy" 
FROM statystyki 
WHERE SQRT(gospodarze[1]) < LOG(2, gospodarze[1] + gospodarze[2] + gospodarze[3] + 	
	COALESCE(gospodarze[4],0) + COALESCE(gospodarze[5],0)); 

--------3.7---------------

--\T [STRING]            set HTML <table> tag attributes, or unset if none
--\pset [NAME[VALUE]]	 set table output option		
--\H                     toggle HTML output mode
--\echo [STRING]         write string to standard output
--\o [FILE]              send all query results to file or |pipe
--\i FILE                execute commands from file



--\H
--\T tabelka
--\o wynik37.html --? można bez o
--SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM siatkowka.statystyki WHERE gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + COALESCE(gospodarze[5], 0) > 100; 
--\o --?

--psql < zapytanie37.sql > wynik37.html
--mv wynik37.html ~/public_html/wynik37.html
--http://borg.kis.agh.edu.pl/~pachizab/wynik37.html

--------3.8---------------

-- \t [on|off]            show only rows

--set search_path to public, siatkowka; --lub siatkowka.statystyki
--\a
--\pset fieldsep ','	
--\t
--SELECT idmeczu, gospodarze[1] + gospodarze[2] + gospodarze[3] + COALESCE(gospodarze[4],0) + 		COALESCE(gospodarze[5], 0) AS "Suma gospodarzy", goscie[1] + goscie[2] + goscie[3] + 		COALESCE(goscie[4],0) + COALESCE(goscie[5], 0) AS "Suma gości" FROM statystyki 
--WHERE gospodarze[5] > 15 OR goscie[5] > 15;

--psql < zapytanie38.sql > wynik38.txt

--------4.1---------------

SELECT k.nazwa FROM klienci k;					--67 (klientów)

SELECT k.nazwa, z.idzamowienia FROM klienci k, zamowienia z;	--iloczyn kartezjański, bezwartościowy

SELECT k.nazwa, z.idzamowienia FROM klienci k, zamowienia z  
WHERE z.idklienta = k.idklienta;				--145 (zamowień),nie scala

SELECT k.nazwa, z.idzamowienia FROM klienci k NATURAL JOIN zamowienia z; --145, scala

SELECT k.nazwa, z.idzamowienia FROM klienci k JOIN zamowienia z
ON z.idklienta=k.idklienta;					--145, nie scala

SELECT k.nazwa, z.idzamowienia FROM klienci k JOIN zamowienia z
USING (idklienta);						--145, scala

--------4.2---------------

SELECT nazwa, idzamowienia, datarealizacji FROM klienci NATURAL JOIN zamowienia 
WHERE nazwa LIKE '%Antoni';

SELECT nazwa, idzamowienia, datarealizacji, ulica  FROM klienci NATURAL JOIN zamowienia 
WHERE ulica LIKE '%/%';

SELECT nazwa, idzamowienia, datarealizacji, miejscowosc  FROM klienci NATURAL JOIN zamowienia 
WHERE miejscowosc = 'Kraków' AND DATE_PART('MONTH',datarealizacji) = 11 AND EXTRACT(YEAR FROM datarealizacji) = 2013;

--------4.3---------------

SELECT nazwa, ulica, miejscowosc, datarealizacji FROM klienci NATURAL JOIN zamowienia 
WHERE datarealizacji >= CURRENT_DATE - INTERVAL '5 YEARS';

--SELECT DISTINCT ON expressions must match initial ORDER BY expressions
SELECT DISTINCT ON(k.nazwa) k.nazwa, ulica, miejscowosc, p.nazwa FROM klienci k NATURAL JOIN zamowienia JOIN artykuly USING(idzamowienia) JOIN pudelka p USING(idpudelka) 
WHERE p.nazwa IN ('Kremowa fantazja', 'Kolekcja jesienna') ORDER BY k.nazwa;

SELECT nazwa, ulica, miejscowosc, idzamowienia FROM klienci LEFT OUTER JOIN zamowienia USING(idklienta) 
WHERE idzamowienia IS NOT NULL;	--outer opcjonalne ,145


SELECT nazwa, ulica, miejscowosc, idzamowienia FROM klienci LEFT JOIN zamowienia USING(idklienta) 
WHERE idzamowienia IS NULL;	--0 bo nie ma klientów którzy nic nie zamówili

SELECT DISTINCT ON(nazwa) nazwa, ulica, miejscowosc, datarealizacji FROM klienci NATURAL JOIN zamowienia 
WHERE DATE_PART('MONTH', datarealizacji) = 11 AND DATE_PART('YEAR', datarealizacji) = 2013; 

SELECT DISTINCT ON(k.nazwa) k.nazwa AS "klient", ulica, miejscowosc,idzamowienia, p.nazwa AS "nazwa pudełka", sztuk FROM klienci k NATURAL JOIN zamowienia JOIN artykuly USING(idzamowienia) JOIN pudelka p USING(idpudelka)
WHERE (p.nazwa = 'Kremowa fantazja' AND sztuk >= 2) OR (p.nazwa = 'Kolekcja jesienna' AND sztuk >= 2);

SELECT DISTINCT ON(k.nazwa) k.nazwa AS "klient", ulica, miejscowosc, p.nazwa AS "nazwa pudełka", c.nazwa AS "nazwa czekoladki", orzechy FROM klienci k 
NATURAL JOIN zamowienia JOIN artykuly USING(idzamowienia) JOIN pudelka p USING(idpudelka)
JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE orzechy = 'migdały';

--------4.4---------------

--1
SELECT p.nazwa AS "nazwa pudełka", substr(p.opis,1,30) AS "opis pudełka", c.nazwa AS "nazwa czekoladki",sztuk, substr(c.opis,1,40) AS "opis czekoladki"
FROM pudelka p LEFT JOIN zawartosc USING(idpudelka) LEFT JOIN czekoladki c USING(idczekoladki);

--2
SELECT idpudelka,p.nazwa AS "nazwa pudełka", substr(p.opis,1,50) AS "opis pudełka", c.nazwa AS "nazwa czekoladki", substr(c.opis,1,40) AS "opis czekoladki"
FROM pudelka p LEFT JOIN zawartosc USING(idpudelka) LEFT JOIN czekoladki c USING(idczekoladki)
WHERE idpudelka = 'heav';

--3
SELECT p.nazwa AS "nazwa pudełka", substr(p.opis,1,30) AS "opis pudełka", c.nazwa AS "nazwa czekoladki", substr(c.opis,1,40) AS "opis czekoladki"
FROM pudelka p LEFT JOIN zawartosc USING(idpudelka) LEFT JOIN czekoladki c USING(idczekoladki)
WHERE p.nazwa LIKE 'Kolekcja%';

--------4.5---------------

--1
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,40) AS "opis pudełka", cena, idczekoladki FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki USING(idczekoladki)
WHERE idczekoladki = 'd09';

--2
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,40) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki" FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE c.nazwa LIKE 'S%';

--3
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,20) AS "opis pudełka", cena, idczekoladki, c.nazwa AS "nazwa czekoladki", sztuk FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE sztuk >= 4;

--4
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", nadzienie FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE nadzienie IN ('truskawki');

--5
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", czekolada FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki) 
EXCEPT
SELECT p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", czekolada FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki) 
WHERE czekolada = 'gorzka';

--6
SELECT p.nazwa AS "nazwa pudelka", substr(p.opis,1,20) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", sztuk FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE c.nazwa = 'Gorzka truskawkowa' AND sztuk >= 3;

--7
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", orzechy FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki) 
EXCEPT
SELECT p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", orzechy FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki) 
WHERE orzechy IS NOT NULL;

--8
SELECT p.nazwa AS "nazwa pudelka", substr(p.opis,1,20) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", sztuk FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE c.nazwa = 'Gorzka truskawkowa';

--9
SELECT DISTINCT ON(p.nazwa) p.nazwa AS "nazwa pudelka", substr(p.opis,1,30) AS "opis pudełka", cena, c.nazwa AS "nazwa czekoladki", nadzienie FROM pudelka p JOIN zawartosc USING(idpudelka) JOIN czekoladki c USING(idczekoladki)
WHERE nadzienie IS NULL;

--------4.6---------------

--samozłączenie - Jak wskazuje nazwa, operacja ta powoduje utworzenie tabeli wynikowej w oparciu o iloczyn kartezjański tabeli z nią samą.

SELECT c2.idczekoladki, c2.nazwa, c2.koszt, c1.koszt AS "koszt d08" FROM czekoladki c2, czekoladki c1 
WHERE c1.idczekoladki = 'd08' AND c2.koszt > c1.koszt;	-- iloczyn kartezjański
--lub 
SELECT idczekoladki, nazwa, koszt FROM czekoladki WHERE koszt > (SELECT koszt FROM czekoladKi 
WHERE idczekoladki = 'd08');


--The SQL WITH clause allows you to give a sub-query block a name
WITH subquery AS (SELECT k1.nazwa AS "nazwa klienta", p1.nazwa AS "nazwa pudełka" FROM czekoladki c1 JOIN zawartosc USING(idczekoladki) JOIN pudelka p1 USING(idpudelka) JOIN artykuly USING(idpudelka) JOIN zamowienia USING(idzamowienia) JOIN klienci k1 USING (idklienta))
SELECT DISTINCT ON(s2."nazwa klienta") s2."nazwa klienta", s2."nazwa pudełka", s1."nazwa pudełka" AS "nazwa pudełka Alicji" FROM subquery s1, subquery s2
WHERE s1."nazwa klienta" = 'Górka Alicja' AND s2."nazwa klienta" != 'Górka Alicja' AND s1."nazwa pudełka" = s2."nazwa pudełka";

--lub
WITH GA AS (SELECT DISTINCT ON(p1.nazwa) k1.nazwa, p1.nazwa AS "nazwa pudełka alicji" FROM czekoladki c1 JOIN zawartosc USING(idczekoladki) JOIN pudelka p1 USING(idpudelka) JOIN artykuly USING(idpudelka) JOIN zamowienia USING(idzamowienia) JOIN klienci k1 USING (idklienta) WHERE k1.nazwa = 'Górka Alicja')  
SELECT DISTINCT ON(k.nazwa)  k.nazwa AS "nazwa klienta", p.nazwa AS "nazwa pudełka", GA."nazwa pudełka alicji" FROM czekoladki c JOIN zawartosc USING(idczekoladki) JOIN pudelka p USING(idpudelka) JOIN GA ON(p.nazwa = GA."nazwa pudełka alicji") JOIN artykuly USING(idpudelka) JOIN zamowienia USING(idzamowienia) JOIN klienci k USING (idklienta)
WHERE k.nazwa != 'Górka Alicja';


WITH subquery AS (SELECT k.nazwa klient, k.ulica AS "ulica", k.miejscowosc "miejscowość", p.nazwa "nazwa pudełka" FROM klienci k NATURAL JOIN zamowienia JOIN artykuly USING(idzamowienia) JOIN pudelka p USING(idpudelka))
SELECT DISTINCT ON(s2.klient) s2.klient, s2.miejscowość, s1."nazwa pudełka", s1.klient AS "klient z Katowic", s1.miejscowość, s1."nazwa pudełka" FROM subquery s1, subquery s2
WHERE s1.miejscowość = 'Katowice' AND s2.miejscowość != 'Katowice' AND s1."nazwa pudełka" = s2."nazwa pudełka" ; 


--------5.1---------------

SELECT COUNT(*) FROM czekoladki; 

SELECT COUNT(*) FROM czekoladki WHERE nadzienie IS NOT NULL;
--lub
SELECT COUNT(nadzienie) FROM czekoladki; --funkcje agregujące ignorują nulle

SELECT idpudelka, SUM(sztuk) FROM zawartosc GROUP BY idpudelka ORDER BY 2 DESC LIMIT 1;

SELECT idpudelka, SUM(sztuk) FROM zawartosc GROUP BY idpudelka;

SELECT idpudelka, SUM(sztuk) FROM zawartosc NATURAL JOIN czekoladki WHERE orzechy IS NULL GROUP BY idpudelka;

SELECT idpudelka, SUM(sztuk) FROM zawartosc NATURAL JOIN czekoladki WHERE czekolada='mleczna' GROUP BY idpudelka;

--------5.2---------------

SELECT idpudelka, SUM(masa*sztuk) FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka;

SELECT idpudelka, SUM(masa*sztuk) FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka ORDER BY 2 DESC LIMIT 1;

WITH masypudelek as ( SELECT idpudelka,SUM(masa*sztuk) AS "ms" FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka) 
SELECT AVG(masypudelek.ms) FROM masypudelek;

SELECT idpudelka, ROUND(AVG(masa),2) AS "średnia waga czekoladki [g]" FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka;

--------5.3---------------

SELECT datarealizacji, COUNT(datarealizacji) AS "liczba zamówień" FROM zamowienia
GROUP BY datarealizacji ORDER BY 1;

SELECT COUNT(idzamowienia) "łączna liczba zamówień" FROM zamowienia;

SELECT SUM(cena) AS "łączna wartość zamówień" FROM zamowienia NATURAL JOIN artykuly NATURAL JOIN pudelka;

SELECT klienci.nazwa, COUNT(idzamowienia) "liczba zamówień", SUM(cena) FROM klienci NATURAL JOIN zamowienia NATURAL JOIN artykuly JOIN pudelka USING(idpudelka) 
GROUP BY klienci.nazwa; 

--------5.4---------------

SELECT idczekoladki, COUNT(idczekoladki) AS "liczba pudełek" FROM zawartosc 
GROUP BY idczekoladki ORDER BY 2 DESC LIMIT 1;

SELECT idpudelka, COUNT(idczekoladki) "ilość czekoladek bez orzechów" FROM zawartosc NATURAL JOIN czekoladki 
WHERE orzechy IS NULL 
GROUP BY idpudelka ORDER BY 2 DESC LIMIT 1; 

SELECT idczekoladki, COUNT(idczekoladki) AS "liczba pudełek" FROM zawartosc 
GROUP BY idczekoladki ORDER BY 2 LIMIT 1;--ale jest czekoladka której nie ma w żadnym pudelku(b01)

SELECT idpudelka, COUNT(idpudelka) FROM artykuly
GROUP BY idpudelka ORDER BY 2 DESC LIMIT 1;

--------5.5---------------

SELECT EXTRACT(QUARTER FROM datarealizacji) AS "kwartał", COUNT(datarealizacji) AS "ilość zamówień" FROM zamowienia
GROUP BY 1;

SELECT 	DATE_PART('MONTH',datarealizacji) "miesiąc", COUNT(datarealizacji) "ilość zamówień" FROM zamowienia
GROUP BY 1 ORDER BY 1;

SELECT 	DATE_PART('WEEK',datarealizacji) "tydzień", COUNT(datarealizacji) "ilość zamówień" FROM zamowienia
GROUP BY 1 ORDER BY 1;

SELECT miejscowosc, COUNT(miejscowosc) "zamówień" FROM zamowienia NATURAL JOIN klienci
GROUP BY miejscowosc ORDER BY 1;

--------5.6---------------

SELECT SUM(masa*zawartosc.sztuk*artykuly.sztuk) FROM zawartosc NATURAL JOIN czekoladki JOIN artykuly USING(idpudelka);
--lub
WITH masypudelek AS (SELECT idpudelka, SUM(masa*sztuk) "masy" FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka)
SELECT SUM(masypudelek.masy*artykuly.sztuk) "łączna masa pudełek" FROM masypudelek JOIN artykuly USING(idpudelka);

SELECT SUM(zawartosc.sztuk*koszt*artykuly.sztuk) "łączna wartość pudełek" FROM zawartosc NATURAL JOIN czekoladki JOIN pudelka USING(idpudelka) JOIN artykuly USING(idpudelka);
--lub
WITH cenypudelek AS (SELECT idpudelka, SUM(sztuk*koszt) "ceny" FROM zawartosc NATURAL JOIN czekoladki GROUP BY idpudelka)
SELECT SUM(cenypudelek.ceny*artykuly.sztuk) "łączna wartość pudełek" FROM cenypudelek JOIN artykuly USING(idpudelka);

--------5.7---------------

SELECT idpudelka, cena-SUM(sztuk*koszt) "zysk" FROM czekoladki NATURAL JOIN zawartosc JOIN pudelka USING(idpudelka)
GROUP BY idpudelka,cena;

WITH zysk AS ( SELECT idpudelka, cena-SUM(zawartosc.sztuk*koszt) "zysk" FROM czekoladki NATURAL JOIN zawartosc JOIN pudelka USING(idpudelka) 
GROUP BY idpudelka,cena )--zysk na konkretnym pudelku
SELECT SUM(zysk.zysk*artykuly.sztuk) "łączny zysk z zamówień" FROM artykuly JOIN zysk USING(idpudelka);

WITH zysk AS ( SELECT idpudelka, cena-SUM(zawartosc.sztuk*koszt) "zysk" FROM czekoladki NATURAL JOIN zawartosc JOIN pudelka USING(idpudelka) 
GROUP BY idpudelka,cena )--zysk na konkretnym pudelku
SELECT SUM(zysk.zysk) "łączny zysk z pudełek" FROM zysk;

--------5.8---------------

SELECT COUNT(*), p2.idpudelka FROM pudelka p1, pudelka p2 
WHERE p1.idpudelka <= p2.idpudelka 
GROUP BY p2.idpudelka ORDER BY p2.idpudelka;



--------6.1---------------

INSERT INTO czekoladki VALUES('w98', 'Biały kieł', 'biała', 'laskowe', 'marcepan', 'Rozpływające się w rękach i kieszeniach.', 0.45, 20);

INSERT INTO klienci VALUES 
	(90, 'Matusiak Edward', 'Kropiwnickiego 6/3', 'Leningrad', '31-471','031 423 45 38'),
	(91, 'Matusiak Alina', 'Kropiwnickiego 6/3', 'Leningrad', '31-471','031 423 45 38'), 
	(92, 'Kimono Franek', 'Karatekow 8', 'Mistrz', '30-029', '501 498 324');

INSERT INTO klienci 
SELECT 93, 'Matusiak Iza', ulica, miejscowosc, kod, telefon FROM klienci 
WHERE nazwa='Matusiak Edward';

--------6.2---------------

INSERT INTO czekoladki VALUES('x91', 'Nieznana nieznajoma', null, null, null, 'Niewidzialna czekoladka wspomagajaca odchudzanie.', 0.26, 0);

INSERT INTO czekoladki VALUES('m98', 'Mleczny raj', 'mleczna', null, null, 'Aksamitna mleczna czekolada w ksztalcie butelki z mlekiem.', 0.26, 36);

--------6.3---------------

DELETE FROM czekoladki WHERE idczekoladki IN ('x91','m98');

INSERT INTO czekoladki(idczekoladki,nazwa,opis,koszt,masa) VALUES('x91', 'Nieznana Nieznajoma', 'Niewidzialana czekolada wspomagajaca odchudzanie',0.26,0);

INSERT INTO czekoladki(idczekoladki,nazwa,czekolada,opis,koszt,masa) VALUES('m98', 'Mleczny raj','mleczna', 'Aksamitna mleczna czekolada w ksztalcie butelki z mlekiem.',0.26, 36);

--------6.4---------------
 
UPDATE klienci SET nazwa='Nowak Iza' WHERE nazwa='Matusiak Iza';

UPDATE czekoladki SET koszt=koszt*0.9 WHERE idczekoladki IN ('w98','m98','x91');

UPDATE czekoladki SET koszt=
	(SELECT koszt FROM czekoladki WHERE idczekoladki='w98')
WHERE nazwa='Nieznana Nieznajoma';

UPDATE klienci SET miejscowosc='Piotrograd' WHERE miejscowosc='Leningrad';

UPDATE czekoladki SET koszt=koszt+0.15 WHERE SUBSTR(idczekoladki,2,2)::int > 90; --substr(string, from [, count])

--------6.5---------------

DELETE FROM klienci 
WHERE nazwa LIKE 'Matusiak%';

DELETE FROM klienci 
WHERE idklienta > 91;

DELETE FROM czekoladki 
WHERE koszt >= 0.45 OR masa >= 36 OR masa = 0;

--------6.6---------------

--skrypt66.sql
INSERT INTO pudelka VALUES('wint', 'Winter collection','kolekcja ziomowa', 25, 100), ('sume','Summer collection','kolekcja letnia', 26, 400);
INSERT INTO zawartosc VALUES('wint','d04', 3), ('wint','m01',4), ('wint','d08',3),('sume', 'b06', 5), ('sume','f02',5);

--\i skrypt66.sql

--------6.7---------------

--skrypt67a.sql
'spri' 'Spring collection.' 'kolekcja wiosenna' 0.35  41 
'lato' 'Lato collection' 'kolekcja ziomowa' 0.34 40
--skrypt67b.sql
'spri' 'd04' 3
'spri' 'm01' 4 
'spri' 'd08' 3
'lato' 'b06' 5
'lato' 'f02' 5
--skrypt67.sql
COPY pudelka FROM 'skrypt67a';
COPY zawartosc FROM 'skrypt67b';

--\i skrypt67.sql
--------6.8---------------

UPDATE zawartosc SET sztuk=sztuk+1 WHERE idpudelka IN ('wint','sume');

--skrypt68a.sql
UPDATE czekoladki SET czekolada='brak'  
WHERE czekolada IS NULL;

UPDATE czekoladki SET orzechy='brak'
WHERE orzechy IS NULL;

UPDATE czekoladki SET nadzienie='brak'
WHERE nadzienie IS NULL;
--\i skrypt68a.sql

--skrypt68b.sql
UPDATE czekoladki SET czekolada=NULL  
WHERE czekolada='brak';

UPDATE czekoladki SET orzechy=NULL
WHERE orzechy='brak';

UPDATE czekoladki SET nadzienie=NULL
WHERE nadzienie='brak';
--\i skrypt68B.sql
