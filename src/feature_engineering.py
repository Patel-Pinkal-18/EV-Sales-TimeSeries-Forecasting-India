def create_time_features(df):
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    return df

def create_lag_features(df, target):
    df['lag_1'] = df[target].shift(1)
    df['lag_3'] = df[target].shift(3)
    df['rolling_mean_3'] = df[target].rolling(3).mean()
    df = df.dropna()
    return df