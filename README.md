# Automatic Database Construction for MLSys Papers

This repository contains our research from MLSys 2025 on building a machine learning-powered pipeline to automatically construct and analyze a curated database of academic papers in the Machine Learning Systems (MLSys) domain.

## 📄 Project Summary

Our work focuses on:
- Automatically ingesting and classifying academic papers relevant to MLSys.
- Using machine learning techniques (clustering, KNN) and embeddings (SPECTER2, Sent2Vec) for document classification.
- Performing citation and trend analysis to identify emerging topics and influential authors/institutions.

See our [poster](docs/poster.pdf), [abstract](docs/abstract.pdf), and [presentation slides](docs/presentation.pdf) for a detailed overview.

## 📁 Contents

- `docs/`: Research artifacts (poster, presentation, abstract, proposal)
- `code/`: Scripts used for data collection, embedding generation, clustering, and classification
- `data/`: (Optional) Sample or anonymized data used in our study
- `results/`: Evaluation metrics, visualizations, and analysis output
- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA) and insight extraction

## 🧠 Key Findings

- KMeans clustering with SPECTER2 embeddings achieved an ROC-AUC of ~0.88
- Cosine similarity outperformed Euclidean distance for nearest neighbor classification
- Trends indicate increasing focus on distributed training and hardware acceleration post-2020

## 📈 Future Work

- Automate the entire ingestion-classification pipeline
- Extend classification framework to other interdisciplinary domains
- Predict research trends using time-series modeling

## 👥 Authors

- Aymaan Shaikh ([@aishaikh@umass.edu](mailto:aishaikh@umass.edu))
- Takuto Ban ([@tban@umass.edu](mailto:tban@umass.edu))

Advised by:
- Prof. Hui Guan
- Lijun Zhang

## 📜 License

This project is licensed under the MIT License.
