==============================
The database is an antipattern
==============================

.. 2018/7/31
.. post::
   :tags: MESS, AntiPattern Pattern
   :category: Architecture
   :location: OnTheRoad
   :language: nl

Vaak *sluipt* er al heel snel een **database** in het architectuur-schets; zoals onlangs ook bij
ons. Waarom eigenlijk? En, is dat erg?

.. uml:: schets-1.puml
   :scale: 100%
   :align: right
   :caption: Versie 1 van een architectuur-schets, met database

Zonder te veel details te onthullen moet ook ons systeem sensor-data inlezen. En deze zowel
aggregeren tot (historische) data, en middels een regellus de actuators real-time aansturen.

