import pandas as pd

# 從csv檔案使用pd陣列讀取
def load_data(file_path: str) -> pd.DataFrame:
    """讀取 CSV 資料。"""
    df = pd.read_csv(file_path)
    return df
