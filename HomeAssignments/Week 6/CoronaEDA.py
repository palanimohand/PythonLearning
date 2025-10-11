import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as cbrn
import matplotlib.pyplot as plt
import numpy as np


class covidEDA:

    df = pd.read_csv(r'HomeAssignments\Week 4 AND 5\Dataset\country_wise_latest.csv',header=0,index_col=0)
    print("Full dataset:")
    print(df)

    new_df = df[["Confirmed","New cases"]]
    print(new_df)

    #Statistical Measures

    print(new_df.mean())
    print(new_df.median())
    print(new_df.var())
    print(new_df.std())
    print(new_df.corr())

    # Outlier Detection using IQR Technique

    q1 = new_df.quantile(0.25)
    print(q1)
    q3 = new_df.quantile(0.75)
    print(q3)

    iqr = q3 - q1

    print(iqr)

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    print(lower_bound,upper_bound)

    outliers = new_df[(new_df<lower_bound)|(new_df>upper_bound)]
    outliers = outliers.dropna(axis=0)
    print(outliers)
    print(outliers.shape)
    outliers.to_csv("HomeAssignments\Week 6\Outliers.csv")

    cleaned_data = new_df[(new_df>=lower_bound)&(new_df<=upper_bound)]
    cleaned_data = cleaned_data.dropna(axis=0)
    print(cleaned_data)
    cleaned_data.to_csv("HomeAssignments\Week 6\CleanedData.csv")

    # cleaned data != fulldata - outliers
    # delta = fulldata - cleaned data + outliers = 15
    print(new_df.index)
    new_df = new_df.drop(index=cleaned_data.index, axis=0)
    print(new_df)
    print(new_df.shape)
    new_df = new_df.drop(index=outliers.index, axis=0)
    print(new_df)
    print(new_df.shape)

    sd = StandardScaler()
    scaled_data = pd.DataFrame(sd.fit_transform(cleaned_data),columns=["Confirmed","New cases"])
    print(scaled_data)

    scaled_data.to_csv("HomeAssignments\Week 6\ScaledData.csv", index=False)

    fig, axes = plt.subplots(2,2, figsize=(16,8))

    cbrn.histplot(new_df["Confirmed"], ax=axes[0,0]).set_title("Before")
    cbrn.histplot(scaled_data["Confirmed"], ax=axes[0,1]).set_title("After")
    cbrn.histplot(new_df["New cases"], ax=axes[1,0]).set_title("Before")
    cbrn.histplot(scaled_data["New cases"], ax=axes[1,1]).set_title("After")

    fig.tight_layout()

    plt.figure()
    print(scaled_data.corr())
    plt.imshow(scaled_data.corr(), cmap="coolwarm")
    # cbrn.heatmap(scaled_data, annot=True, fmt='0.0f', cmap="viridis" ,cbar=True)

    plt.show()

    