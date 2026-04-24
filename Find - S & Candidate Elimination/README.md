\# Assignment 1: Find-S and Candidate Elimination



\## Background



This assignment demonstrates concept learning using Find-S and Candidate Elimination algorithms.



\## Case Study



A dataset is used to predict whether a person enjoys sport based on environmental conditions.



\## Code



Python implementation is provided in find\_s\_candidate.py.



\## How I Traced It



\* Initialized S as most specific

\* Initialized G as most general

\* Updated S for positive examples

\* Specialized G for negative examples



\## Situations Where Version Space Fails



1\. Noisy data

2\. Missing values

3\. Continuous attributes

4\. Irrelevant attributes

5\. Inconsistent hypothesis space



\## Output



Final Specific Hypothesis:

\['Sunny', 'Warm', '?', 'Strong', '?', '?']



Final General Hypothesis:

\[\['Sunny', '?', '?', '?', '?', '?'], \['?', 'Warm', '?', '?', '?', '?'], \['?', '?', '?', '?', '?', '?']]



\## Author



Lakshmi L K



