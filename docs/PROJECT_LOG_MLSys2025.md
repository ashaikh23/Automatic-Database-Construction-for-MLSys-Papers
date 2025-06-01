# 📓 Project Log: Automatic Database Construction for MLSys Papers

This project is a culmination of systematic planning, exploration, and iteration across multiple facets of building a domain-specific academic paper database for Machine Learning Systems (MLSys). Below is a high-level, goal-oriented summary of our process and progress.

---

## 🏗️ Building the MLSys Paper Database

- **Seed Data Collection**  
  We curated an initial database of ~575 seed papers from the MLSys Conference (2018–2024) and the Awesome Systems for Machine Learning GitHub repository. These formed the basis for what defines an MLSys paper.

- **Metadata Extraction**  
  Using the Semantic Scholar API, we extracted metadata for each paper: paper ID, title, authors, citations, references, venue, and abstract. We structured this data into CSVs to serve as input for downstream processing.

- **Database Expansion**  
  We expanded the database by identifying papers citing the seed set and applying relevance filters using clustering and classification techniques.

---

## 🧪 Machine Learning for Classification

- **Unsupervised Learning (Clustering)**  
  K-Means was applied to embeddings generated using SPECTER2 and Sent2Vec to form clusters of relevant papers. Reference papers were scored based on their distance from the cluster centroids.

- **Supervised Learning (KNN)**  
  We balanced the dataset with positive and carefully chosen negative samples—ranging from ML-only (NeurIPS), Systems-only (ASPLOS), and non-CS disciplines (Biology, Chemistry). KNN classifiers were trained to distinguish relevant papers based on abstract/title embeddings.

- **Ablation Studies**  
  We compared performance across embedding models (Sent2Vec vs. SPECTER2) and distance metrics (Cosine vs. Euclidean) to validate our approach.

---

## 📈 Analytical Goals

- Identify and analyze the most studied topics in MLSys across time and venues
- Determine the evolution of topics over the years and across major conferences
- Predict future research trends based on topic dynamics
- Pinpoint rising contributors and influential publications through citation graph analysis

---

## 🔍 Filtering & Precision Challenges

- **Negative Sampling Strategy**  
  We designed a comprehensive method for generating true and hard negatives, ensuring diversity in our negative class for classifier robustness.

- **Semantic Similarity Evaluation**  
  To automate relevance filtering, we compared seed papers and candidate references using title + abstract similarity in embedding space. Threshold tuning was critical to ensure precision.

---

## 📊 Graph-Based Vision

We envisioned our database as a knowledge graph:
- **Nodes**: paper IDs, authors, venues, and topics
- **Edges**: citations, authorship, publication, topical relevance

This graph would later support analyses like:
- Topic trajectory over time
- Collaboration networks
- Influence propagation and PageRank-style author/venue ranking

---

## 🔄 Iterative Refinement

- Created a unified Google Sheet for consistent metadata logging
- Wrote scripts for automatic ingestion and de-duplication
- Manually labeled and validated subsets to benchmark classifier accuracy
- Explored Semantic Scholar’s Recommendation API for intelligent expansion
- Investigated binary vs. multi-class classification strategies
- Tuned classification thresholds and evaluated results on manually curated 200-paper test set

---

## 🚀 Looking Ahead

- Scale database from 500 → 5,000+ papers
- Fully automate ingestion, embedding, classification, and storage pipeline
- Publish findings on citation trends, emerging subfields, and co-authorship dynamics
- Compare results with alternate methods (e.g., transfer learning, entropy-based filtering)
- Expand to other interdisciplinary ML domains

---

This project is ongoing and continues to evolve with each iteration. We are committed to releasing updates to this repository as we refine and expand our framework.
