[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/CNxME27U)

# Calcularis Crusaders M4 Repo

## Requirements

`pip install -r requirements.txt`

Install pygraphviz from https://pygraphviz.github.io/documentation/stable/install.html

## Repo structure

### Main pipeline

- milestone-4-calcularis-crusaders/project/milestone-04/m4_calcularis_calcularis_crusaders.ipynb
    - Integrated pipeline (preprocessing, baseline model, lgbm model, explainability, evaluation)

- milestone-4-calcularis-crusaders/project/milestone-04/utils.py
    - helper functions for preprocessing
    
- milestone-4-calcularis-crusaders/project/milestone-04/utils_lgbm.py
    - helper functions for lgbm models

- milestone-4-calcularis-crusaders/project/milestone-04/report.pdf
    - project report
    

### Other experiments

- milestone-4-calcularis-crusaders/project/milestone-04/Experiments-LGBM.ipynb
    - LGBM initial experimentation. Includes knowledge tracing predictions for correctness
    - Initial SHAP experimentation
- milestone-4-calcularis-crusaders/project/milestone-04/Experiments-full-dataset.ipynb
    - Using Dask to read the full dataset and perform pre-processing
    - The noto notebook and server time out or run out of memory
    - needs more work
- milestone-4-calcularis-crusaders/project/milestone-04/Experiments-Transformer.ipynb
    - Transformer initial experimentation
    - Reached AUC of 0.776
    - Preliminary visualization of attention maps for explainability, needs more work

