import sqlite3
import pandas as pd
from datetime import timedelta
from pathlib import Path

DB_PATH = "data/rides.db"
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def generate_report():
    with sqlite3.connect(DB_PATH) as conn:
        # Find max trip_start_time
        max_date_query = "SELECT MAX(trip_start_time) AS max_date FROM trips;"
        max_date = pd.read_sql_query(max_date_query, conn).iloc[0, 0]

        if not max_date:
            print("⚠️ No data in trips table")
            return

        max_date = pd.to_datetime(max_date)
        start_date = max_date - timedelta(days=7)
        end_date = max_date

        start_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
        end_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

        print(f"Generating report for last week: {start_str} → {end_str}")

        # Load last week's data
        query = """
        SELECT * FROM trips
        WHERE trip_start_time BETWEEN ? AND ?;
        """
        df = pd.read_sql_query(query, conn, params=[start_str, end_str])

        if df.empty:
            print("⚠️ No rides in this period")
            return

        # KPIs
        kpis = {
            "total_rides": len(df),
            "completed_rides": (df["trip_status"] == "completed").sum(),
            "cancelled_rides": (df["trip_status"] != "completed").sum(),
            "avg_distance_kms": df["distance_kms"].mean(),
            "avg_fare_usd": df["price_usd"].mean(),
            "avg_wait_mins": df["wait_time"].mean(),
        }
        kpi_df = pd.DataFrame([kpis])

        # Save Excel report
        report_path = REPORTS_DIR / f"weekly_report_{end_date.date()}.xlsx"
        with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
            kpi_df.to_excel(writer, sheet_name="KPIs", index=False)
            df.to_excel(writer, sheet_name="RawData", index=False)

        print(f"✅ Weekly report saved: {report_path}")

if __name__ == "__main__":
    generate_report()
