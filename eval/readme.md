[中文说明](readme.md) | [English README](readme_en.md)

# 使用说明
使用了[MuCGEC](https://github.com/HillZhang1999/MuCGEC)的评估方法，该方法借鉴了英文上主流的GEC评估工具[ERRANT](https://github.com/chrisjbryant/errant)，搭建了中文GEC评估工具ChERRANT（Chinese ERRANT）。ChERRANT的主要功能是通过对比预测编辑和标准编辑，计算预测结果的精确度、召回度、F值指标，从而评估语法纠错模型的性能。

## 环境配置
`requirements.txt`包含了实验所需的主要环境，具体环境搭建流程如下所示：
```
conda create -n cherrant python==3.8
conda activate cherrant
pip install -r requirements.txt
```

# 使用说明
1. 执行`python infer2evaldata.py `通过infer2evaldata.py将LLMs生成的响应提取出预测答案并转换格式。
2. 执行`python parallel_to_m2.py -f answer.txt -o answer.m2`将标准答案平行文件通过parallel_to_m2.py转换成M2格式的编辑文件gold.m2（仅首次评估需要，之后可以复用）
3. 执行`python parallel_to_m2.py -f predict.txt -o predict.m2`将预测答案平行文件通过parallel_to_m2.py转换成M2格式的编辑文件hyp.m2；
4. 执行`python compare_m2_for_evaluation.py -hyp predict.m2 -ref answer.m2`使用compare_m2_for_evaluation.py对比hyp.m2和gold.m2，得到最终的评价指标。

字级别的F0.5指标是MuCGEC数据集采用的官方评测指标，评价结果如下所示：
```
=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
8       19      35      0.2963  0.186   0.2649
==============================================
```

# 引用
如果您使用了使用了我们的数据集PALTEC和该评价程序，请引用我们的论文[CCoT](https://github.com/liuliAI/CCoT)和论文[MuCGEC](https://github.com/HillZhang1999/MuCGEC)