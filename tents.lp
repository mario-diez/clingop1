#const n = 6.

col(1..n).
row(1..n).

tent(X,Y) :- row(X), col(Y).

:- tent(X, Y), tent(X, Y1), |Y - Y1| == 1.
:- tent(X, Y), tent(X1, Y), |X - X1| == 1.
:- tent(X, Y), tent(X1, Y1), |X - X1| == 1, |Y - Y1| == 1.  

#show tent/2.
