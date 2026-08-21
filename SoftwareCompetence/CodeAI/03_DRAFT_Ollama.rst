.. Copyright (C) ALbert Mietus; 2026

.. image:: ScenerySketching-image6.png
   :class: codeai-head

:reading-time:  XXX		

=======================
Sovereignty with Ollama
=======================

.. post:: 2026/09/06
   :category: ScenerySketching
   :tags: CodeAI
   :location: Geldrop
   :language: en

   Frequently, SW engineers complain they aren’t allowed to use CodeAI, as *‘GDPR’* enforces strict rules on personal
   data --- as a result, all kinds of cloud services are forbidden by the organization.
   |BR|
   At the same time, there is a strategic risk in the operational habit of “uploading” all your embedded software to
   American AI providers, to gain a bit of productivity. The big question is: *Who is reading it?*

   Even when the contract mentions *“will not be used for ...”*, US law stands above that --- and by law, the US
   government can demand all that data. Secret agencies can demand a copy of our code, and even forbid your provider
   from mentioning it.

   This article will show that you can use CodeAI without disclosing any of your code. With tools like ‘Ollama’, you can
   run it even on your laptop in airplane mode!

.. include:: ./sidebar-ScenerySketching.irst

.. sidebar:: Maps & Milestones
   :class: sidebar-ScenerySketching
   
   XXX XXX XXX			
   
   In ca 100 woorden: wat achtergrond e/o links naar (eigen/externe) voorbeelden, als brug naar actie.

Remote CodeAI
=============

Most *ready-to-run* CodeAI tools heavily depends on the cloud. Even when using a local editor, all your code is uploaded
to an LLM, again and again. The same applies to your design, and other IP you give to the AI-tool. And, as most cloud/tool
are owned by US-business, those standard solutions may have a potential security-risk.
|BR|
Often, that is risk is low. For example, when working on open-source software, of this blog. Or, there may be legal
constructs to mitigate that risk.

Sometimes, there are other reasons to avoid such an remote solution. Like networking capacity and other
technical limitation. Especially when working interactively (using *ghost code*), any (network) delay is annoying, a
local solution will be more speedy --- even  when the LLM runs on cheaper hardware.

The latest the greatest?
========================
Another pitfall it how AI-providers push the latest models -- even I suffered from it lastly ...

I use some AI-chats to validate my blog-postings. To find general typo’s, but also to check the “writing style” ---I
have one for every (kind) of blog. It normally works perfectly, using a ``*-latest``(cloud) model. Until recently. It
still worked, it found some mistakes. But somehow I wasn't perfect; it did a bad job.
|BR|
With no options left I selected an older model: it worked perfectly again.

With hindsight, it almost trivial. I forgot the classic *“develop, test/accept, production” concept*,  and got used to *“latest
/greatest”* -- using a dev-version in production ....

Sure, I could have pinned the *x.y* version; but I like to use the lasted verified one (as we all are used to).
|BR|
It happens only to me, when using a cloud-LLM, as all my local LLMs are validated before I install them.

A Local LLM
===========

Many of those risks become smaller by using classic quality assurance approaches: Validate every tool and setup before
it rolled out for production -- that test it before it’s rolled-out to all developers. Whether you formally test it, let
a few mature developers “play” with it, or just wait until other have used it, doesn't matter. My recommendation is
simple: use the normal processes also for AI-tools.

The question is of-cause: is that possible? Can we deploy a full CodeAI environment our-self? Can we host an LLM on-side?

Without going in all the details, you have 2 options for a “local LLM”. Either deploy them in your server-park, or run
on the developers laptop. Both work, with pros and cons. Usually, the PC-local one is faster, the (on-premises)
server-local one can run bigger, more powerful LLMs. Both are save and give you sovereignty, by using the normal
network-security you should have installed anyhow.

A Model is data
===============

The core of *CodeAI* is a LLM. And, a LLM is, as the name hints, a (Large Language) *Model* In plain English, it is
“data”, not “code”. One need a program to run it ---- horrendous behemothic spreadsheet: a huge file, that needs (f.e.)
Excel to process it.
|BR|
Only a LLM is bigger: even a small one is often about 10MByte! This implies you need a lot of RAM.

Some LLM’s are commercial, but there are also open-source (and/or open-weight) LLM’s. You can download them and use the
for free. And even adapt them you your needs ----however most run fine out of the box.
|BR|
A well-known program to execute (and manage) those LLM is `Ollama <https://ollama.com>`__;  which is `open-source itself
<https://github.com/ollama/ollama>`__ ---- so, you can even inspect it on quality and security issues (when you like the last mile).












==========

Nog toevoegen
=============


Left overs
----------
* the influence of popular movies, but I wouldn't take that risk
* And so, controlling what happens with that know-how can be important.

* See you soon; keep using your own synapses too--ALbert   

..  LocalWords:  Ollama GDPR LLM LLMs MByte
