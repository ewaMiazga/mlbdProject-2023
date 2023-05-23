# MLBD project

## Project contributors
 - [Ewa Miazga](https://github.com/ewaMiazga)
 - [Olivia Perryman](https://github.com/oliviaperryman)
 - [Blanche Duron](https://github.com/BDURON99)

## Project goal
Creating prediction that will inform teacher about students seeking thier help. Early reaction should make student more chances to mastery skills.

## Results summary poster:
[Poster](https://github.com/ewaMiazga/mlbdProject-2023/blob/main/MLBD_poster.pdf)

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
        ├ milestone-02
            └ m2_dataset.ipynb
                - Initial analysis of dataset
        └ milestone-04
            ├ Research.ipynb
                - Integrated pipeline (preprocessing, baseline model, lgbm model, explainability, evaluation)
            ├  utils.py
                - helper functions for preprocessing
            ├  utils_lgbm.py
                - helper functions for lgbm models
            └ report.pdf
                - project report
```    
#### Snippet of dataframe created in Research.ipynb:
![image](https://github.com/ewaMiazga/mlbdProject-2023/assets/126163122/1b3a139f-5f20-41b4-a6fd-894dbc38b773)

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
