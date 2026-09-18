# GSE54154_analysis
Re-analysis of diabetic bone marrow progenitors - 1979 UP genes

## Day 2: GSE107557 - Dnm3os lncRNA as diabetic mimic
**Date:** Sep 18, 2026

### What I did:
- Downloaded GSE107557 RAW.tar from NCBI FTP (4 samples: 2 EV, 2 Dnm3os)
- Merged 35,786 transcripts, used normalized-counts
- log2 + t-test

### Result:
- UP in Dnm3os: 357 genes
- DOWN in Dnm3os: 211 genes
- Top UP: Mmp11, Serpinb2, NR_002870 (Dnm3os itself) - all M1/inflammation markers
- Plot: Day2_volcano.png

### Key learning:
GEO SOFT files can be empty. Real data is in RAW.tar. Always check GSM titles first.

### Files:
- `HG_Macrophage_30Days.ipynb` - master notebook
- `Day2_FINAL_DEG.csv` - DEG results
- `Day2_volcano.png` - volcano plot
- `day2_GSE107557_DEG.py` - clean code

### Next: Day 3 - Pathway enrichment of 357 UP genes
