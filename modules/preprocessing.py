

import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    坪數轉換與清理資料。
    """
 
    # 平方公尺轉換成坪數
    df["每坪單價"] = (df["總價元"]/df["建物移轉平方"]*3.3).round(1)
    df["轉移坪數"] = (df["建物移轉平方"] / 3.3).round(1)
 
    # 為了以年份為組別分析數據，新建[交易年]
    df["交易年"]=df["交易年月日"].astype(str).str[:3].astype(int)+1911
 
    # 清除不必要的欄目:建物移轉平方/單價元平方公尺/土地移轉平方
    df = df.drop(columns=["建物移轉平方","單價元平方公尺","土地移轉平方","交易年月日"])

    return df