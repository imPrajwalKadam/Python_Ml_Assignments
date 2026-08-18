"""
Q8 .plot  a line chart of marks for 'Amit'  accross all subjects  .a

data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def main():
    border = 50 * '-'
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }

    # load to pandas dataframe
    df = pd.DataFrame(data)

    print(border)
    print(df)
    print(border)

    #Shape of dataset
    print("Shape of dataset")
    print(df.shape)
    print(border)

    #Print columns of dataframe
    print("Print columns of dataframe")
    print(df.columns)
    print(border)

    #Data type 
    print("Data type")
    print(df.dtypes)
    print(border)

    print("descriptive statistics")
    print(df.describe())
    print(border)

    print("Add total column")
    df['Total'] = df.sum(axis=1,numeric_only=True)
    print(df)   
    print(border)

    print(" Display Students who scored  more than  85 in Science. ")

    print(df[df['Science'] > 85])
    print(border)

    print("Replace 'Pooja' to 'Puja' in 'Name' Column")

    df.loc[df['Name'] ==  'Pooja','Name'] = 'Puja'
    print(df)

    print(border)

    print("Sort the dataframe  by 'total' marks in descending order.")
    df = df.sort_values(by='Total',ascending=False)
    print(df)

    print(border)

    print("Create a bar plot of student names vs total marks.   ")

    # sns.barplot(df,x="Name",y="Total")
    # plt.show()

    print(border)
    print(".plot  a line chart of marks for 'Amit'  accross all subjects  .")
    amit_row = df[df['Name'] == 'Amit'].drop(columns=['Name', 'Total'])

    amit_df = amit_row.melt(var_name='Subject', value_name='Marks')

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(7, 4.5))

    sns.lineplot(
    data=amit_df, 
    x='Subject', 
    y='Marks', 
    marker='o', 
    linewidth=3, 
    color='dodgerblue'
    )


    plt.title("Amit's Subject-Wise Marks", fontweight='bold')
    plt.xlabel("Subjects")
    plt.ylabel("Marks Obtained")
    plt.ylim(0, 100) 
    plt.show()


if __name__ == "__main__":
    main()
