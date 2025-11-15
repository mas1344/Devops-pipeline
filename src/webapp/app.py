import streamlit as st
import pandas as pd

from webapp.constants import UPDATE_FREQ_SEC
from webapp.crypto_api import get_crypto_data
from webapp.utils import format_number_with_suffix

st.set_page_config(page_title="Crypto Prices", layout="centered")


@st.fragment(run_every=UPDATE_FREQ_SEC)
def display_crypto_price():
    st.write("# Cryptocurrency Prices Dashboard")

    coins = get_crypto_data()  
    if not coins:
        st.error("No data from API.")
        return

    cols = st.columns(len(coins))
    for col, coin in zip(cols, coins):
        price = coin.get("price", 0) or 0
        change_24h = coin.get("percent_change_24h", 0) or 0
        symbol = coin.get("symbol", "")

        with col:
            st.metric(
                label=symbol or "CRYPTO",
                value=format_number_with_suffix(price),
                delta=f"{change_24h:.2f}%",
            )

    st.subheader("Latest quotes (table)")

    df = pd.DataFrame(coins)

    desired_order = [
        "symbol",
        "base_currency",
        "price",
        "percent_change_24h",
        "market_cap",
        "volume_24h",
        "last_updated",
    ]
    cols_in_df = [c for c in desired_order if c in df.columns]
    df = df[cols_in_df]

    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    display_crypto_price()
