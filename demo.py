import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(5);n=500
tot=rng.poisson(60,n)+10
ref=rng.binomial(tot,0.5)  # balanced
ase=rng.choice(n,40,replace=False);ref[ase]=rng.binomial(tot[ase],rng.uniform(0.75,0.95,40))
frac=ref/tot;imbal=(np.abs(frac-0.5)>0.2)
plt.figure(figsize=(6,5))
plt.scatter(tot[~imbal],frac[~imbal],s=8,c="grey",alpha=.5)
plt.scatter(tot[imbal],frac[imbal],s=14,c="firebrick",label="allelic imbalance")
plt.axhline(0.5,ls="--",c="k");plt.xlabel("total reads");plt.ylabel("reference allele fraction")
plt.title("Allele-specific expression (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"imbalanced genes: {int(imbal.sum())}\n");print("ok")