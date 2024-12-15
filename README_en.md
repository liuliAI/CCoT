# CCoT: Advancing Long-Text Error Correction in Post-ASR Transcripts via Fine-Grained Contextual Chain-of-Thought

[中文说明](README.md) | [English README](README_en.md)

---

## introduction
This repository contains the code and data for the CCoT project, which aims to advance long-text error correction in post-Automatic Speech Recognition (ASR) transcripts using fine-grained contextual Chain-of-Thought.

### PALTEC Dataset
Our data mainly comes from [LCSTS](https://aclanthology.org/D15-1229/). The overall statistics of the data are shown in the table below.
| Dataset       | Train Size | Test Size | Source | Err.ratio | Avg err | Avg len | Refs | CoT len |
| ------------ | ------------ | ------------ | ---- | ------------------- | ---------------- | ------------ | ------------ | -------------- |
| SIGHAN 2014  | 3437         | 1062         | CSL  | 86.19%              | 1.52             | 50           | 1            | —              |
| SIGHAN 2015  | 2339         | 1100         | CSL  | 81.82%              | 1.33             | 30.6         | 1            | —              |
| NLPCC2018    | —            | 2000         | NCS  | 99.2%               | —                | 29.7         | 1.1          | —              |
| MuCGEC       | —            | 7063         | CSL  | 92.7%               | 3.2              | 38.5         | 2.3          | —              |
| CSCD-NS      | 30000        | 5000         | NCS  | 46.02%              | 1.09             | —            | 1            | —              |
| FCGEC        | 36340        | 5000         | NCS  | 54.45%              | —                | 53.1         | 1.7          | —              |
| **PALTEC**       | **80000**        | **20000**        | **NCS**  | **85%**                 | **2.44**           | **102.1**        | **1.6**          | **259.8**          |


Compared with previous text error correction datasets, PALTEC has a larger scale, which helps to train more accurate and generalizing models. PALTEC has an appropriate error rate, which is more in line with the actual scene; PALTEC has richer answers and is better for evaluation.

For more details on the PALTEC dataset, please refer to our paper.

- **PALTEC**: Currently, we have only opened some examples of the entire test and training sets containing 20000 samples. Dataset samples can be queried in the [data](https://github.com/liuliAI/CCoT/tree/main/data).
- **Training** data and code: The entire training set and code will be made public after our paper is accepted.
- **MP3**: All MP3 audio files can be found [here](https://pan.baidu.com/s/16VJNLRMrAfk05htePZDQQQ?pwd=xmiz) to get (10.6GB)

**Notice**: The trainset and code will be released upon the acceptance of our paper. Stay tuned for updates!
---
Currently open source [PALTEC test](https://github.com/liuliAI/CCoT/tree/main/data), all audio MP3 files of [PALTEC](https://pan.baidu.com/s/16VJNLRMrAfk05htePZDQQQ?pwd=xmiz) and [eval code](https://github.com/liuliAI/CCoT/tree/main/eval). The training set and all code will be released after our paper is accepted. Please continue to follow updates!

