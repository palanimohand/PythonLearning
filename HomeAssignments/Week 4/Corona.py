import kagglehub
import shutil
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class covidCases:
    # path = kagglehub.dataset_download("imdevskp/corona-virus-report")
    # print("Path to dataset files:", path)
    # source_dir = path
    # dest_dir = r"C:\Users\Palanimohan\Desktop\AI Engineer\Python_Practice\HomeAssignments\Week 4\Dataset"
    # for filename in os.listdir(source_dir):
    #     src_file = os.path.join(source_dir, filename)
    #     dst_file = os.path.join(dest_dir, filename)
    #     if os.path.isfile(src_file):
    #         shutil.copy(src_file, dst_file)

    # 1. Summarize Case Counts by Region
    print("====================== 1. Case Counts by Region ======================")
    df = pd.read_csv(r'HomeAssignments\Week 4\Dataset\country_wise_latest.csv',header=0,index_col=0)
    print("Full dataset:")
    print(df)
    print(pd.concat([df['Confirmed'],df['Deaths'],df['Recovered']],axis=1))

    # 2. Filter Low Case Records
    print("====================== 2. Records with Confirmed Cases < 10 ======================")
    print(df[df['Confirmed']<10])

    # 3. Identify Region with Highest Confirmed Cases
    print("====================== 3. Region with Highest Confirmed Cases ======================")
    print(df['Confirmed'].idxmax(),df['Confirmed'].max())

    # 4. Sort Data by Confirmed Cases
    print("====================== 4. Sorted Data by Confirmed Cases ======================")
    print(df['Confirmed'].sort_values().to_csv("Test.CSV",index=True))

    # 5. Top 5 Countries by Case Count
    print("Top 5 countries by confirmed cases:")
    print(df['Confirmed'].sort_values(ascending=False).head())

    # 6. Region with Lowest Death Count
    print("====================== 6. Region with Lowest Death Count ======================")
    print(df['Deaths'].sort_values().idxmin(), df['Deaths'].sort_values().min())

    # 7. India’s Case Summary (as of April 29, 2020)
    print("====================== 7. India’s Case Summary (as of April 29, 2020) ======================")
    print(df.loc['India',:])

    # 8. Calculate Mortality Rate by Region
    # o Death-to-confirmed case ratio.
    print("====================== 8. Mortality Rate by Region ======================")
    print(df['Deaths']/df['Confirmed']*100)

    # 9. Compare Recovery Rates Across Regions
    print("====================== 9. Recovery Rates by Region ======================")
    print(df['Recovered']/df['Confirmed']*100)

    # 12. Identify Regions with Zero Recovered Cases
    print("====================== 12. Regions with Zero Recoveries ======================")
    print(df[df['Recovered']==0]['Recovered'])

    # 11. Group Data by Country and Region
    print("====================== 11. Data Grouped by WHO Region ======================")
    ds = pd.DataFrame(df.groupby("WHO Region",group_keys=True))
    print(ds)
    print("Details for each region:")
    for index in range(len(set(df['WHO Region'].unique()))):
        print(ds[1][index])

    # 10. Detect Outliers in Case Counts
    #  Use mean ± 2*std deviation.
    print("====================== 10. Outliers in Case Counts ======================")
    lower = df['Deaths'].mean() - (df['Deaths'].std()*2)
    upper = df['Deaths'].mean() + (df['Deaths'].std()*2)
    print(lower,upper)
    print(df[(df['Deaths']<upper) & (df['Deaths']>lower)]['Deaths'])
    lower = df['Confirmed'].mean() - (df['Confirmed'].std()*2)
    upper = df['Confirmed'].mean() + (df['Confirmed'].std()*2)
    print(lower,upper)
    print(df[(df['Confirmed']<upper) & (df['Confirmed']>lower)]['Confirmed'])
    lower = df['Recovered'].mean() - (df['Recovered'].std()*2)
    upper = df['Recovered'].mean() + (df['Recovered'].std()*2)
    print(lower,upper)
    print(df[(df['Recovered']<upper) & (df['Recovered']>lower)]['Recovered'])
    lower = df['Active'].mean() - (df['Active'].std()*2)
    upper = df['Active'].mean() + (df['Active'].std()*2)
    print(lower,upper)
    print(df[(df['Active']<upper) & (df['Active']>lower)]['Active'])
    lower = df['New cases'].mean() - (df['New cases'].std()*2)
    upper = df['New cases'].mean() + (df['New cases'].std()*2)
    print(lower,upper)
    print(df[(df['New cases']<upper) & (df['New cases']>lower)]['New cases'])


class CovidVisualization(covidCases):

    # code to set the yticker for plain style instead of scientific globally
    # from matplotlib.ticker import ScalarFormatter

    # for ax in axs.flat:
    #     ax.yaxis.set_major_formatter(ScalarFormatter())
    #     ax.ticklabel_format(style='plain', axis='y')   # ensure no offset/sci
    #     ax.yaxis.get_major_formatter().set_useOffset(False)

    # 1. Bar Chart of Top 10 Countries by Confirmed Cases
    # plt.figure(figsize=(12,6))
    # plt.bar(covidCases.df['Confirmed'].sort_values(ascending=False).head(10).index, list(covidCases.df['Confirmed'].sort_values(ascending=False).head(10)))
    # plt.xlabel("Country")
    # plt.ylabel("Confirmed Cases")
    # plt.title("Bar Chart of Top 10 Countries by Confirmed Cases")
    # plt.ticklabel_format(style="plain", axis="y")

    pandas_line_plot = pd.DataFrame(covidCases.df['Confirmed'].sort_values(ascending=False).head(10))
    ax = pandas_line_plot.plot(kind="bar",xlabel="Country", ylabel="Confirmed Cases", title="Bar Chart of Top 10 Countries by Confirmed Cases", figsize=(8,6))
    ax.ticklabel_format(style="plain", axis="y")
    ax.get_figure().savefig("HomeAssignments\Week 4\Plot_Images\Bar_Plot_with_Pandas.jpeg")
    # Legend came automatically and by default x tick values are 90 rotated

    # 2. Pie Chart of Global Death Distribution by Region
    plt.figure(figsize=(10,6))
    print(covidCases.df.groupby("WHO Region")['Deaths'].sum())
    plt.pie(list(covidCases.df.groupby("WHO Region")['Deaths'].sum()), frame=False, autopct='%1.1f%%', startangle=90)
    plt.legend(covidCases.df.groupby("WHO Region")['Deaths'].sum().index, loc='lower left', bbox_to_anchor=(1.0, 0.0), fontsize='small')
    plt.title("Deaths split by WHO Region")
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Pie_Plot.jpeg")

    # 3. Line Chart comparing Confirmed and Deaths for Top 5 Countries
    plt.figure(figsize=(10,4))
    plt.plot(covidCases.df['Confirmed'].nlargest().index,covidCases.df['Confirmed'].nlargest(), marker="o", label='Confirmed')
    plt.plot(covidCases.df['Deaths'].nlargest().index,covidCases.df['Deaths'].nlargest(),marker="D", label="Deaths")
    plt.ticklabel_format(style='plain', axis='y')
    plt.legend()
    plt.xlabel("Top 5 Countries")
    plt.ylabel("Count of Confirmed/Death caseas")
    plt.title("Line Chart comparing Confirmed and Deaths for Top 5 Countries")
    for xi, yi in zip(covidCases.df['Confirmed'].nlargest().index, covidCases.df['Confirmed'].nlargest()):
            plt.annotate(f'{yi}', xy=(xi, yi), xytext=(5, 5),
                        textcoords='offset points', fontsize=8,
                        bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))
    for xi, yi in zip(covidCases.df['Deaths'].nlargest().index, covidCases.df['Deaths'].nlargest()):
                plt.annotate(f'{yi}', xy=(xi, yi), xytext=(5, 5),
                            textcoords='offset points', fontsize=8,
                            bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Line_Plot.jpeg")

    # 4. Scatter Plot of Confirmed Cases vs Recovered Cases
    plt.figure(figsize=(18,7))
    plt.scatter(covidCases.df['Confirmed'].index, list(covidCases.df['Confirmed']), label='Confirmed')
    plt.scatter(covidCases.df['Recovered'].index, list(covidCases.df['Recovered']), label='Recovered')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tick_params(axis='x', which='major', labelsize=5.0)
    plt.ticklabel_format(style='plain', axis='y')
    plt.ylim(0, 500000)
    plt.yticks(np.arange(100000, 500001, 25000)) 
    plt.xlabel("Country", loc="center")
    plt.ylabel("Case Count")
    plt.title("Scatter Plot of Confirmed Cases vs Recovered Cases")
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Scatter_Plot.jpeg")

    # 5. Histogram of Death Counts across all Regions
    plt.figure(figsize=(10,6))
    print(list(covidCases.df['Deaths'].sort_values()))
    plt.hist(list(covidCases.df['Deaths']))
    plt.xlabel("Death counts")
    plt.ylabel("No of Countries in the Death count")
    plt.title("Histogram of Death Counts across all Regions")
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Histogram_Plot.jpeg")

    # 6. Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
    plt.figure()
    x1 = np.arange(len(covidCases.df['Confirmed'].head().index)) #arange from numpy
    x2 = [x + 0.25 for x in x1]
    x3 = [x + 0.25 for x in x2]
    plt.bar(x1, list(covidCases.df['Confirmed'].head()), width=0.25, color="yellow", label="Confirmed")
    plt.bar(x2, list(covidCases.df['Deaths'].head()), width=0.25, color="green", label="Deaths")
    plt.bar(x3, list(covidCases.df['Recovered'].head()), width=0.25, color="orange", label="Recovered")
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("Confirmed / Death / Recovered Cases")
    plt.title("Stacked Bar Chart of First 5 Countries by Confirmed / Death / Recovered Cases")
    plt.xticks([x + 0.25 for x in range(len(covidCases.df['Confirmed'].head().index))],covidCases.df['Confirmed'].head().index)
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Stacked_bar.jpeg")

    # 7. Box Plot of Confirmed Cases across Regions
    fig, axes = plt.subplots(1,2, figsize=(16,8))
    axes[0].boxplot(covidCases.df.groupby('WHO Region')['Confirmed'].sum())
    axes[0].set_title("Box Plot of Confirmed Cases across Regions")
    axes[0].set_ylabel("Count of Confirmed Cases")
    axes[0].ticklabel_format(style='plain', axis='y')
    axes[1].boxplot(covidCases.df.groupby('WHO Region')['Deaths'].sum())
    axes[1].set_title("Box Plot of Death Cases across Regions")
    axes[1].set_ylabel("Count of Death Cases")
    axes[1].ticklabel_format(style='plain', axis='y')
    fig.tight_layout()
    fig.savefig("HomeAssignments\Week 4\Plot_Images\Box_Plot_Sub_Plot.jpeg")

    # try with normal plt plot and pd plot
    # plt.figure()
    # print(covidCases.df.groupby('WHO Region')['Confirmed'].sum())
    # plt.boxplot(covidCases.df.groupby('WHO Region')['Confirmed'].sum())
    # plt.ticklabel_format(style='plain', axis='y')
    # plt.ylabel("Count of Confirmed Cases")
    # plt.title("Box Plot of Confirmed Cases across Regions")
    # box_plot_df = pd.DataFrame(covidCases.df.groupby('WHO Region')['Confirmed'].sum())
    # box_plot_df.plot(kind="box",ylabel="Count of Confirmed Cases", title="Box Plot of Confirmed Cases across Regions").ticklabel_format(style='plain', axis='y')

    # 8. Trend Line: Plot Confirmed cases for India vs another chosen country (side by side comparison)
    plt.figure()
    x = np.array([covidCases.df['Confirmed']['India'],covidCases.df['Confirmed']['China']])
    y = np.array([0,1])
    plt.scatter([x],y,label="Data Points")
    coefficients = np.polyfit(x,y,1)
    trendline_function = np.poly1d(coefficients)
    trendline_y = trendline_function(x)
    plt.plot(x, trendline_y, color='red', linestyle='--', label='Trendline')
    plt.ticklabel_format(style="plain")
    plt.title("Trend Line: Confirmed cases - India vs China")
    plt.xlabel("Confirmed Cases Count")
    plt.ylabel("Country Index")
    plt.savefig("HomeAssignments\Week 4\Plot_Images\Trend_Line.jpeg")
    
    # plt.show()