# instructions
Using the [MuCGEC] (https://github.com/HillZhang1999/MuCGEC) evaluation method, The method is reference to the English major of GEC assessment tools [ERRANT] (https://github.com/chrisjbryant/errant), set up Chinese GEC assessment tools ChERRANT (Chinese ERRANT). The main function of ChERRANT is to evaluate the performance of the syntactic error correction model by comparing prediction editing with standard editing and calculating the accuracy, recall, and F-number indicators of the prediction results.

## Environment configuration
`requirements.txt`contains the main environment required for the experiment, and the specific environment construction process is shown as follows：
```
conda create -n cherrant python==3.8
conda activate cherrant
pip install -r requirements.txt
```

# Instructions for use
1. Execute 'python infer2evaldata.py' to extract the predicted answer from the LLMs generated response through infer2evaldata.py and convert the format.
2. Execute 'python parallel_to_m2.py -f answer.txt -o answer.m2' to convert standard answer parallel files through parallel_to_m2.py into an editing file in M2 format gold.m2 (only needed for first evaluation, can be reused later)
3. Run 'python parallel_to_m2.py -f predict.txt -o predict.m2' to convert parallel files of the prediction answers through parallel_to_m2.py into an edit file in M2 format hyp.m2
4. Execute 'python compare_m2_for_evaluation.py -hyp predict.m2-ref answer.m2' and compare hyp.m2 with gold.m2 using compare_m2_for_evaluation.py. Get the final evaluation index.

The word-level F0.5 indicator is the official metric used in the MuCGEC dataset, and the evaluation results are shown below：
```
=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
8       19      35      0.2963  0.186   0.2649
==============================================
```

# reference
If you have used our data set PALTEC and the evaluation program, please cite our paper[CCoT](https://github.com/liuliAI/CCoT)and paper[MuCGEC](https://github.com/HillZhang1999/MuCGEC)