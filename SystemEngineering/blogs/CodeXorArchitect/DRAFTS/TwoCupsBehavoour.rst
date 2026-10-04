.. Copyright (C) ALbert Mietus, 2026

.. image:: images/TwoCupsbehavior.png
   :width: 100%


Two Cups behaviour
=================

.. post:: 
   :tags: CodeXorArchitect
   :category: LinkedIn-Post

   :reading-time:	ToDo
   :LinkedIn: 		ToDo

   I always wonder why the *Ultimo Superior Brewmaster* luxury coffee machines only discover they are low on water after
   brewing the first shot when the double-cup option is selected. Its water sensor can differentiate
   between espresso and regular coffee, but somehow it forgets that two cups need more water too.
   |BR|
   What a stupid behaviour!

Without a doubt, it's a software flaw ---almost all *un-behavior* is software-related. Still, when I ask my development
team (or actually: my training class), all TTD tests pass. The problem isn't the code; it's how we deal with constantly
changing features.  Nowadays, we tend to solve the current "stories" without designing the product as a whole. When the
"double" feature was added, the test for the water sensor already passes.
|BR|
Both features work --- nobody asked for the combination.

How can we solve this unintentional behavior? That is simple: describe it. Not only what we need, but also what we
dislike.  "*Given two cups of coffee are selected, and there is enough water, then both cups are made in one go*", and
"When the water level is low, ask the user to fill the tank before starting to brew".
|BR|
A BDD expert can phrase it more formally. But even those informal 'needs' will drive the engineers in the right direction!





Architecture isn't just technology; it’s about solutions that make the machinery work.

|BR|





#CodeXorArchitect -- Your #TechFluencer

---



..  LocalWords:  TechFluencer Brewmaster un-behavior  BDD TTD
