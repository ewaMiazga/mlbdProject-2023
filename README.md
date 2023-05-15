[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/CNxME27U)

# Calcularis Crusaders

## Project contributors
 - [Olivia Perryman](https://github.com/oliviaperryman)
 - [Ewa Miazga](https://github.com/ewaMiazga)
 - [Blanche Duron](https://github.com/BDURON99)

## Project goal
Creating prediction that will inform teacher about students seeking thier help. Early reaction should make student more chances to mastery skills.

## Requirements
```
pip install -r requirements.txt
```
You can install pygraphviz using this link: 
[pygraphviz](https://gitlab-stud.elka.pw.edu.pl/emiazga/seasupport/-/blob/main/doc/index.html)

## Repo structure

### Main pipeline

```
milestone-4-calcularis-crusaders
    └ project
        └ milestone-04
            ├ m4_calcularis_calcularis_crusaders.ipynb
                - Integrated pipeline (preprocessing, baseline model, lgbm model, explainability, evaluation)
            ├  utils.py
                - helper functions for preprocessing
            ├  utils_lgbm.py
                - helper functions for lgbm models
            └ report.pdf
                - project report
```    

### Other experiments

```
milestone-4-calcularis-crusaders
    └ project
        └ milestone-04
            ├  Experiments-LGBM.ipynb
                - LGBM initial experimentation. Includes knowledge tracing predictions for correctness
                - Initial SHAP experimentation
            ├  Experiments-full-dataset.ipynb
                - Using Dask to read the full dataset and perform pre-processing
                - The noto notebook and server time out or run out of memory
                - needs more work
            └ Experiments-Transformer.ipynb
                - Transformer initial experimentation
                - Reached AUC of 0.776
                - Preliminary visualization of attention maps for explainability, needs more work
```

