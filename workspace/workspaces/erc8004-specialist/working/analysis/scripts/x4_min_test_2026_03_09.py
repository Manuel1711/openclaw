import numpy as np, matplotlib.pyplot as plt
x=np.linspace(-3,3,600)
y=x**4
xmin=0.0; ymin=0.0
plt.figure(figsize=(6,4)); plt.plot(x,y,label='y=x^4'); plt.scatter([xmin],[ymin],color='red',label='minimum (0,0)'); plt.legend(); plt.grid(True,alpha=.3); plt.tight_layout(); plt.savefig('workspaces/erc8004-specialist/outbox/figures/2026-03-09_x4_test/x4_plot.pdf')
