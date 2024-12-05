import pandas as pd
import matplotlib.pyplot as plt

def calculate_outliers(data, whisker_factor=1.5):
  q1 = data.quantile(0.25)
  q3 = data.quantile(0.75)
  iqr = q3 - q1
  lower_boundary = q1 - whisker_factor * iqr
  upper_boundary = q3 + whisker_factor * iqr
  return lower_boundary, upper_boundary

for feat in df.columns:
  try:
    boundaries = calculate_outliers(df[feat])
    lower_border, upper_border = boundaries

    plt.figure(figsize=(5, 4))
    plt.boxplot(df[feat], vert=True, patch_artist=True, sym='.')
    plt.ylabel('Values (' + feat + ')')
    plt.xlabel(feat)
    plt.title('Boxplot for ' + feat + '\n')
    plt.show()
  except:
    print('Categorical feature')
