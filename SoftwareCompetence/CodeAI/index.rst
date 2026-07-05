.. image:: ScenerySketching-image6.png
      :width: 100%

.. include:: ./sidebar-ScenerySketching.irst

.. sidebar:: Maps & Milestones
   :class: sidebar-ScenerySketching

   Throughout this series, I will test these concepts against the reality of designing a complex sovereign software
   product: `CCastle <https://docideas.mietus.nl/en/default/CCastle>`__; another, long-running, ambitious
   side-project. Here, I’m aiming to build a tool-chain for a new language, based on ‘CC’ ---the successor of ‘OO’. I
   can indeed use the assistance of a few (artificial) teams.
   |BR|
   Both to code, but mainly to engineer (design, brainstorm, test, ...).

   As we integrate CodeAI into our generic toolbox, we face some extra non-negotiable constraints, that will need
   special attention (as they are less obvious for CCastle).

   #. **Maintainability**:
      Big, long living code-bases do change often over time. Every modification has to be checked and traced (see:
      :ref:`RequirementsTraceability`). Even CodeAI should not change lines, when not needed.

   #. **Auditability**:
      A "black box" is a liability; especially in regulated domains. But it applies to any commercial software.
      |BR|
      This includes questions like: *‘Are we allowed to use this code?’* As CodeAI is usually trained with open-source,
      whose copyrights might create conflicts.

   #. **Sovereignty**:
      The AI tech-bros promote their all-in-one solutions, making us vulnerable to vendor lock-in. Sometimes that is
      fine, sometimes it's not.
      |BR|
      In all cases it should be a deliberate choice -- and we should be able to change that later.



.. _ScenerySketching_CodeAI:

Scenery Sketching:: CodeAI
==========================

The software world is changing rapidly. Some believe that bots will take over coding. Others see **(gen)AI** as a
threat, pointing to the amount of energy it consumes, or to the risk that computers will supersede humans. Those
are all big words, and to me, they are mostly driven by fear and marketing.

In this series, I will sketch the “CodeAI” scenery --- at the architectural level. For a moment, we set the great
*all-in-one solutions* of the AI tech-bros aside. To study the options: what are the interfaces, what are the parts and
parcels we can use to build complicated, high-tech software systems, using generative AI. Our goal is to have
options --- and we need alternatives.

Sometimes, an integrated cloud solution is fine. But what if your software shouldn't leave the premises?  Can we ---when
inventing a bespoke embedded system--- trust the output of common “statistical apparatus”?  Given it involves new
hard- and software, how likely is it that “recycling existing code” will comply to our new specifications?

The core question is: Can we build a flexible team of bots suited to the technical complications of the embedded
systems we build? (And does it speed up development).
|BR|
Therefore, we should be able to look under the bonnet ...


Architecting the Horizon
------------------------

Looking to history, all big changes have come with huge promises and burdens. Seldom were those judgments based on
facts --- it was simply too early to call. In due time, we will see the debate on ‘CodeAI’ in the same way. But, how can
we reason about that future today?
|BR|
Doubtless, some simple coding work can be automated -- this is a normal way forward, as we like to “automate”.

But software engineering is more than writing code, a lot more. In particular for “:term:`sovereign software`” ---which
includes embedded software--- ‘engineering’ is *thinking*: Understanding the needs, grasping the possibilities of the
hardware, comparing the options, and aligning it with others, takes most of our time. When we comprehend all that,
writing the code is almost trivial. Personally, I’m glad when bots can do the boring parts.

Remember, we might be at the dawn of big changes ahead. I can’t predict the future. But, I have the skills to
investigate. I will look to the options, examine the new *(meta)* **interfaces** and share this ‘blueprint’. I hope it
helps me -- and you-- to sketch the future a bit better. Still, we are navigating uncertainty, but now with a few facts.


Articles
---------

See below for the current articles, expect more soon.
You can also find the last ones in the navigation bar (:ref:`Recent Posts <blog-posts>`)


.. toctree::
   :glob:
   :titlesonly:

   [0-9][0-9]*

Cooperation
-----------

Feel free to disagree, share your ideas below every post, and to request new “topics” in the comments field below.


..  LocalWords:  CCastle
