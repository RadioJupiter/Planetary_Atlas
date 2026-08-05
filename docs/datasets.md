\# Working With Datasets



Planetary\_Atlas supports external datasets that describe the physical structure

of a protoplanetary disk. This guide explains how datasets must be formatted,

how to load them, and how to run candidate detection on any new dataset.



\---



\## Dataset Format



Planetary\_Atlas expects datasets stored as `.npz` files containing the following

fields:



\- r\_vals

\- scores

\- compression

\- stability

\- v\_drift

\- planet\_forces

\- pressure

\- sigma

\- curvature

\- ring\_width

\- survival

\- gap\_mass

\- planet\_mass\_inversion

\- brightness

\- alpha

\- nu



Each field must be a NumPy array of equal length. These arrays represent the

radial structure and physical diagnostics of the disk.



\---



\## Loading a Dataset



Planetary\_Atlas includes a dataset loader module that simplifies importing new

datasets. Use it like this:



```python

from atlas.dataset import load\_dataset



da = load\_dataset("path/to/dataset.npz")



