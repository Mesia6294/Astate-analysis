
import pandas as pd


def transaction_count_by_district(df: pd.DataFrame) -> pd.Series:
    """各鄉鎮市區的交易筆數。"""
    return df["鄉鎮市區"].value_counts()

def transaction_count_by_year(df: pd.DataFrame,year: int) -> pd.Series:
    """指定交易年的各鄉鎮市區交易筆數。"""
    return df.loc[df["交易年"] == year,"鄉鎮市區"].value_counts()

def prepare_pie_data(counts: pd.Series,threshold: float = 0.02) -> pd.Series:
    """將低於指定比例的分類合併為「其他」。"""
    ratio = counts / counts.sum()
    main = counts[ratio >= threshold]
    others = counts[ratio < threshold].sum()
    if others > 0:
        return pd.concat([main,pd.Series({"其他": others})])
    return main

def total_transaction_count_by_year(df: pd.DataFrame) -> pd.Series:
    """每年度總交易筆數。"""
    return df["交易年"].value_counts().sort_index()

def area_transaction_by_year(df: pd.DataFrame,area: str) -> pd.Series:
    """指定區域每年度的交易筆數。"""
    area_df = df[df["鄉鎮市區"] == area]
    return area_df["交易年"].value_counts().sort_index()

def all_area_transaction_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """所有區域每年度的交易筆數。"""
    return df.groupby(["交易年", "鄉鎮市區"]).size().unstack(fill_value=0)

def district_median_ping_by_year(df: pd.DataFrame,year: int) -> pd.Series:
    """指定年份，各鄉鎮市區的建物移轉坪數中位數。"""
    year_df = df[df["交易年"] == year]
    return year_df.groupby("鄉鎮市區")["轉移坪數"].median().sort_values()

def area_ping_distribution(df: pd.DataFrame,area: str,year: int) -> pd.Series:
    """指定年份、指定區域的建物移轉坪數資料。"""
    area_df = df[(df["鄉鎮市區"] == area) &(df["交易年"] == year)]
    return area_df["轉移坪數"]

def area_median_ping_price(df: pd.DataFrame,area: str) -> pd.Series:
    """指定區域每年度的每坪單價中位數。"""
    area_df = df[df["鄉鎮市區"] == area]
    return area_df.groupby("交易年")["每坪單價"].median().sort_index()

def area_median_estimated_total_price(df: pd.DataFrame,area: str) -> pd.Series:
    """指定區域每年度的中位數坪數 × 中位數每坪單價。"""
    area_df = df[df["鄉鎮市區"] == area]
    result = area_df.groupby("交易年").agg({"轉移坪數": "median","每坪單價": "median"})
    estimated_price = (result["轉移坪數"] * result["每坪單價"])
    return estimated_price.sort_index()

def filter_area_year(df: pd.DataFrame,area: str,year: int) -> pd.DataFrame:
    """篩選指定區域與年份的交易資料。"""
    result = df[(df["鄉鎮市區"] == area) &(df["交易年"] == year)]
    return result

