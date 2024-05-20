import pandas as pd

def process_dates_and_ids(df):
    df['date'] = pd.to_datetime(df['date'])
    df['start_station_id'] = df['start_station_id'].astype('category')
    df['end_station_id'] = df['end_station_id'].astype('category')
    df['duration_seconds'] = (df['end_time'] - df['start_time']).dt.total_seconds()
    return df

def split_datasets(df):
    dataset1 = df[df['duration_seconds'] <= 600]
    dataset2 = df[df['duration_seconds'] > 600]
    return dataset1, dataset2

def average_duration(dataset1):
    return dataset1.groupby('start_station_id')['duration_seconds'].mean().reset_index(name='average_duration')

def count_trips(dataset2):
    return dataset2.groupby('start_station_id').size().reset_index(name='total_trips')

def final_stats(dataset1_processed, dataset2_processed):
    stats = {
        'Dataset': ['dataset1_processed', 'dataset2_processed'],
        'Rows': [dataset1_processed.shape[0], dataset2_processed.shape[0]]
    }
    return pd.DataFrame(stats)
