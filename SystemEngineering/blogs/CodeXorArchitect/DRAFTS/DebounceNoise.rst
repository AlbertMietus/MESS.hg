.. Copyright (C) ALbert Mietus, 2026

.. .. image:: images//DebounceNoise.png  .. TO BE DONE
   :width: 100%


Debounce Noise
==============


.. post:: 
   :tags: CodeXorArchitect
   :category: LinkedIn-Post

   :reading-time:	ToDo
   :LinkedIn: 		ToDo

   .. 336 words from here

   Everybody likes to push buttons. And every engineer knows you must debounce them. Or we get a lot of noise. But who
   decides how to do that? Is there a best strategy?

   Today we do a deep dive and consider all details that might be architecturally important. And, as we will see, we
   might even find some noise in the organization.

Roughly, there are two options: an (RC) filter in electronics, or a bit of software -- both with several variants. Both
an electrical engineer and an (embedded) software professional can implement them in a couple of hours. 
|BR|
But which *technical* solution is the best option? And what is ‘best’?

Suppose we are designing a high-volume, long-lasting, luxurious, self-powered device. This implies the ‘BOM’ should be
low, and that it runs *for years* on a battery, possibly using energy harvesting.
|BR|
Now look to those buttons again: how can we minimize cost and power use at the same time?

Any solution with fewer components will be cheaper -- that votes for a software solution. But software needs an active
processor, using power. Whereas ‘long-lasting, low power’ calls for a CPU that is mostly in deep sleep. Pulling the
switch every 10ms will drain the battery!
|BR|
Where the (RC) filter doesn't use energy --- unless the button is pressed.

Long story short: You need an estimate of how often & long the buttons are pressed to calculate how many
µC will be used every day and per *push*.
|BR|
And you need the exact details on how the buttons are connected to the MCU, and the algorithm used, to estimate how
often the processor will be awake. Only then, you can determine what s the best option!

A great embedded systems architect will surely do so beforehand.
|BR|
There is one other option, with two possible outcomes -- here comes the noise. Leave it to the two departments. Either
the engineers solve it, or both bureaucrats know it the other sides issue ...




#CodeXorArchitect -- Your #TechFluencer

---


Zie `~/work/MIJN.docs/MoreBlogs/0.meta/2.CodeXorArchitect.rst` (etc) voor info.

* Plaatje voor linkedIn maken met `~/work/MIJN.docs/tools/AddText-toHeaderImage.html`
* Basis: ~/work/MESS,hg/SystemEngineering/blogs/CodeXorArchitect/images/base/CodeXorArchitect-header-1128x368.png
* The kop/title (met spaces) er overheen. #CodeXorArchitect als reeks

..  LocalWords:  TechFluencer debounce  µC
