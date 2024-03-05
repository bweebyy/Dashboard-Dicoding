import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib
import matplotlib.image as mpimg
from scipy import stats
import seaborn as sns
import streamlit as st

ecommerce = pd.read_csv("C:/Users/Latifatul Khumairoh/anaconda3/envs/StreamlitEnv/mydata.csv")

st.title("E-Commerce Public Data Analysis")

st.write("**This is a dashboard for analyzing E-Commerce public data.**")

cats_terjual = ecommerce.groupby('product_category_name_english')['product_id'].count().reset_index().sort_values(by = 'product_id', ascending = False)
cats_penjualan = ecommerce.groupby('product_category_name_english')['payment_value'].sum().reset_index().sort_values(by = 'payment_value', ascending = False)

fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (16,8))
sns.barplot(x="product_id", y="product_category_name_english", data=cats_terjual.head(10), palette = 'terrain_r', ax = ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel('Jumlah Produk Terjual')
ax[0].set_title('10 Kategori Produk dengan Jumlah Produk Terjual Tertinggi', loc="center", fontsize=14)
sns.barplot(x="payment_value", y="product_category_name_english", data=cats_penjualan.head(10), palette = 'terrain_r', ax = ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel('Jumlah Penjualan ($)')
ax[1].set_title('10 Kategori Produk dengan Jumlah Penjualan Tertinggi', loc="center", fontsize=14)

plt.suptitle("Grafik Kategori Produk Terjual Terbanyak dan Penjualan Tertinggi", fontsize=16)
st.pyplot(fig)

review_scores = ecommerce['review_score'].value_counts().sort_values(ascending=False)
most_score = review_scores.idxmax()

fig, ax = plt.subplots(figsize = (10, 5))
sns.barplot(x = review_scores.index,
            y = review_scores.values,
            order = review_scores.index,
            palette = ["#72F626" if score == most_score else "#F3F9D1" for score in review_scores.index]
            )

plt.title("Tingkat Kepuasan Pelanggan", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Jumlah")
st.pyplot(fig)

group_payment = ecommerce.groupby('payment_type')['order_id'].nunique()
group_payment_percentage = (group_payment / ecommerce['order_id'].nunique() * 100).round(2)
group_payment_percentage = pd.DataFrame(group_payment_percentage)
group_payment_percentage.reset_index(inplace=True)

fig, ax = plt.subplots(figsize = (14, 6))
plt.pie(group_payment_percentage['order_id'], labels = group_payment_percentage['payment_type'], autopct='%1.1f%%')
plt.title('Tipe pembayaran yang digunakan pelanggan (%)', fontdict = {'fontsize': 15}, pad = 10)
st.pyplot(fig)