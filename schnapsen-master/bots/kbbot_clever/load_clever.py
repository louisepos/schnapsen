from kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
# Jacks
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')

#Queens
Q0 = Boolean('q0')
Q1 = Boolean('q1')
Q2 = Boolean('q2')
Q3 = Boolean('q3')
Q4 = Boolean('q4')
Q5 = Boolean('q5')
Q6 = Boolean('q6')
Q7 = Boolean('q7')
Q8 = Boolean('q8')
Q9 = Boolean('q9')
Q10 = Boolean('q10')
Q11 = Boolean('q11')
Q12 = Boolean('q12')
Q13 = Boolean('q13')
Q14 = Boolean('q14')
Q15 = Boolean('q15')
Q16 = Boolean('q16')
Q17 = Boolean('q17')
Q18 = Boolean('q18')
Q19 = Boolean('q19')

#Kings
K0 = Boolean('k0')
K1 = Boolean('k1')
K2 = Boolean('k2')
K3 = Boolean('k3')
K4 = Boolean('k4')
K5 = Boolean('k5')
K6 = Boolean('k6')
K7 = Boolean('k7')
K8 = Boolean('k8')
K9 = Boolean('k9')
K10 = Boolean('k10')
K11 = Boolean('k11')
K12 = Boolean('k12')
K13 = Boolean('k13')
K14 = Boolean('k14')
K15 = Boolean('k15')
K16 = Boolean('k16')
K17 = Boolean('k17')
K18 = Boolean('k18')
K19 = Boolean('k19')

#Tens
T0 = Boolean('t0')
T1 = Boolean('t1')
T2 = Boolean('t2')
T3 = Boolean('t3')
T4 = Boolean('t4')
T5 = Boolean('t5')
T6 = Boolean('t6')
T7 = Boolean('t7')
T8 = Boolean('t8')
T9 = Boolean('t9')
T10 = Boolean('t10')
T11 = Boolean('t11')
T12 = Boolean('t12')
T13 = Boolean('t13')
T14 = Boolean('t14')
T15 = Boolean('t15')
T16 = Boolean('t16')
T17 = Boolean('t17')
T18 = Boolean('t18')
T19 = Boolean('t19')

#Aces
A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')

#Trump Tens
TT0 = Boolean('tt0')
TT1 = Boolean('tt1')
TT2 = Boolean('tt2')
TT3 = Boolean('tt3')
TT4 = Boolean('tt4')
TT5 = Boolean('tt5')
TT6 = Boolean('tt6')
TT7 = Boolean('tt7')
TT8 = Boolean('tt8')
TT9 = Boolean('tt9')
TT10 = Boolean('tt10')
TT11 = Boolean('tt11')
TT12 = Boolean('tt12')
TT13 = Boolean('tt13')
TT14 = Boolean('tt14')
TT15 = Boolean('tt15')
TT16 = Boolean('tt16')
TT17 = Boolean('tt17')
TT18 = Boolean('tt18')
TT19 = Boolean('tt19')

#Trump Ace
TA0 = Boolean('ta0')
TA1 = Boolean('ta1')
TA2 = Boolean('ta2')
TA3 = Boolean('ta3')
TA4 = Boolean('ta4')
TA5 = Boolean('ta5')
TA6 = Boolean('ta6')
TA7 = Boolean('ta7')
TA8 = Boolean('ta8')
TA9 = Boolean('ta9')
TA10 = Boolean('ta10')
TA11 = Boolean('ta11')
TA12 = Boolean('ta12')
TA13 = Boolean('ta13')
TA14 = Boolean('ta14')
TA15 = Boolean('ta15')
TA16 = Boolean('ta16')
TA17 = Boolean('ta17')
TA18 = Boolean('ta18')
TA19 = Boolean('ta19')

#Play Jack
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')

#Play Ten
PT0 = Boolean('pt0')
PT1 = Boolean('pt1')
PT2 = Boolean('pt2')
PT3 = Boolean('pt3')
PT4 = Boolean('pt4')
PT5 = Boolean('pt5')
PT6 = Boolean('pt6')
PT7 = Boolean('pt7')
PT8 = Boolean('pt8')
PT9 = Boolean('pt9')
PT10 = Boolean('j10')
PT11 = Boolean('pt11')
PT12 = Boolean('pt12')
PT13 = Boolean('pt13')
PT14 = Boolean('pt14')
PT15 = Boolean('pt15')
PT16 = Boolean('p16')
PT17 = Boolean('pt17')
PT18 = Boolean('pt18')
PT19 = Boolean('pt19')

#Play Trump Ace
PTA0 = Boolean('pta0')
PTA1 = Boolean('pta1')
PTA1 = Boolean('pta1')
PTA2 = Boolean('pta2')
PTA3 = Boolean('pta3')
PTA4 = Boolean('pta4')
PTA5 = Boolean('pta5')
PTA6 = Boolean('pta6')
PTA7 = Boolean('pta7')
PTA8 = Boolean('pta8')
PTA9 = Boolean('pta9')
PTA10 = Boolean('pta10')
PTA11 = Boolean('pta11')
PTA12 = Boolean('pta12')
PTA13 = Boolean('pta13')
PTA14 = Boolean('pta14')
PTA15 = Boolean('pta15')
PTA16 = Boolean('pta16')
PTA17 = Boolean('pta17')
PTA18 = Boolean('pta18')
PTA19 = Boolean('pta19')

#Play Trump Tens
PTT0 = Boolean('ptt0')
PTT1 = Boolean('ptt1')
PTT2 = Boolean('ptt2')
PTT3 = Boolean('ptt3')
PTT4 = Boolean('ptt4')
PTT5 = Boolean('ptt5')
PTT6 = Boolean('ptt6')
PTT7 = Boolean('ptt7')
PTT8 = Boolean('ptt8')
PTT9 = Boolean('ptt9')
PTT10 = Boolean('ptt10')
PTT11 = Boolean('ptt11')
PTT12 = Boolean('ptt12')
PTT13 = Boolean('ptt13')
PTT14 = Boolean('ptt14')
PTT15 = Boolean('ptt15')
PTT16 = Boolean('ptt16')
PTT17 = Boolean('ptt17')
PTT18 = Boolean('ptt18')
PTT19 = Boolean('ptt19')

#PlayCheap card (K, Q or J)
PC0 = Boolean('pc0')
PC1 = Boolean('pc1')
PC2 = Boolean('pc2')
PC3 = Boolean('pc3')
PC4 = Boolean('pc4')
PC5 = Boolean('pc5')
PC6 = Boolean('pc6')
PC7 = Boolean('pc7')
PC8 = Boolean('pc8')
PC9 = Boolean('pc9')
PC10 = Boolean('pc10')
PC11 = Boolean('pc11')
PC12 = Boolean('pc12')
PC13 = Boolean('pc13')
PC14 = Boolean('pc14')
PC15 = Boolean('pc15')
PC16 = Boolean('pc16')
PC17 = Boolean('pc17')
PC18 = Boolean('pc18')
PC19 = Boolean('pc19')

#Trump Queens
TQ0 = Boolean('tq0')
TQ1 = Boolean('tq1')
TQ2 = Boolean('tq2')
TQ3 = Boolean('tq3')
TQ4 = Boolean('tq4')
TQ5 = Boolean('tq5')
TQ6 = Boolean('tq6')
TQ7 = Boolean('tq7')
TQ8 = Boolean('tq8')
TQ9 = Boolean('tq9')
TQ10 = Boolean('tq10')
TQ11 = Boolean('tq11')
TQ12 = Boolean('tq12')
TQ13 = Boolean('tq13')
TQ14 = Boolean('tq14')
TQ15 = Boolean('tq15')
TQ16 = Boolean('tq16')
TQ17 = Boolean('tq17')
TQ18 = Boolean('tq18')
TQ19 = Boolean('tq19')

#Trump Kings
TK0 = Boolean('tk0')
TK1 = Boolean('tk1')
TK2 = Boolean('tk2')
TK3 = Boolean('tk3')
TK4 = Boolean('tk4')
TK5 = Boolean('tk5')
TK6 = Boolean('tk6')
TK7 = Boolean('tk7')
TK8 = Boolean('tk8')
TK9 = Boolean('tk9')
TK10 = Boolean('tk10')
TK11 = Boolean('tk11')
TK12 = Boolean('tk12')
TK13 = Boolean('tk13')
TK14 = Boolean('tk14')
TK15 = Boolean('tk15')
TK16 = Boolean('tk16')
TK17 = Boolean('tk17')
TK18 = Boolean('tk18')
TK19 = Boolean('tk19')

#Play Trump Wedding (Trump King + Trump Queen)
PTW0 = Boolean('ptw0')
PTW1 = Boolean('ptw1')
PTW2 = Boolean('ptw2')
PTW3 = Boolean('ptw3')
PTW4 = Boolean('ptw4')
PTW5 = Boolean('ptw5')
PTW6 = Boolean('ptw6')
PTW7 = Boolean('ptw7')
PTW8 = Boolean('ptw8')
PTW9 = Boolean('ptw9')
PTW10 = Boolean('ptw10')
PTW11 = Boolean('ptw11')
PTW12 = Boolean('ptw12')
PTW13 = Boolean('ptw13')
PTW14 = Boolean('ptw14')
PTW15 = Boolean('ptw15')
PTW16 = Boolean('ptw16')
PTW17 = Boolean('ptw17')
PTW18 = Boolean('ptw18')
PTW19 = Boolean('ptw19')

def general_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
     kb.add_clause(J4)
     kb.add_clause(J9)
     kb.add_clause(J14)
     kb.add_clause(J19)

     #These are Queens
     kb.add_clause(Q3)
     kb.add_clause(Q8)
     kb.add_clause(Q13)
     kb.add_clause(Q18)

     #These are Kings
     kb.add_clause(K2)
     kb.add_clause(K7)
     kb.add_clause(K12)
     kb.add_clause(K17)

     #These are 10s
     kb.add_clause(T1)
     kb.add_clause(T6)
     kb.add_clause(T12)
     kb.add_clause(T16)

     #These are Aces
     kb.add_clause(A0)
     kb.add_clause(A5)
     kb.add_clause(A10)
     kb.add_clause(A15)

    #The bot itself will add clauses about what is a
    #   trump queen
    #   trump king
    #   trump ace


def strategy_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Add clauses (This list is sufficient for this strategy)
    # PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
    # In other words that the PJ strategy should play a card when it is a jack

    #CHEAPCARD STRATEGY
     kb.add_clause(~J2, PC2)
     kb.add_clause(~Q2, PC2)
     kb.add_clause(~K2, PC2)

     kb.add_clause(~J3, PC3)
     kb.add_clause(~Q3, PC3)
     kb.add_clause(~K3, PC3)

     kb.add_clause(~J4, PC4)
     kb.add_clause(~Q4, PC4)
     kb.add_clause(~K4, PC4)

     kb.add_clause(~J7, PC7)
     kb.add_clause(~Q7, PC7)
     kb.add_clause(~K7, PC7)

     kb.add_clause(~J8, PC8)
     kb.add_clause(~Q8, PC8)
     kb.add_clause(~K8, PC8)

     kb.add_clause(~J9, PC9)
     kb.add_clause(~Q9, PC9)
     kb.add_clause(~K9, PC9)

     kb.add_clause(~J12, PC12)
     kb.add_clause(~Q12, PC12)
     kb.add_clause(~K12, PC12)

     kb.add_clause(~J13, PC13)
     kb.add_clause(~Q13, PC13)
     kb.add_clause(~K13, PC13)

     kb.add_clause(~J14, PC14)
     kb.add_clause(~Q14, PC14)
     kb.add_clause(~K14, PC14)

     kb.add_clause(~J17, PC17)
     kb.add_clause(~Q17, PC17)
     kb.add_clause(~K17, PC17)

     kb.add_clause(~J18, PC18)
     kb.add_clause(~Q18, PC18)
     kb.add_clause(~K18, PC18)

     kb.add_clause(~J19, PC19)
     kb.add_clause(~Q19, PC19)
     kb.add_clause(~K19, PC19)

     kb.add_clause(J2, Q2, K2, ~PC2)
     kb.add_clause(J3, Q3, K3, ~PC3)
     kb.add_clause(J4, Q4, K4, ~PC4)
     kb.add_clause(J7, Q7, K7, ~PC7)
     kb.add_clause(J8, Q8, K8, ~PC8)
     kb.add_clause(J9, Q9, K9, ~PC9)
     kb.add_clause(J12, Q12, K12, ~PC12)
     kb.add_clause(J13, Q13, K13, ~PC13)
     kb.add_clause(J14, Q14, K14, ~PC14)
     kb.add_clause(J17, Q17, K17, ~PC17)
     kb.add_clause(J18, Q18, K18, ~PC18)
     kb.add_clause(J19, Q19, K19, ~PC19)

    #PLAY TRUMP TEN
     kb.add_clause(~TT1, PTT1)
     kb.add_clause(~TT6, PTT6)
     kb.add_clause(~TT11, PTT11)
     kb.add_clause(~TT16, PTT16)
     kb.add_clause(~PTT1, TT1)
     kb.add_clause(~PTT6, TT6)
     kb.add_clause(~PTT11, TT11)
     kb.add_clause(~PTT16, TT16)

    #PLAY TRUMP ACE
     kb.add_clause(~TA0, PTA0)
     kb.add_clause(~TA5, PTA5)
     kb.add_clause(~TA10, PTA10)
     kb.add_clause(~TA15, PTA15)
     kb.add_clause(~PTA0, TA0)
     kb.add_clause(~PTA5, TA5)
     kb.add_clause(~PTA10, TA10)
     kb.add_clause(~PTA15, TA15)

     #PLAY TEN
     kb.add_clause(~T1, PT1)
     kb.add_clause(~T6, PT6)
     kb.add_clause(~T11, PT11)
     kb.add_clause(~T16, PT16)
     kb.add_clause(~PT1, T1)
     kb.add_clause(~PT6, T6)
     kb.add_clause(~PT11, T11)
     kb.add_clause(~PT16, T16)

     #PLAY JACK
     kb.add_clause(~J4, PJ4)
     kb.add_clause(~J9, PJ9)
     kb.add_clause(~J14, PJ14)
     kb.add_clause(~J19, PJ19)
     kb.add_clause(~PJ4, J4)
     kb.add_clause(~PJ9, J9)
     kb.add_clause(~PJ14, J14)
     kb.add_clause(~PJ19, J19)