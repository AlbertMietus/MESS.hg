.. Copyright (C) ALbert Mietus, 2026

.. image:: images/TwoCupsBehavior.png
   :width: 100%


Two Cups Behaviour
==================

.. post:: 
   :tags: CodeXorArchitect
   :category: LinkedIn-Post

   :reading-time:	ToDo
   :LinkedIn: 		ToDo

   I always wonder why the *Ultimo Superior Brewmaster* luxury coffee machines only discover they are low on water after
   brewing the first shot when the double-cup option is selected. Its water sensor can differentiate between espresso
   and regular coffee, but somehow it forgets that two cups need more water too.
   |BR|
   What a stupid behaviour!

Without a doubt, it's a software flaw ---almost all *misbehaviour* is software-related. Still, when I ask my development
team (or actually: my training class), all TDD tests pass. The problem isn't in the code, however. It's about how we
deal with constantly changing features. When the water sensor story is 'done' long before the "double" option was
requested, we tend to implement it, including some (new) tests.

Unlike in the old days ---when architecture and design were finished before coding started--- we now do all phases
concurrently in each sprint. We also tend to forget to design the product as a whole. As nobody asked for the
combination, both features will work, but not the couple.
|BR|
TDD, when applied correctly, defines and validates the technical parts needed for the device. It proves the code is
correct, not that we build the right system.

How can we solve this unintentional behaviour? That is simple: describe it. Not only what we need, but also what we
dislike.  "*Given two cups of coffee are selected, and there is enough water, then both cups are made in one go*", and
"When the water level is low, ask the user to fill the tank before starting to brew".
|BR|
A BDD expert can phrase it more formally. But even those informal 'needs' will drive the engineers in the right direction!

With a nested double-loop of *Behaviour-* and *Test-Driven Development* ('B&TDD'), the high-level 'needs' explain the
requested behaviour of the parts, and thus define the TDD tests --- even when extra stories are added later.
|BR|
This yields in structure, and like the old architecture documents did.

Architecture isn't just technology; it’s about solutions that make the machinery work.
|BR|
When you want to become a genuine architect, you should learn to coach your team to follow the correct path ---for
example, with *B&TDD*. That is why I designed this "USB-practice" carefully.  It's no wonder the machinery never works;
it is an intended pitfall.





#CodeXorArchitect -- Your #TechFluencer

---



..  LocalWords:  TechFluencer Brewmaster  BDD TTD ALbert
