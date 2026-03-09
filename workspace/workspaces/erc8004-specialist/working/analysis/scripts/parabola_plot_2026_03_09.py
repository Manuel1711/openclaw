import numpy as np, matplotlib.pyplot as plt
x=np.linspace(-10,10,400)
y=x**2
plt.figure(figsize=(6,4)); plt.plot(x,y); plt.title('Parabola y=x^2'); plt.xlabel('x'); plt.ylabel('y'); plt.grid(True,alpha=.3); plt.tight_layout(); plt.savefig('workspaces/erc8004-specialist/outbox/figures/2026-03-09_parabola_test/parabola_plot.pdf')
