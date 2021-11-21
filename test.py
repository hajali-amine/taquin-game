from copy import deepcopy

from taquin import Taquin

taq = Taquin()
taqq = deepcopy(taq)
sett = set()
sett.add(taq)

print(taqq in sett)