# 🏢 Astate-analysis｜新北市不動產交易資料分析

**Astate-analysis** 是一個使用 Python 與 Streamlit 開發的互動式房地產資料分析儀表板。

本專案以不動產交易資料為基礎，透過 Pandas 進行資料處理，並使用 Plotly、Seaborn 等視覺化工具，分析不同年度、行政區及建物條件下的交易分布與價格特徵。

使用者可以透過選擇年份與行政區，查看不同條件下的分析結果。

## 🌐 線上展示

**Live Demo：**

https://astate-analysis-ghnzj5c8sisejksadtaax7.streamlit.app/

## ✨ 專案功能

### 1. 資料總覽
- 全期間各行政區交易次數分析
- 指定年度交易次數分析
- 行政區交易占比分布
- 交易資料視覺化

### 2. 鄉鎮區域分析
- 歷年不動產交易趨勢
- 各行政區交易次數比較
- 年度與區域交易分布分析

### 3. 建物坪數分析
- 全市建物坪數中位數分析
- 指定行政區建物坪數分布
- 直方圖分析

### 4. 建物條件與價格分析
- 不同建物型態的交易次數
- 不同建物型態的每坪單價分布
- 不同管理組織的每坪單價分布
- 指定行政區的價格分布分析

### 5. 互動式資料篩選
- 年份選擇
- 行政區選擇
- 透過 Sidebar 控制分析條件
- 圖表依據選擇條件動態更新

## 🛠️ 使用技術

| 技術 | 用途 |
|---|---|
| Python | 主要程式語言 |
| Pandas | 資料清理與分析 |
| Streamlit | 互動式網頁應用程式 |
| Plotly | 互動式資料視覺化 |
| Seaborn | 統計圖表視覺化 |
| Matplotlib | 圖表繪製 |
| Git | 版本控制 |
| GitHub | 原始碼管理 |
| Streamlit Community Cloud | 雲端部署 |

## 📁 專案結構

```text
Astate-analysis/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── 10年份資料.csv
│
└── modules/
    ├── __init__.py
    ├── analysis.py
    ├── data_loader.py
    ├── preprocessing.py
    └── visualization.py
```

### 模組說明

| 檔案 | 功能 |
|---|---|
| app.py | Streamlit 主程式與頁面配置 |
| data_loader.py | 資料讀取 |
| preprocessing.py | 資料清理與前處理 |
| analysis.py | 資料分析與統計計算 |
| visualization.py | 圖表繪製與視覺化 |
| requirements.txt | Python 套件依賴清單 |

## 🚀 本機執行方式

### 1. Clone 專案

```bash
git clone https://github.com/Mesia6294/Astate-analysis.git
```

### 2. 進入專案資料夾

```bash
cd Astate-analysis
```

### 3. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 4. 啟動 Streamlit

```bash
streamlit run app.py
```

啟動後即可透過瀏覽器開啟本機儀表板。

## 📊 資料處理

本專案使用 CSV 格式的不動產交易資料，透過 Pandas 進行資料清理與欄位處理。


分析內容包含：

- 交易年度
- 鄉鎮市區
- 建物型態
- 管理組織
- 建物移轉面積
- 總價
- 每坪單價

每坪單價計算方式：

```python
建物轉移坪數 /總價元   R-squared:                    0.587<<選擇
土地移轉平方 /總價元   R-squared:                    0.382
df["每坪單價"] = (df["總價元"] / df["建物移轉平方"] * 3.3).round(1)
```

## ☁️ Deployment

本專案使用 **Streamlit Community Cloud** 部署。

- Source Code：GitHub
- Repository：Mesia6294/Astate-analysis
- Branch：main
- Entry Point：app.py

## 🎯 Project Objective

透過實際的不動產交易資料，練習並整合以下技能：

- Python 資料處理
- Pandas 資料分析
- 資料視覺化
- Streamlit 互動式應用程式開發
- Python 模組化設計
- Git 版本控制
- GitHub 專案管理
- 雲端應用程式部署

---

**Developed with Python & Streamlit.**