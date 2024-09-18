import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importer les données et définir l'index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Nettoyage des données
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Créer un graphique en ligne
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    
    # Ajouter un titre et des étiquettes
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Sauvegarder la figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Préparer les données pour le bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Grouper les données par année et mois
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Créer un graphique en barres
    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Sauvegarder la figure
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Préparer les données pour les box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Créer les box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Sauvegarder la figure
    fig.savefig('box_plot.png')
    return fig
