# Awesome-RAG-Datasets

A curated list of benchmark datasets for Retrieval-Augmented Generation (RAG) research and engineering. Covering TextRAG, GraphRAG, MultimodalRAG, and TableRAG, this repository aims to provide a comprehensive, structured, and up-to-date resource for researchers and developers to evaluate and optimize RAG systems.

🏆 **Core Value**: One-stop access to high-quality RAG benchmarks, with standardized metadata, usage guides, and evaluation references.

## Table of Contents

- [Introduction](#introduction)
- [Dataset Classification](#dataset-classification)
    - [1. TextRAG](#textrag)
    - [2. GraphRAG](#graphrag)
    - [3. MultimodalRAG](#multimodalrag)
    - [4. TableRAG](#tablerag)
- [Evaluation Metrics](#evaluation-metrics)

## Introduction

### What is RAG?

Retrieval-Augmented Generation (RAG) is a paradigm that combines information retrieval with large language models (LLMs) to enhance the factuality, accuracy, and timeliness of generated content. RAG systems retrieve relevant external knowledge from a corpus and feed it to the LLM as context, addressing limitations such as knowledge obsolescence and hallucinations in standalone LLMs.

### Purpose of This Repository

This repository collects and organizes benchmark datasets for RAG systems, with the following goals:

- Provide a **structured classification** of RAG datasets to cover diverse tasks, domains, and scenarios.
- Supplement **standardized metadata** for each dataset (e.g., task type, sample size, evaluation metrics) to facilitate quick comparison and selection.
- Offer **practical usage guides** and code examples to lower the barrier for researchers and developers to use the datasets.
- Maintain an **up-to-date resource** to track the latest advances in RAG benchmarking.

## Dataset Classification

Datasets are categorized into four core types based on the data format and RAG scenario. Each category includes sub-tasks and domain-specific datasets, with standardized metadata tables for easy reference.

### 1. TextRAG

**Description**: Benchmark datasets for text-only Retrieval-Augmented Generation, covering single-hop/multi-hop QA, fact verification, long-text understanding, and domain-specific tasks. Suitable for evaluating the basic retrieval and generation capabilities of RAG systems on text corpora.

#### 1.1 General Domain TextRAG

|Dataset Name|Task Type|Sample Size|Context Characteristics|Evaluation Metrics|Official Link|Paper Reference|
|-|-|-|-|-|-|-|
||||||||


#### 1.2 Domain-Specific TextRAG

|Dataset Name|Task Type|Domain|Sample Size|Knowledge Source|Evaluation Metrics|Official Link|Paper Reference|
|-|-|-|-|-|-|-|-|
|||||||||


### 2. GraphRAG

**Description**: Datasets for Graph Retrieval-Augmented Generation, focusing on tasks that require reasoning over knowledge graphs or structured graph data. Suitable for evaluating RAG systems' ability to retrieve and utilize graph-structured knowledge (e.g., entity relationships, event chains).

|Dataset Name|Task Type|Graph Type|Sample Size|Data Source|Evaluation Metrics|Official Link|Paper Reference|
|-|-|-|-|-|-|-|-|
|||||||||


### 3. MultimodalRAG

**Description**: Datasets for Multimodal Retrieval-Augmented Generation, involving multiple modalities such as text, images, tables, charts, and PDFs. Suitable for evaluating RAG systems' ability to retrieve and fuse multimodal information (e.g., answering questions based on scanned documents, infographics, or scientific charts).

|Dataset Name|Task Type|Modalities|Sample Size|Data Source|Evaluation Metrics|Official Link|Paper Reference|
|-|-|-|-|-|-|-|-|
|||||||||
|||||||||


### 4. TableRAG

**Description**: Datasets for Table Retrieval-Augmented Generation, focusing on tasks that require retrieving and reasoning over tabular data. Suitable for evaluating RAG systems' ability to process structured tabular information (e.g., answering questions based on Wikipedia tables, financial reports).

|Dataset Name|Task Type|Table Source|Sample Size|Table Characteristics|Evaluation Metrics|Official Link|Paper Reference|
|-|-|-|-|-|-|-|-|
|||||||||


## Evaluation Metrics

Common evaluation metrics for RAG systems are summarized below, categorized by task type:

### 1. QA Tasks (Single-hop/Multi-hop)

- **EM (Exact Match)**: Measures whether the generated answer exactly matches any of the reference answers. Suitable for short fact-based answers.
- **F1 Score**: Computes the harmonic mean of precision and recall between the generated answer and reference answers. Robust to minor wording differences.
- **Distractor Accuracy**: For multi-hop QA (e.g., HotpotQA), measures the ability to distinguish between relevant and distractor documents.

### 2. Fact Verification Tasks

- **Accuracy**: The proportion of correctly classified claims (SUPPORT/REFUTE/NOT ENOUGH INFO).
- **FEVER Score**: Combines accuracy with evidence retrieval precision/recall, requiring the system to retrieve valid evidence for verification.

### 3. Generation Tasks (Summary/Biography)

- **FactScore**: Measures the factuality of generated text by comparing it with the reference knowledge corpus.
- **MAUVE**: Evaluates the fluency and diversity of generated text by measuring the divergence between model-generated text and human-written text.
- **ROUGE-L**: Evaluates the coherence of long-text generation (e.g., summaries, biographies).

### 4. Retrieval Tasks

- **Precision@k**: The proportion of relevant documents among the top-k retrieved documents.
- **Recall@k**: The proportion of all relevant documents that are retrieved in the top-k results.
- **MRR (Mean Reciprocal Rank)**: The average of the reciprocals of the ranks of the first relevant document retrieved.


