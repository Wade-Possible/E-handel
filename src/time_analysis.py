import pandas as pd


def add_time_columns(df):
    result = df.copy()  # make a copy so the original table is not changed
    result["date"] = pd.to_datetime(result["date"])  # make sure the date column is a real date
    result["month_number"] = result["date"].dt.month  # month as a number for sorting
    result["month_name"] = result["date"].dt.month_name()  # month as a name, ex. January
    result["weekday_number"] = result["date"].dt.weekday + 1  # day as a number for sorting, 1 = Monday
    result["weekday_name"] = result["date"].dt.day_name()  # day as a name, ex. Monday
    result["week_number"] = result["date"].dt.isocalendar().week  # week of the year (week 1 starts on Monday 1 January 2024)

    return result


def summarize_revenue(df, group_columns):
    summary = (
        df.groupby(group_columns)
        .agg(
            total_revenue=("revenue", "sum"),
            total_units=("units", "sum"),
            order_count=("order_id", "count"),
        )
        .reset_index()  # turn the group labels back into normal columns
    )
    summary["average_order_value"] = summary["total_revenue"] / summary["order_count"]
    summary["total_revenue"] = summary["total_revenue"].round(2)
    summary["average_order_value"] = summary["average_order_value"].round(2)

    return summary