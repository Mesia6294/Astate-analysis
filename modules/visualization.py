"""Plotly 視覺化函式。所有函式回傳 Plotly Figure，供 Streamlit 顯示。"""

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

DEFAULT_TEMPLATE = "plotly_white"

def plot_transaction_bar(counts: pd.Series, title: str):
    """區域交易次數的長條圖。"""
    plot_data = pd.DataFrame({"鄉鎮市區": counts.index.astype(str),"交易次數": counts.values})
    fig = px.bar(
        plot_data,
        x="交易次數",
        y="鄉鎮市區",
        orientation="h",
        title=title
    )
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=30))
    return fig

def plot_transaction_pie(pie_data: pd.Series, title: str):
    """交易占比圓餅圖。"""
    fig = px.pie(
        names=pie_data.index.astype(str),
        values=pie_data.values,
        title=title
    )
    fig.update_traces(textinfo="percent", texttemplate="%{percent:.1%}", hovertemplate="%{label}<br>交易筆數：%{value:,}<br>占比：%{percent}<extra></extra>")
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=30))
    return fig

def plot_yearly_transaction_trend(data: pd.Series, title: str):
    """年度交易量直條與折線圖。"""
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data.index, y=data.values, name="交易數量"))
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data.values,
        mode="lines+markers",
        name="交易趨勢",
        line=dict(color="red")
    ))
    fig.update_layout(
        title=title,
        xaxis_title="交易年",
        yaxis_title="交易數量",
        height=450,
        margin=dict(l=20, r=20, t=60, b=40),
        xaxis=dict(tickmode="array", tickvals=list(data.index))
    )
    return fig

def plot_area_transaction_bar(area_data: pd.Series, title: str):
    """區域年度交易量直條圖。"""
    plot_data = pd.DataFrame({"交易年": area_data.index, "交易數量": area_data.values})
    fig = px.bar(
        plot_data,
        x="交易年",
        y="交易數量",
        title=title
    )
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=40))
    fig.update_xaxes(tickmode="array", tickvals=list(area_data.index))
    return fig

def plot_all_area_transaction_trend(data: pd.DataFrame, title: str):
    """所有區域年度交易量折線圖。"""
    plot_data = data.rename_axis("交易年").reset_index().melt(
        id_vars="交易年", var_name="鄉鎮市區", value_name="交易數量"
    )
    fig = px.line(
        plot_data,
        x="交易年",
        y="交易數量",
        color="鄉鎮市區",
        markers=True,
        title=title
    )
    fig.update_layout(
        showlegend=False,
        height=450,
        margin=dict(l=20, r=20, t=60, b=40),
        hovermode="closest"
    )
    fig.update_xaxes(tickmode="array", tickvals=list(data.index))
    return fig

def plot_area_transaction_line(area_data: pd.Series, title: str):
    """區域年度交易量折線圖。"""
    plot_data = pd.DataFrame({"交易年": area_data.index, "交易數量": area_data.values})
    fig = px.line(
        plot_data,
        x="交易年",
        y="交易數量",
        markers=True,
        title=title
    )
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=40))
    fig.update_xaxes(tickmode="array", tickvals=list(area_data.index))
    return fig

def plot_district_median_ping(ping_data: pd.Series, title: str):
    """區域建物坪數中位數直條圖。"""
    plot_data = pd.DataFrame({"鄉鎮市區": ping_data.index.astype(str), "坪數（坪）": ping_data.values})
    fig = px.bar(
        plot_data,
        x="鄉鎮市區",
        y="坪數（坪）",
        title=title
    )
    fig.update_yaxes(range=[20, 60])
    fig.update_xaxes(tickangle=45)
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=90))
    return fig

def plot_area_ping_hist(ping_data: pd.Series, title: str):
    """區域建物坪數直方圖。"""
    fig = px.histogram(
        x=ping_data,
        nbins=30,
        title=title,
        labels={"x": "坪數（坪）", "count": "交易筆數"}
    )
    fig.update_traces(marker_line_width=1,xbins=dict(start=0,end=80,size=5))
    fig.update_xaxes(range=[0, 80])
    fig.update_layout(xaxis_title="坪數（坪）", yaxis_title="交易筆數", height=450,
                      margin=dict(l=20, r=20, t=60, b=50))
    return fig

def plot_area_total_price(price_data: pd.Series, title: str):
    """區域年度價格趨勢，單位轉換為萬元。"""
    plot_data = pd.DataFrame({"交易年": price_data.index, "價格（萬元）": price_data.values / 10000})
    fig = px.line(
        plot_data,
        x="交易年",
        y="價格（萬元）",
        markers=True,
        title=title
    )
    fig.update_xaxes(tickmode="array", tickvals=list(price_data.index))
    fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=40))
    return fig

def plot_building_type_count(data: pd.DataFrame, title: str):
    """建物型態交易數量。"""
    count_data = data["建物型態"].value_counts().rename_axis("建物型態").reset_index(name="交易數量")
    fig = px.bar(
        count_data,
        x="建物型態",
        y="交易數量",
        color="建物型態",
        title=title
    )
    # 保留原圖設定：隱藏 X 軸各類別文字。
    fig.update_xaxes(showticklabels=False, title_text="")
    fig.update_layout(showlegend=False, height=450, margin=dict(l=15, r=15, t=70, b=35))
    return fig

def plot_building_type_price_box(data: pd.DataFrame, title: str):
    """型態分類每坪單價盒鬚圖。"""
    fig = px.box(
        data,
        x="建物型態",
        y="每坪單價",
        color="建物型態",
        points=False,
        title=title
    )
    fig.update_xaxes(showticklabels=False, title_text="建物型態")
    fig.update_layout(showlegend=False, height=450, margin=dict(l=15, r=15, t=70, b=55))
    return fig

def plot_management_price_box(data: pd.DataFrame, title: str):
    """無管理分類，每坪單價盒鬚圖。"""
    fig = px.box(
        data,
        x="有無管理",
        y="每坪單價",
        color="有無管理",
        points=False,
        title=title
    )
    fig.update_layout(showlegend=False, height=450, margin=dict(l=15, r=15, t=70, b=55))
    return fig

def plot_area_price_box(data: pd.DataFrame, title: str):
    """區域每坪單價盒鬚圖。"""
    fig = px.box(
        data,
        y="每坪單價",
        points=False,
        title=title,
        labels={"每坪單價": "每坪單價（元）"}
    )
    fig.update_xaxes(showticklabels=False, title_text="")
    fig.update_layout(showlegend=False, height=450, margin=dict(l=15, r=15, t=70, b=35))
    return fig