Hello World using a Genetic Algorithm
===================


This is my first time messing around with genetic algorithms and demonstrates the oh-so-beloved "Hello World" program.


Resources
-------------

I learned about this topic and how to program this from a blog by Ferry Boender found [here](http://www.electricmonk.nl/log/2011/09/28/evolutionary-algorithm-evolving-hello-world/)

Running the program
-------------

    $python2 geneticHello.py
  

Output
------
The output should start by showing all the mutations that improve the fitness score of the string. The first column shows the generation it is on. The second shows its fitness score (how close it is to the target string "Hello, World!"). The third column shows the string.

    1 23700  at!Ph;`fn23Xc
    5 23677  at!Ph;`fn23Yc
    7 23648  at!Ph:`fn23Yc
    18 23517  at!Ph:`fn23Yb
    21 23404  at!Ph:`fn24Yb
    26 23277  at!Ph:_fn24Yb
    30 23150  at!Ph:_fn34Yb
    37 23101  `t!Ph:_fn34Yb
    48 23054  _t!Ph:_fn34Yb
    49 22943  _t!Ph:_fn35Yb
    54 22814  _t!Ph:_fn35Ya

After many many mutations, we see that our program matches the target string when the fitness score is 0. We have used evolution to print out "Hello World"

     2754    40  Heflo,"World!
     2767    37  Heflo,!World!
     2772    26  Heglo,!World!
     2792    17  Hehlo,!World!
     2806    16  Hehlo, World!
     2811     9  Heilo, World!
     2812     4  Hejlo, World!
     2851     1  Heklo, World!
     2865     0  Hello, World!

Is Neat.
