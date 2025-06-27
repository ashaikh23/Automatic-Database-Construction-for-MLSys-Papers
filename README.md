# Automatic Database Construction for MLSys Papers

This repository contains our accepted research from [**MLSys 2025**](https://mlsys.org/Conferences/2025), presented at the Santa Clara, CA. Our project introduces a machine learning-powered pipeline for automatically curating and analyzing a domain-specific database of academic papers in Machine Learning Systems (MLSys).

## 📄 Project Summary

Our work addresses the need for scalable, automated analysis of the rapidly growing MLSys literature. We:

- Automatically ingest and classify academic papers relevant to MLSys 
- Use document embeddings (SPECTER2, Sent2Vec) and ML techniques (K-Means clustering, KNN classification)
- Perform citation graph analysis to uncover emerging topics, influential authors, and research trends

For a detailed overview, see our [poster](docs/MLSys_Poster_Automatic_Database_Construction_for_MLsys.pdf), [abstract](docs/MLSys%202025%20Accepted%20Abstract%20Automatic%20Database%20Construction%20for%20MLSys%20Papers.pdf), and [presentation slides](docs/presentation_slides.pdf).

---

## 📁 Repository Structure

```
MLSys-2025-Database-Research/
│
├── README.md
├── LICENSE
│
├── docs/
│   ├── abstract_mlsys2025.pdf
│   ├── presentation_slides.pdf
│   ├── poster_mlsys2025.pdf
│   ├── project_log.pdf
│
├── data/
│   ├── MLPapersFinal.csv
│   └── embeddings/                   # Sent2Vec and SPECTER2 vectors
│
├── code/
│   ├── data_ingestion.py
│   ├── embedding_generation.py
│   ├── clustering.py
│   ├── classification.py
│   └── utils.py
│
├── results/
│   ├── figures/
│   └── performance_metrics.txt
│
└── notebooks/
    └── analysis.ipynb
```

---

## 🧠 Key Results

- **KMeans clustering (unsupervised)** with SPECTER2 embeddings achieved a ROC-AUC of **~0.88**
- **KNN classification (supervised)** performed with high precision on balanced datasets
- **Cosine similarity** outperformed Euclidean distance in classification tasks
- **Emerging topics** include distributed training, hardware acceleration, and model optimization

---

## 🔍 Insights & Trends

We explored:
- The **evolution of research themes** in MLSys (2018–2024)
- The **most cited papers** and **top contributing institutions**
- **Emerging trends** using time-series analysis on cluster centroids

---

## 🧾 Development Log

For detailed progress and technical decisions, see [`docs/project_log.pdf`](docs/project_log.pdf). It includes weekly meeting notes, design milestones, and implementation details.

---

## 📈 Future Work

- Automate the full ingestion and classification pipeline
- Scale the dataset from 500 to 5000+ papers
- Explore **graph-based learning** on citation networks
- Extend our methodology to interdisciplinary domains
- Improve model interpretability and classifier robustness

---

## 💻 Installation

Clone the repo and install required dependencies (Python 3.8+ recommended):

```bash
git clone https://github.com/ashaikh23/Automatic-Database-Construction-for-MLSys-Papers.git
cd Automatic-Database-Construction-for-MLSys-Papers
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the pipeline step-by-step or execute modules individually:

```bash
python code/data_ingestion.py
python code/embedding_generation.py
python code/clustering.py
python code/classification.py
```

Jupyter notebooks for analysis are available in the `notebooks/` directory.

---

## 🧪 Evaluation

- All classification results are stored in `results/performance_metrics.txt`
- Visualizations are saved under `results/figures/`

We report results using standard metrics (ROC-AUC, precision, recall) and include ablation studies comparing embedding methods and distance metrics.

---

## 📚 Citing This Work

If you use this project or build on our pipeline, please consider citing our MLSys 2025 abstract:

```
@misc{shaikh2025mlsysdb,
  title={Automatic Database Construction for MLSys Papers},
  author={Aymaan Shaikh and Takuto Ban},
  year={2025},
  howpublished={Accepted to MLSys 2025, Santa Clara Convention Center}
}
```

---

## 👥 Authors (University of Massachusetts Amherst)

- [Aymaan Shaikh](https://ashaikh23.github.io/)
- Takuto Ban

**Advisors:**
- Prof. [Hui Guan](https://guanh01.github.io/)
- [Lijun Zhang, PhD](https://zhanglijun95.github.io/)

---

## 📜 License

This project is licensed under the MIT License.
