# Homework 6

## Folder Structure

- data/raw/ -> All raw csv data is located here
- data/processed -> All processed/cleaned data is located here
- notebooks/ -> Jupyter notebook for saving and processing data is located here

## Preprocessing Assumptions

- Filling missing data with medians assumes that missing data is not MAR (Missing at Random) or MCAR (Missing Completely at Random), and thus not critical for analysis
- Dropping rows assumes dropped rows are not critical for analysis
- StandardScaler assumes features are roughly normally distributed
- MinMaxScaler assumes min and max values are repesentative and not outliers
- Using modular functions assumes future datasets will follow similar structures and patterns
