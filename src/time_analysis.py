import pandas as pd

def add_time_columns(df):
    result = df.copy()  # make a copy so the original table is not changed
    result["month_number"] = result["date"].dt.month  # month as a number for sorting
    result["month_name"] = result["date"].dt.month_name()
    result["weekday_number"] = result["date"].dt.weekday +1 # day as a number for sorting
    result["weekday_name"] = result["date"].dt.day_name()

    return result

def summarize_revenue(df, group_columns):
    summary = (
        df.groupby(group_columns)
        .agg(
            total_revenue = ("revenue", "sum"),
            total_units = ("units", "sum"),
            order_count = ("order_id", "count")
        )
        .reset_index()  # turn the week labels back into normal columns
    )
    summary["average_order_value"] = summary["total_revenue"] / summary["order_count"]
    summary = summary.round(2)

    return summary