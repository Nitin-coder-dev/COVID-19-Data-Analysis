import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import io
import base64

df = pd.read_csv("covid_19_india.csv")
df = df.drop(['ConfirmedIndianNational', 'ConfirmedForeignNational', 'Sno', 'Time'], axis=1)


def drop_star(df):
    for i in df['State/UnionTerritory'].items():
        if i[1][-3:] == "***":
            df.drop(i[0], inplace=True)


drop_star(df)
df['State/UnionTerritory'].unique()

df.rename(columns={'State/UnionTerritory': 'States'}, inplace=True)
df['States'] = df['States'].replace(['Maharashtra'], 'MH')
df['States'] = df['States'].replace(['Kerala'], 'KL')
df['States'] = df['States'].replace(['Karnataka'], 'KA')
df['States'] = df['States'].replace(['Tamil Nadu'], 'TN')
df['States'] = df['States'].replace(['Andhra Pradesh'], 'AP')
df['States'] = df['States'].replace(['Uttar Pradesh'], 'UP')
df['States'] = df['States'].replace(['Madhya Pradesh'], 'MP')
df['States'] = df['States'].replace(['Karanataka'], 'KA')
df['States'] = df['States'].replace(['West Bengal'], 'WB')
df['States'] = df['States'].replace(['Himachal Pradesh'], 'HP')
df['States'] = df['States'].replace(['Jammu and Kashmir'], 'JNK')
df['States'] = df['States'].replace(['Arunachal Pradesh'], 'Arunachal')
df['States'] = df['States'].replace(['Dadra and Nagar Haveli and Daman and Diu'], 'DNHDD')
df['States'] = df['States'].replace(['Andaman and Nicobar Islands'], 'Andaman')


def stats(date):
    df1 = df[df.Date == date]
    death = df1['Deaths'].sum()
    confirm = df1['Confirmed'].sum()
    cured = df1['Cured'].sum()
    return death, cured, confirm


def piechart(date):
    Death, Cured, Confirm = stats(date)
    dataFrame = pd.DataFrame({"Cases": ['Deaths', 'Cured', 'Confirmed Cases'], "No. of Cases": [Death, Cured, Confirm]})
    plt.pie(dataFrame["No. of Cases"], labels=dataFrame["Cases"], explode=(0.005, 0.005, 0.005), startangle=90,
            autopct='%1.1f%%', colors=['salmon', 'tomato', 'darksalmon'])

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def max_cases(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=False)
    plt.figure(figsize=(12, 4), dpi=80)
    plt.bar(df1['States'][:10], df1['Confirmed'][:10], align='center', color='blue')
    plt.ylabel('Number of Confirmed Cases', size=12)
    plt.title("States with maximum confirmed cases till Aug’21", size=16)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def lowest_cases(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=True)
    plt.figure(figsize=(12, 4), dpi=80)
    plt.bar(df1['States'][:10], df1['Confirmed'][:10], align='center', color='blue')
    plt.ylabel('Number of Confirmed Cases', size=12)
    plt.title("States with lowest confirmed cases till Aug’21", size=16)
    plt.subplots_adjust(left=None, bottom=0.2, right=None, top=0.85, wspace=None, hspace=None)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def high_impact_confirmed(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=False)
    plt.figure(figsize=(20, 8))
    sns.barplot(data=df1.sort_values('Confirmed', ascending=False).head(20), x="States", y="Confirmed", linewidth=0,
                edgecolor="black")
    plt.title(f"Top 20 highly impacted states by Confirmed cases as on {date}", size=20)
    plt.xlabel("States", size=18)
    plt.ylabel("Confirmed", size=18)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def lowest_impact_confirmed(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=False)
    plt.figure(figsize=(20, 8))
    sns.barplot(data=df1.sort_values('Confirmed', ascending=True).tail(20), x="States", y="Confirmed", linewidth=0,
                edgecolor="black")
    plt.title(f"Top 20 lowest impacted states by Confirmed cases as on {date}", size=20)
    plt.xlabel("States", size=18)
    plt.ylabel("Confirmed", size=18)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def high_impact_cured(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=False)
    plt.figure(figsize=(20, 8))
    sns.barplot(data=df1.sort_values('Cured', ascending=False).head(20), x="States", y="Cured", linewidth=0,
                edgecolor="black")
    plt.title(f"Top 20 states by number of total cured cases as on {date}", size=20)
    plt.xlabel("States", size=18)
    plt.ylabel("Cured", size=18)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image


def high_impact_death(date):
    df1 = df[df.Date == date]
    df1 = df1.sort_values(by=['Confirmed'], ascending=False)
    plt.figure(figsize=(20, 8))
    sns.barplot(data=df1.sort_values('Deaths', ascending=False).head(20), x="States", y="Deaths", linewidth=0,
                edgecolor="black")
    plt.title(f"Top 20 states by total number of deaths as on {date}", size=20)
    plt.xlabel("States", size=18)
    plt.ylabel("Deaths", size=18)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image



def line_graph(date):
    df1 = df[df.Date == date]
    plt.title(" ")
    sns.set(rc={"figure.figsize": (10, 8)})
    sns.swarmplot(x="Date", y="Confirmed", data=df1)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return chart_image

def table(date):
    df_latest = df[df.Date == date]
    df2= df_latest.copy()
    df_Top= df2.head(10)
    df_Top.style.background_gradient(cmap='Reds')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    table_image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    return table_image

def main():
    date = "2021-05-18"
    Death, Cured, Confirmed = stats(date)
    print(df.head())
    print(df.tail())
    # print(f"Number of death: {Death} \nNumber of Cured cases: {Cured}\nNumber of Confirmed cases: {Confirmed}")
    # print(df.tail(5))
    # piechart(date)
    # max_cases(date)
    # lowest_cases(date)
    # line_graph(date)
    return


if __name__ == '__main__':
    main()
