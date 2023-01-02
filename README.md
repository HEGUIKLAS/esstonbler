# esstonbler
stack based esoteric programing language written in python, theoretically should be turing complete but not yet proven
instruction set in czech:
LDA – načte hodnotu na stack, následuje buďto instrukce ADR a číslo n, což načte číslo na adrese n, nebo VAL a číslo n, což na stack načte číslo n.
STA – uloží hodnotu do paměti, následuje buďto instrukce VAL a čísla n, k, což uloží číslo n na adrese k, nebo SCT a číslo n, což odstraní vrchní hodnotu ze stacku a uloží ji na adresu n.
PNT – vytiskne hodnoty na stacku
IMP – vloží na stack hodnotu kterou uživatel napíše
EXT – ukončí program
ADD – sečte vrchní dvě hodnoty ze stacku, odebere je a vloží místo nich výsledek
SUB – odečte vrchní dvě hodnoty ze stacku, odebere je a vloží místi nich  výsledek
DEF – vždy následuje FNC, poté jméno fukce (3 velká písmena a čísla) a její délka v řádkách (bez tohoto řádku)
EXE – provede funkci, vždy následuje FNC, poté jméno funkce.
IFF – následuje jeden z 6 operátorů: a potom EXE, FNC a jméno funcke. IFF odebere vrchní dvě hodnoty stacku a provede operaci, pokud vyjde pravda, spustí funkci.
	EGL – rovná se
	IGL – nerovná se
	SML – striktně menší
	BIG – striktně větší
	EOH – rovná se nebo větší
	EOS – rovná se nebo menší
WHL – následuje IFF (a všechno co je potřeba za IFF), pořád provádí IFF dokud operace vrací pravdu, pokud ne tak cyklus končí
program examples:
geusseing game:
IMP
STA SCT 1
LDA VAL 1
LDA VAL 1
DEF FNC AAA 2
    PNT
    EXT
DEF FNC GSS 5
    LDA ADR 1
    IMP
    IFF EQL EXE FNC AAA
    LDA VAL 1
    LDA VAL 1
WHL IFF EQL EXE FNC GSS

multiplication:
DEF FNC CNT 10 
    LDA ADR 1
    LDA ADR 4
    ADD
    STA SCT 4
    LDA ADR 3
    LDA VAL 1
    ADD
    STA SCT 3
    LDA ADR 3
    LDA ADR 2
DEF FNC AAA 3
    LDA ADR 3
    LDA ADR 2
    WHL SML EXE FNC CNT
DEF FNC SMB 3
    LDA VAL 0
    PNT
    EXT
DEF FNC MUL 17
    IMPX	
    STA SCT 1
    IMP
    STA SCT 2
    STA VAL 1 3
    LDA ADR 1
    STA SCT 4
    LDA ADR 1
    LDA VAL 0
    IFF EQL EXE FNC SMB
    LDA ADR 2
    LDA VAL 0
    IFF EQL EXE FNC SMB
    EXE FNC AAA
    LDA ADR 4
    PNT
    EXT
DEF FNC SMC 3
    LDA VAL 0
    PNT
    EXT
EXE FNC MUL
