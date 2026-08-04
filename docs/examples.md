\# Examples



This page shows simple usage patterns for Planetary\_Atlas.



\## Load the DiskAtlas



from atlas.disk\_atlas import DiskAtlas

atlas = DiskAtlas("atlas/atlas\_data.npz")



\## Find Planet Candidates



from tools.planet\_finder import find\_planet\_candidates

candidates = find\_planet\_candidates(atlas, max\_candidates=5)

print(candidates)



\## Build Hydro Simulation Plan



from tools.hydro\_planner import make\_hydro\_plan

plan = make\_hydro\_plan(atlas, max\_targets=10)

print(plan)



\## Full Workflow



from atlas.disk\_atlas import DiskAtlas

from tools.planet\_finder import find\_planet\_candidates

from tools.hydro\_planner import make\_hydro\_plan



atlas = DiskAtlas("atlas/atlas\_data.npz")



candidates = find\_planet\_candidates(atlas)

plan = make\_hydro\_plan(atlas)



print("Candidates:", candidates)

print("Hydro Plan:", plan)



