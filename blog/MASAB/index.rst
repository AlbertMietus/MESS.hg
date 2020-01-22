======================================
Modern, Agile System-Architecting Blog
======================================

.. toctree::
   :hidden:
   :glob:

   *
   */index

.. post:: 2019/6/18
   :category: MASAB
   :location: Eindhoven
   :language: en
   :tags: MASAB, Natrix

   To share my experience and vision as System-Architect I will design [#architect-verb]_ the “:term:`Natrix`” and blog about it in this :term:`MASAB` blog. For
   practical reasons :term:`Natrix` will be implemented mostly in (open-source) software. This enable readers to use/continue/experiment and help (without
   cost). This system is also chosen to demonstrate modern approaches in system-architecting.


What is System-Architecting?
============================

System-Architecting is --*to cut some corners short*-- the architectural-phase of system-engineering; which is the science to analyse and design a complex,
multidisciplinar system.
|BR|
Or even more simple. Solving to puzzle:

  Which parts of a not-yet-existing apparatus should be realised, in mechanical, electrical, software components (to name a few); such that at
  the end of the project it is economical affordable, and can be validated to requirements can’t be envisioned yet.


This is not an easy profession. And it is hard to learn; as it always about big, complex systems. A “hello wold” exemple is hard to
imagine.
|BR|
Therefore one often speaks about “an **art**”; not a discipline. Still, it is becoming more and more important for an R&D organisation: each new system is
bigger, and more complex and the current ones.

What is *Modern*  System-Architecting?
--------------------------------------

In the past, the *V-model* was mostly executed sequential; implying the architectural-phase had to be finalised before realisation could start. The agile
movement has shown there is an alternative, better approach.  This is sometimes called *concurrent engineering*. There are more way to modernisation, however.

Currently, systems are becoming connected to other systems; creating systems-of-systems. Where each system is independently designed. It’s no longer possible to
develop a system *top-down*; when one has a  requirement as ‘works with others. Whenever such ‘other’ system hits te market before our one, we have to adapt and
make ours compatible with that newcomer.

Similarly, the open-source-world has created a environment where one has to restrict architecture-choices to be able to use those ‘free’ components. More and
more such ‘open’ components become available in other developments. By example, an (industrial version of the) `Raspberry Pi
<https://www.raspberrypi.org/products/compute-module-3-plus/>`_ can help to shorten the time-2-market, which can be a requirement for the system-architect.
|BR|
The question however is: How to incorporate this (implementation detail) in the architecture-phase, without restricting it to much.

Similarly, there is *VHDL-code* available, to help FPGA development; however they are often restricted for a limited number of FPGA’s. With a classical top-down
approach it almost impossible to use to *details*, later the process -- at least not when strictly applied.

Ambition & Goal
===============

It is my ambitions to train (mainly software & system) engineers. Therefore, I started this :term:`MASAB` `blog
<http://mess.softwarebetermaken.nl/en/staging/blog/MASAB/index.html>`_


.. rubric:: All blogs about :term:`MASAB`:

.. postlist::
   :category: MASAB
   :date: %Y/%m
   :sort:
   :format: {title} ({date})
   :excerpts:


.. rubric:: All blogs about :term:`Natrix`:

.. postlist::
   :tags: Natrix
   :date: %Y/%m
   :sort:
   :format: {title} ({date})
   :excerpts:

----

.. rubric:: Footnotes

.. [#architect-verb]   As a verb as *‘architecting’* doesn’t exist, *designing* is commonly used.

