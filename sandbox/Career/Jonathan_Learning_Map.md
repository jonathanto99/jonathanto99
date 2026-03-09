# 🗺️ Jonathan's Personal Learning Map

### Oncolytic Virus R&D Leadership — Self-Study Guide (2026–2036)

*Companion to Career Roadmap \| Last Updated: March 2026*

------------------------------------------------------------------------

## How to Use This Map

-   **Priority 1 (🔴)** = Must master before next phase. Non-negotiable.
-   **Priority 2 (🟠)** = Important. Engage deeply but can run concurrently.
-   **Priority 3 (🟡)** = Enrichment. Add when bandwidth allows.
-   **✅ Habit** = Ongoing forever. Not a phase — a career discipline.
-   Each subject lists the **best single starting resource** + depth goal.

![Learning Map](learning_map_timeline.png)

------------------------------------------------------------------------

## PHASE 0 — Finishing Strong at BYU (Now → Apr 2026)

*Goal: Graduate with 3.4+ GPA, hands-on lab skills, and a reading habit.*

### 🔴 Priority 1

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **BYU Virology (MMBIO 465)** | Earn an A. Foundation for everything downstream. | Your course + Flint *Principles of Virology* (supplement) |
| **BYU Bioinformatics (BIO 165)** | Learn the vocabulary: BLAST, sequence alignment, databases. | Your course + NCBI tutorials |
| **qPCR & Flow Cytometry** | Achieve hands-on proficiency before graduation. | Lab (CHEM 497R / MMBIO 494R) |
| **Literature Habit — Start Now** | Read 1 primary OV paper/week. Summarize in ≤200 words. | *Nature Cancer*, *Molecular Therapy — Oncolytics* |

### 🟠 Priority 2

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **Linux/Bash Basics** | Navigate terminal, run scripts, manage files. | The Odin Project (free) or Software Carpentry Shell lesson |
| **Git & GitHub** | Set up a profile. Commit your BIO 165 work. | Pro Git book (free, progit.org) |

------------------------------------------------------------------------

## PHASE 1 — Lab Work + Prerequisites (Apr 2026 → Dec 2027)

*Goal: Retake Orgo, complete Biochem, build computational foundation, deepen virology knowledge.*

### 🔴 Priority 1 — Chemistry Prerequisites (UCSD Extension)

| Course | When | Goal |
|------------------------|------------------------|------------------------|
| **Organic Chemistry I (Retake)** | Summer 2026 | Replace D with B+ or higher. Solidify mechanisms. |
| **Biochemistry** | Fall 2026 | A-range. Focus: signal transduction, gene regulation, cell death pathways. |
| **Organic Chemistry II** | Spring 2027 | Complete if required by MD Anderson GSBS / Mayo. |

### 🔴 Priority 1 — Programming Foundation

| Subject | Goal | Resource | Est. Time |
|------------------|------------------|------------------|------------------|
| **R Basics** | Read/write data frames, ggplot2 visualization, basic stats. | R for Data Science (r4ds.hadley.nz, free) | 40 hrs |
| **Computational Genomics with R** | PCA, clustering, differential expression concepts. | compgenomr.github.io (free textbook) | 60 hrs |
| **Statistics Core** | FDR, linear models, GLMs, survival analysis basics. | StatQuest with Josh Starmer (YouTube, free) | 30 hrs |
| **Linux/Bash Intermediate** | Loops, piping, running bioinformatics tools from CLI. | NCI Bioinformatics for Beginners 2025 (free) | 20 hrs |

### 🟠 Priority 2 — Python & Data Science

| Subject | Goal | Resource | Est. Time |
|------------------|------------------|------------------|------------------|
| **Python Basics** | Variables, loops, functions, pandas, NumPy. | Python for Everybody (Coursera, free audit) | 30 hrs |
| **Python for Genomic Data Science** | Parse FASTA/FASTQ, work with biological data. | JHU Coursera Specialization (free audit) | 40 hrs |
| **Linear Algebra (Conceptual)** | Understand matrices, PCA, eigenvectors visually. | 3Blue1Brown Essence of Linear Algebra (YouTube) | 4 hrs |

### 🔴 Priority 1 — Biology Deepening

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **Molecular Virology** | Understand replication cycles, immune evasion, interferon antagonism. | *Fundamentals of Molecular Virology* 3rd Ed. (Acheson/Flint) — OV chapter is new in this edition |
| **Cancer Cell Biology** | Hallmarks of cancer, oncogenic signaling (RAS, p53, Rb), tumor metabolism. | *The Biology of Cancer* (Weinberg) — Chapters 4, 5, 9, 11 |
| **Tumor Immunology** | TME cellular composition, checkpoint biology, T cell exhaustion, innate sensing. | *Janeway's Immunobiology* — Chapters 12–15 (cancer-focused); *Oncoimmunology* (Zitvogel & Kroemer) |

### 🟠 Priority 2 — Scientific Communication (Start Early)

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **Paper Summarizing** | Write structured summaries (Background/Methods/Results/Significance) for every paper you read. | Self-practice — build a Zotero library |
| **Zotero Setup** | Organize 100+ papers before your MS starts. Tag by: OV platform, TME, bioinformatics method. | zotero.org (free) |
| **Science Twitter/X** | Follow 20 active OV researchers. Engage with preprints. | @NatCancer, @MolTherapy, key PIs at MD Anderson/CoH |

### 🟡 Priority 3 — Enrichment

| Subject | Resource |
|------------------------------------|------------------------------------|
| **Statistics Done Wrong** (critical thinking about data) | statisticsdonewrong.com (free, \~3 hrs) |
| **Pharmacology basics** | Khan Academy Pharmacology (free) |

------------------------------------------------------------------------

## PHASE 2 — MS Translational Bioinformatics + Industry (Jan 2028 → Dec 2029)

*Goal: MS degree, capstone publication, 4 years lab experience, PhD-ready computational skills.*

### 🔴 Priority 1 — MS Coursework (UofU DBMI)

| Course | Key Skills to Extract |
|------------------------------------|------------------------------------|
| BMI 6018 — Intro Programming for Biomedical Data Science | Python pipelines for clinical data |
| BMI 6015 — Applied Machine Learning in Biomedical Informatics | Scikit-learn, model evaluation, feature selection |
| BMI 6060 — Computational Genomics | RNAseq pipelines end-to-end: HISAT2 → StringTie → DESeq2 |
| HGEN 6421 — Genetics of Complex Disease | GWAS, statistical genetics, variant interpretation |
| BMI 6203 — Clinical Database Design | SQL for clinical data, EHR schemas, OMOP CDM |

### 🔴 Priority 1 — Bioinformatics Tools (Self-study alongside MS)

| Tool | Purpose | Resource |
|------------------------|------------------------|------------------------|
| **DESeq2 / edgeR** | Differential expression in bulk RNAseq | DIYtranscriptomics.com (free full course) |
| **Seurat** | Single-cell RNAseq analysis (clustering, UMAP, trajectory) | satijalab.org/seurat tutorials (free) |
| **Bioconductor ecosystem** | Gene ontology, pathway enrichment (fgsea, clusterProfiler) | Bioconductor workflows (bioconductor.org) |
| **Snakemake / Nextflow** | Reproducible pipeline management | Snakemake tutorial (snakemake.readthedocs.io) |
| **TCGA / GEO / cBioPortal** | Mining public clinical + genomic datasets for capstone | cbioportal.org tutorials |

### 🟠 Priority 2 — Advanced Python & ML

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **Pandas / Seaborn / Matplotlib** | Clinical data wrangling and visualization | Python Data Science Handbook (free, jakevdp.github.io) |
| **Scikit-learn ML** | Classification, cross-validation, feature importance | Scikit-learn user guide (free) |
| **SQL Intermediate** | Query EHR and clinical trial databases. | Mode SQL Tutorial (free) or SQLZoo |

### 🟠 Priority 2 — Capstone Execution

| Milestone | Target |
|------------------------------------|------------------------------------|
| Partner with Huntsman Cancer Institute researcher | By end of MS Year 1 |
| Capstone topic: "Computational Analysis of Tumor-Immune Dynamics in OV-Treated Cancers" | Utilize TCGA, GEO public datasets |
| Submit manuscript to *Molecular Therapy — Oncolytics* or *Bioinformatics* | By graduation (Dec 2029) |

### 🟠 Priority 2 — Grant Writing Literacy

| Subject | Goal | Resource |
|------------------------|------------------------|------------------------|
| **Read NIH R01 Specific Aims** | Read 10 Specific Aims pages from OV PIs at MD Anderson, CoH, Moffitt. | NIH RePORTER (reporter.nih.gov, free) |
| **Write a Mock Specific Aims** | Draft one 1-page Specific Aims for your capstone project in grant format. | Bourne & Chalupa *Ten Simple Rules for Getting Grants* (PLOS) |

### 🟡 Priority 3 — Enrichment

| Subject | Resource |
|------------------------------------|------------------------------------|
| **Spatial Transcriptomics** | 10x Genomics Visium tutorials; Hudson Lab (BCM) publications |
| **Rust (optional programming)** | Only if career pivots toward high-performance bioinformatics tools |
| **Physiology & Histopathology** | Wheater's Functional Histology (for interpreting tumor histology in translational papers) |

------------------------------------------------------------------------

## PHASE 3 — PhD Applications (Jun 2029 → Apr 2030)

*Goal: Compelling application narrative, 3 strong letters, 6–8 program applications.*

### 🔴 Priority 1 — Application Craft

| Task | Detail |
|------------------------------------|------------------------------------|
| **Personal Statement** | Lead with OV + bioinformatics dual identity. Name specific labs and why. 1–2 pages. |
| **Letters of Rec** | Utah MS advisor (computational), BYU research mentor, Industry supervisor — cultivate all three throughout Phases 1–2 |
| **Cold Email Target PIs** | Email 8–10 PIs at target programs 6 months before deadline. Attach a 1-page research interest summary. |
| **NIH F31 Awareness** | Study 2–3 funded F31 applications to understand how to frame predoctoral research aims. Prep for Year 2 of PhD. |

------------------------------------------------------------------------

## PHASE 4 — PhD Training (Aug 2030 → \~2036)

*Goal: Become the world's foremost expert at the intersection of OV biology and tumor transcriptomics.*

### 🔴 Priority 1 — Thesis & Research Skills

| Subject | Goal |
|------------------------------------|------------------------------------|
| **Advanced Virology** | Deep expertise in your chosen OV platform (HSV, oncolytic adenovirus, or poxvirus) — mechanisms, engineering, immune activation |
| **Single-Cell Multi-omics** | scRNAseq + ATAC-seq, proteomics integration (CITE-seq); apply to your tumor-virus interaction data |
| **NIH F31 Predoctoral Fellowship** | Apply in Year 2. Builds grant writing skills + prestigious on your CV |
| **Conference Presentations** | AACR Annual Meeting, SITC, American Society of Virology — present annually from Year 2 onward |
| **First-Author Publications** | Target 3–5 by graduation. At least one computational + one experimental. |

### 🟠 Priority 2 — Career Infrastructure

| Subject | Goal |
|------------------------------------|------------------------------------|
| **Peer Review** | Volunteer to review for *Molecular Therapy* or *Journal of Virology* from Year 3 onward |
| **Mentoring** | Co-mentor a rotation student or undergrad from Year 3 — builds leadership record |
| **Adjunct Teaching Prep** | TA a virology or cancer biology course during PhD to build teaching portfolio |

------------------------------------------------------------------------

## ✅ Evergreen Habits — Maintain for Life

These are not phases — they are career disciplines to build starting NOW and never stop.

| Habit | Cadence | Tool/Method |
|------------------------|------------------------|------------------------|
| **Read Primary Literature** | 2–3 papers/week minimum | Zotero + structured summaries |
| **Journals to Follow** | *Nature Cancer*, *Cell Host & Microbe*, *Molecular Therapy — Oncolytics*, *Journal of Immunotherapy for Cancer*, *Cancer Cell* | RSS feed or journal alerts |
| **Write Something Weekly** | Paper summary, blog post, mock aims paragraph, or lab notebook entry | Foam + Obsidian |
| **GitHub Commits** | At least 1 meaningful commit/week during computational phases | github.com |
| **Network Actively** | Email 1 researcher/month whose work excites you | Keep a "network spreadsheet" |
| **Track the OV Field** | Follow 3–5 clinical trials (ClinicalTrials.gov) actively enrolling OV studies | ClinicalTrials.gov saved searches |
| **Reflect Quarterly** | Review this learning map every 3 months. Check off completed items. Adjust priorities. | Add to Roadmap QMD file |

------------------------------------------------------------------------

## 📚 Master Resource List

### Free Online Courses

-   DIY Transcriptomics (diytranscriptomics.com) — RNAseq start to finish
-   Griffith Lab RNA-seq (rnabio.org) — clinical-grade RNAseq
-   Computational Genomics with R (compgenomr.github.io)
-   NCI Bioinformatics for Beginners 2025 (bioinformatics.ccr.cancer.gov)
-   StatQuest with Josh Starmer (YouTube) — statistics + bioinformatics
-   3Blue1Brown Essence of Linear Algebra (YouTube)
-   Python for Everybody (Coursera, free audit)
-   JHU Genomic Data Science Specialization (Coursera, free audit)

### Textbooks

-   *Fundamentals of Molecular Virology* 3rd Ed. — Acheson/Flint (2024) — has new OV chapter
-   *The Biology of Cancer* — Weinberg (standard PhD cancer biology text)
-   *Janeway's Immunobiology* — current edition (cancer immunity chapters)
-   *Oncoimmunology* — Zitvogel & Kroemer (OV-adjacent tumor immunology)
-   *R for Data Science* — Wickham (free online)
-   *A First Course in Systems Biology* — Voit (good reference for systems biology)
-   *Bioinformatics and Functional Genomics* — Penvsner (computational genomics)
-   *Introduction to Bioinformatics with R A Practical Guide for Biologists* — (Curry)
-   *Lehninger Principles of Biochemistry* — Nelson (gold standard biochemistry reference)
-   *Molecular Biology of the Cell Seventh Edition* — Alberts (great cell biology reference)
-   *The Communicating Scientist A Practical Handbook* — Bergman (guide to scientific communication)
-   *Genetics and Genomics in Medicine* — Cohn (resource for clinical genetics & genomics)

### Key Databases to Master

-   TCGA (The Cancer Genome Atlas) — tcga-data.nci.nih.gov
-   GEO (Gene Expression Omnibus) — ncbi.nlm.nih.gov/geo
-   cBioPortal — cbioportal.org (clinical + genomic integration)
-   NIH RePORTER — reporter.nih.gov (grant reading, PI networking)
-   ClinicalTrials.gov — OV trial tracking

### Key Journals to Read

-   *Nature Cancer* — broad cancer biology + immunotherapy
-   *Cell Host & Microbe* — virus-host interactions
-   *Molecular Therapy — Oncolytics* — dedicated OV journal
-   *Journal of Immunotherapy for Cancer* — translational immunotherapy
-   *Bioinformatics* / *Genome Biology* — computational methods

------------------------------------------------------------------------

*"Sustainability \> Speed. A 3.7 GPA is better than burnout." — Your Roadmap, Phase 1 Guidelines*