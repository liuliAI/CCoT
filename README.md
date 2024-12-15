# CCoT: Advancing Long-Text Error Correction in Post-ASR Transcripts via Fine-Grained Contextual Chain-of-Thought

[中文说明](README.md) | [English README](README_en.md)

---

## 简介

该存储库包含CCoT项目的代码和PALTEC数据集，该项目利用教师-学生学习范式通过细粒度的上下文思维链来提升ASR转录文本中的长文本错误纠正技术。

### PALTEC数据集
我们的数据主要来自[LCSTS](https://aclanthology.org/D15-1229/)，数据的整体统计如下表所示。
| 数据集       | 训练集句子数 | 测试集句子数 | 来源 | 平均错误句子数(比例) | 每句平均错误数量 | 每句平均字数 | 平均答案数量 | 平均思维链长度 |
| ------------ | ------------ | ------------ | ---- | ------------------- | ---------------- | ------------ | ------------ | -------------- |
| SIGHAN 2014  | 3437         | 1062         | CSL  | 86.19%              | 1.52             | 50           | 1            | —              |
| SIGHAN 2015  | 2339         | 1100         | CSL  | 81.82%              | 1.33             | 30.6         | 1            | —              |
| NLPCC2018    | —            | 2000         | NCS  | 99.2%               | —                | 29.7         | 1.1          | —              |
| MuCGEC       | —            | 7063         | CSL  | 92.7%               | 3.2              | 38.5         | 2.3          | —              |
| CSCD-NS      | 30000        | 5000         | NCS  | 46.02%              | 1.09             | —            | 1            | —              |
| FCGEC        | 36340        | 5000         | NCS  | 54.45%              | —                | 53.1         | 1.7          | —              |
| **PALTEC**       | **80000**        | **20000**        | **NCS**  | **85%**                 | **2.44**           | **102.1**        | **1.6**          | **259.8**          |

相较于之前的文本纠错数据集，PALTEC拥有更大的规模，有助于训练更准确、泛化能力更强的模型；PALTEC具有适当的错误率，更符合实际场景；PALTEC具有更丰富的答案，更好利于评估。

更多关于PALTEC数据集的细节，请参考我们的论文。

- **PALTEC**: 目前，我们只开放了包含2万条的全部测试集和训练集的一些示例。数据集样例可在[data](https://github.com/liuliAI/CCoT/tree/main/data)中查询。
- **Training data and Code**: 全部训练集和代码将在我们的论文被接受后公开。
- **MP3**: 全部PALTEC的MP3音频文件可在[此处](https://pan.baidu.com/s/16VJNLRMrAfk05htePZDQQQ?pwd=xmiz)获取 （10.6GB）
- **Eval**: 评估方法可在[eval](https://github.com/liuliAI/CCoT/tree/main/eval)获取

###  **通知**: 目前已经开源[PALTEC测试集](https://github.com/liuliAI/CCoT/tree/main/data)，[PALTEC的全部音频文件](https://pan.baidu.com/s/16VJNLRMrAfk05htePZDQQQ?pwd=xmiz)以及[评估代码](https://github.com/liuliAI/CCoT/tree/main/eval)，训练集和全部代码将在我们的论文被接受后发布。请继续关注更新！
---


