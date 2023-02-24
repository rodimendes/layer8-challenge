import plotly.express as px


def event_occurences(file):
    """
    Returns a simple chart of the chosen column and its occurrence
    """
    choices = [column for column in file.columns if file[column].nunique() < 200]
    column_name = input(f"Choose a column {choices}: ")
    event_occur = file[column_name].value_counts()
    graph = px.bar(x=event_occur.index, y=event_occur.values, color=event_occur.values, color_continuous_scale='Aggrnyl', hover_name=file[column_name].value_counts())
    graph.update_layout(xaxis_title=f'{column_name.capitalize()}', yaxis_title='Amount', coloraxis_showscale=False)
    graph.show()


def date_occurrences(file):
    """
    Returns pie chart with date data
    """
    dates_df = file.select_dtypes(include="datetime")
    column_name = input(f"Choose a column {dates_df.columns}: ")
    years_occur = dates_df[column_name].dt.year.value_counts()
    year_graph = px.pie(data_frame=years_occur, values=years_occur.values, hover_name=years_occur.index, hole=0.5, names=years_occur.index)
    year_graph.show()
