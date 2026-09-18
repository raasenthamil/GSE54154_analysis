
# Day 2: GSE107557 EV vs Dnm3os
import pandas as pd, glob, re, numpy as np
from scipy.stats import ttest_ind
from functools import reduce

# Merge RAW
all_dfs = []
for f in glob.glob('GSM*.txt.gz'):
    df = pd.read_csv(f, sep='	')
    gsm_id = re.search(r'GSM\d+', f).group(0)
    df = df[['transcript-id','normalized-counts']]
    df.columns = ['probe', gsm_id]
    all_dfs.append(df)

merged = reduce(lambda l,r: pd.merge(l,r,on='probe'), all_dfs).set_index('probe')

EV = ['GSM2871196','GSM2871197']
DNM = ['GSM2871198','GSM2871199']

df_log = np.log2(merged + 1)
results = []
for gene in merged.index:
    ev = df_log.loc[gene, EV].values
    dn = df_log.loc[gene, DNM].values
    log2fc = np.mean(dn) - np.mean(ev)
    _, p = ttest_ind(dn, ev)
    results.append([gene, log2fc, p])

deg = pd.DataFrame(results, columns=['probe','log2FC','pval'])
deg.to_csv('Day2_FINAL_DEG.csv', index=False)
print(f"UP: {len(deg[deg['log2FC']>1])}, DOWN: {len(deg[deg['log2FC']<-1])}")
