def compute_aov(df):
    return df["revenue"].sum()/df["order_id"].nunique()

def find_outliers(df):
    q1 = df["revenue"].quantile(0.25)
    q3 = df["revenue"].quantile(0.75)
    upper_limit = q3 + 1.5 * (q3 - q1)
    return df[df["revenue"] > upper_limit]

def order_spread(df):
    return df["revenue"].describe().round(2)