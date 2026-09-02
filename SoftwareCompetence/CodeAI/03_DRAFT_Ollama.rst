.. Copyright (C) ALbert Mietus; 2026

.. image:: ScenerySketching-image6.png
   :class: codeai-head

:reading-time:  XXX

.. _CodeAI-Ollama:

=======================
Sovereignty with Ollama
=======================

.. post:: 2026/09/06
   :category: ScenerySketching
   :tags: CodeAI
   :location: Geldrop
   :language: en

   Frequently, SW engineers complain they aren’t allowed to use CodeAI, because *‘GDPR’* enforces strict rules on personal
   data --- as a result, all kinds of cloud services are forbidden by their organization.
   |BR|
   At the same time, there is a strategic risk in the operational habit of “uploading” all your embedded software to
   American AI providers, to gain a bit of productivity. The big question is: *Who is reading it?*

   Even when the contract mentions *“will not be used for ...”*, US law stands above that. By law, the US government can
   demand all that data. Secret agencies can demand a copy of our code, and even forbid the provider from mentioning it.

   This article will show that you can use CodeAI without disclosing any of your code. With a tool like ‘Ollama’, I can
   use CodeAI even in airplane mode!

.. include:: ./sidebar-ScenerySketching.irst

.. sidebar:: Maps & Milestones
   :class: sidebar-ScenerySketching

   Ollama is, like any AI-tool, in constant development. It started to *run* open LLMs locally ---and still
   does. Nowadays it also offers *"cloud models"* --- the same open-source/weigh models run on their
   servers. Using the same setup and API.
   |BR|
   It's a nice options to use bigger open-models, without investing in hardware, but less local. Still, it offers an
   transition path: start small local, try less-local bigger models, and invest in own hardware when it work and you
   need maximum sovereignty.

   Ollama is the best known tool for local, safe, sovereign LLMs, but not the only one. It is based on `Llama.cpp
   <https://en.wikipedia.org/wiki/Llama.cpp>`__, a library that comes with it own CLI-tool, and used by other tools as
   well.
   |BR|
   Also Apple's 'MLX' can me mentioned here. It used to be a alternative, but is now integrated in Ollama. Especially
   for Apple-computers this is interesting as its "unified memory design" fits very well for AI computing. That makes it
   realistic to run CodeAI in airplane-mode: it works fine on my M1-32G MacBook --- locally.


Remote CodeAI
=============

Most *ready-to-run* CodeAI tools heavily depend on the cloud. Even when using a local editor, all your code is uploaded
to an LLM, again and again. The same applies to your design and other IP you give to the AI-tool. And, as most cloud/tool
are owned by US businesses, those standard solutions may pose a potential security risk.
|BR|
Often, that risk is low. For example, when working on open-source software, or this blog. Or, there may be legal
constructs to mitigate that risk.

Sometimes, there are other reasons to avoid such a remote solution. Like networking capacity and other
technical limitations. Especially when working interactively (using *ghost code*), any (network) delay is annoying. Then a
local solution will be more speedy --- even  when the LLM runs on cheaper hardware.

The latest the greatest?
========================
Another pitfall is how AI-providers push the latest models; even I suffered from it recently ...

I use some AI-chats to validate my blog-postings. To find general typos, but also to check the “writing style” --- I
have one for every kind of blog. It always worked perfectly, using a ``*-latest`` (cloud) model ---basically an
*alias* to latest version. Until recently..
|BR|
It still worked, it found some mistakes. But somehow it didn't work as usual --- I didn't understand many of its remarks.

With no options left, I selected an older model; it worked perfectly again.
|BR|
With hindsight, it was almost trivial. I forgot the classic *“develop, test/accept, production” concept*,  and got used
to *“latest/greatest”* --- using a dev-version in production ....

Sure, I could have pinned to a *x.y* version; but I like to use the latest verified one (as we all are used to). But
``-latest`` isn't verified; it just the latest, not the greatest.
|BR|
This never happens to me when I use a local LLM; as I only install them after validating.


A Local LLM
===========

Many of those risks become smaller by using classic quality assurance approaches: Validate every tool and setup before
it's rolled out for production --- that is: test it before it’s rolled-out to all developers. Whether you formally test it, let
a few mature developers “play” with it, or just wait until others have used it, doesn't matter. My recommendation is
simple: use the normal processes also for AI-tools.

The question is of course: is that possible? Can we deploy a full CodeAI environment ourselves? Can we host an LLM on-site?

Without going in all the details, you have 2 options for a “local LLM”. Either deploy them in your server park, or run
on the developer's laptop. Both work, with pros and cons. Usually, the PC-local one is faster; the (on-premises)
server-local one can run bigger, more powerful LLMs. Both are safe and give you sovereignty by using the normal
network security you should have installed anyhow.

A Model is data
===============

The core of *CodeAI* is an LLM. And, an LLM is, as the name hints, a (Large Language) *Model* In plain English, it is
“data”, not “code”. One needs a program to run it. One can compare it to a horrendous behemothic spreadsheet: a huge file,
that needs (f.e.) Excel to process it.
|BR|
Only an LLM is bigger: even a small one is often about 10 Gigabytes! This implies you need a lot of RAM.


Some LLM’s are commercial, but there are also open-source (and/or open-weight) LLM’s. You can download them and use them
for free. And even adapt them to your needs, however most run fine out of the box.
|BR|
A well-known program to execute (and manage) those LLMs is `Ollama <https://ollama.com>`__;  which is `open-source itself
<https://github.com/ollama/ollama>`__ --- so you can even inspect it for quality and security issues (when you like the last mile).



..  LocalWords:  Ollama GDPR LLM LLMs
