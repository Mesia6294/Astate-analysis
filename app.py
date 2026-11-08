import streamlit as st

from modules.data_loader import load_data
from modules.preprocessing import preprocess_data
import modules.analysis as ana
import modules.visualization as vis 


# Streamlit 頁面設定
st.set_page_config(
    page_title="新北市不動產分析",
    page_icon="🏢",
    layout="wide",
)

st.title("新北市2017~2026年 房地產交易資料分析")
st.caption("✒️本站資料來源:不動產交易實價查詢服務網(內政部)，類型:公寓、華夏、大樓，經清理後僅挑選'住房不動產'")

# 載入與處理資料
df = load_data("data/10年份資料.csv")
df = preprocess_data(df)

st.sidebar.markdown("## 你好~💕")
st.sidebar.markdown("## 🔎 選擇查詢選項")
# Sidebar：篩選器
# 年份
years = sorted(df["交易年"].unique())
selected_year = st.sidebar.selectbox("選擇交易年", years,index=8)
# 鄉鎮市區
areas = sorted(df["鄉鎮市區"].unique())
selected_area = st.sidebar.selectbox("選擇鄉鎮市區", areas,index=13)
st.sidebar.markdown("---")

st.sidebar.write("📢本網站提供新北市")
st.sidebar.write("2017~2026年住房資料")
st.sidebar.write("查看各種分析/視覺化")

st.sidebar.caption(f"📊 當前資料總量：**{len(df)}** 筆")



def show_chart(fig):
    """管理plotly的顯示方式"""
    st.plotly_chart(fig, width="stretch", theme="streamlit")


# 主畫面分頁
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "交易量分布",
    "各區交易趨勢",
    "建物坪數分析",
    "價格趨勢",
    "建物型態與管理",
])

with tab1:# 第一頁：交易量分布
    st.caption("📌 可以充分了解每個區域的熱絡度，直條圖可以看對比，圓餅圖可以看占比")
    left, center, right = st.columns([1, 8, 1])

    all_counts = ana.transaction_count_by_district(df)
    year_counts = ana.transaction_count_by_year(df, selected_year)
    all_pie_data = ana.prepare_pie_data(all_counts)
    year_pie_data = ana.prepare_pie_data(year_counts)

    with center:
        col1, col2 = st.columns(2)
        with col1:
            st.header("總交易分布圖")
            fig = vis.plot_transaction_bar(all_counts.sort_values(),"2017~2026年")
            show_chart(fig)
        with col2:
            st.header("年度交易分布圖")
            fig = vis.plot_transaction_bar(year_counts.sort_values(), f"請選擇查詢的📆年份：{selected_year}年")
            show_chart(fig)

        col1, col2 = st.columns(2)
        with col1:
            st.header("總交易占比圖")
            fig = vis.plot_transaction_pie(all_pie_data, "2017~2026年")
            show_chart(fig)
        with col2:
            st.header("年度交易占比圖")
            fig = vis.plot_transaction_pie(year_pie_data, f"請選擇查詢的📆年份：{selected_year}年")
            show_chart(fig)



with tab2:#第二頁：各區的交易趨勢
    st.caption("📌 可以了解全部 / 各區10年的活絡趨勢")
    left, center, right = st.columns([1, 8, 1])
    
    df_n = ana.total_transaction_count_by_year(df)
    area_data = ana.area_transaction_by_year(df, selected_area)
    df_gr = ana.all_area_transaction_by_year(df)

    with center:
        col1, col2 = st.columns(2)
        with col1:
            st.header("整體趨勢圖")
            fig = vis.plot_yearly_transaction_trend(df_n, "2017~2026年")
            show_chart(fig)
        with col2:
            st.header("區域趨勢")
            fig = vis.plot_area_transaction_bar(area_data, f"請選擇查詢的🧭區域：{selected_area}")
            show_chart(fig)

        col1, col2 = st.columns(2)
        with col1:
            st.header("全區態勢圖")
            fig = vis.plot_all_area_transaction_trend(df_gr, "2017~2026年")
            show_chart(fig)
        with col2:
            st.header("區域趨勢")
            fig = vis.plot_area_transaction_line(area_data, f"請選擇查詢的🧭區域：{selected_area}")
            show_chart(fig)



with tab3:# 第三頁：建物坪數分析
    st.caption("📌 可以了解各區坪數中位數，各區對坪數高低的需求指標")
    left, center, right = st.columns([1, 8, 1])
    
    median_data = ana.district_median_ping_by_year(df, selected_year)
    ping_data = ana.area_ping_distribution(df, selected_area, selected_year)

    with center:
        col1, col2 = st.columns(2)
        with col1:
            st.header("區域坪數(中位數)")
            fig = vis.plot_district_median_ping(median_data,f"請選擇查詢的📆年份：{selected_year}年")
            show_chart(fig)
        with col2:
            st.header("區域坪數分布")
            fig = vis.plot_area_ping_hist(ping_data,f"請選擇查詢的🧭和📆：{selected_area} {selected_year}年")
            show_chart(fig)



with tab4:# 第四頁：價格趨勢分析
    st.caption("📌 每坪單價中位數、(坪數中位x單價中位)，更真實的價位可以參考")
    left, center, right = st.columns([1, 8, 1])
    
    avg_price = ana.area_median_ping_price(df, selected_area)
    median_price = ana.area_median_estimated_total_price(df, selected_area)

    with center:
        col1, col2 = st.columns(2)
        with col1:
            st.header("每坪單價中位數")
            fig = vis.plot_area_total_price(avg_price,f"請選擇查詢的🧭區域趨勢：{selected_area} ")
            show_chart(fig)
        with col2:
            st.header("總價中位數")
            fig = vis.plot_area_total_price(median_price,f"請選擇查詢的🧭區域趨勢：{selected_area} ")
            show_chart(fig)



with tab5:# 第五頁：建物型態與單價分析
    st.caption("📌 型態間的差異造成的價差表現，並搭配型態的數量了解每區的都市形態")
    left, center, right = st.columns([1, 8, 1])
    
    area_year_df = ana.filter_area_year(df, selected_area, selected_year)

    with center:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("型態的交易差")
            fig = vis.plot_building_type_count(area_year_df,f"請選擇🧭和📆：{selected_area} {selected_year}年")
            show_chart(fig)

        with col2:
            st.header("型態的價格差")
            fig = vis.plot_building_type_price_box(area_year_df,"")
            show_chart(fig)

        with col3:
            st.header("管理的價格差")
            fig = vis.plot_management_price_box(area_year_df,"")
            show_chart(fig)

        with col4:
            st.header("單價中位數")
            fig = vis.plot_area_price_box(area_year_df,"")
            show_chart(fig)
