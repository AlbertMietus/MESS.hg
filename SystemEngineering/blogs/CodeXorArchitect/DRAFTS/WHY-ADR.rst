. Copyright (C) ALbert Mietus, 2026

.. image:: images/WhyTheADR.png
   :width: 100%


Why? the ADR!
=============

.. post:: 20/Oct/2026
   :tags: CodeXorArchitect
   :category: LinkedIn-Post

   :reading-time:	1min46
   :LinkedIn: 		ToDo
   :status:			RC3

   June 1996: The maiden flight of Ariane 5 --a €666M rocket-- failed, with a big explosion!
   |BR|
   But **Why**?

   You probably remember: it was a software flaw. An expensive one, but not a very complicated one. Or, as studies show,
   a couple of them. Some *dead code*, a calculation *overflow*, and faulty *error handling*. Each of them shouldn't
   happen ---but can you guarantee that your system doesn't have them?

   But **Why**? Why did the code have those kinds of stupid mistakes?
   |BR|
   Or maybe more importantly: How can you, as an architect, prevent them?

Expensive flaws are hardly ever introduced during coding. In an unpublished investigation, I showed that over 2 in 3
field-hits are *“pre-coding”*. That is, the specification, architecture or design documents almost *demand* the bug to
happen. And it seems that the larger the blunder, the earlier it was made.

The Ariane 5 reused code from the Ariane 4 without much discussion or documentation. “It worked” was the main
argument. The specs of the ‘4’ and ‘5’ are totally different, however. The existing code didn't need to work with the
much higher speeds of the Ariane 5. A disaster waiting to happen.

**Why** is this relevant? Maybe because you recognize them: aren't these the kinds of misses everybody makes? How can we
learn to avoid them?
|BR|
I give you two simple concepts: “**5 Whys**” and the “**ADR**” (*Architecture Decision Records)*. Both are lean and
agile. They make you a better architect.

For every bug that escapes the sprint, ask yourself and the team: Why? Why did it happen? Why didn't we find it? And
keep digging until you find the root cause. Typically, you need 5 levels ---hence the name.
|BR|
Don't do it to blame someone; do it to understand. And to fix it forever.

The ADR works proactively. It documents **WHY** decisions are made, including the context & drivers, the considered
options, the outcome and next steps. Keep it simple, not technical.
|BR|
Maybe a technically superior solution exists, but there was no time to implement it. Write it down! For the ‘4’, the
chosen one was adequate!

One day, there will be a ‘5’, then you spend maybe half a day writing a new ADR.  Option 1: reuse as is, with a small
risk: the €666M bug. Option 2: rework; will cost a few days more ---no big bang. Option 3: ...
|BR|
Even the writing itself will help.

Plenty of examples are freely available. Look them up today and start tomorrow.
|BR|
Please do! **Why?** *Because!* If you don’t, who will?








#CodeXorArchitect -- Your #TechFluencer

---



..  LocalWords:  TechFluencer Ariane ADR
