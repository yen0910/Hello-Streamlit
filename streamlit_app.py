# 第一行指令：%%writefile 會將此儲存格內容直接寫入成一個名為 streamlit_app.py 的檔案
# 第二行用途：這是在雲端開發環境中產生可執行腳本的標準做法
import streamlit as st

# ==========================================
# 1. 開發者變數定義區 (請在此修改個人學籍資訊)
# ==========================================
dev_name = "裝正彥"                # 學生姓名
dev_class = "高二 12 班"            # 班級
dev_id = "311325"               # 學號
dev_group = "自然組"               # 組別 (自然組 或 自學組)
dev_skills = ["Python", "GitHub", "Streamlit", "Colab"]

# ==========================================
# 2. 網頁配置與側邊欄 (Layout Layer)
# ==========================================
st.set_page_config(page_title=f"{dev_name} 的作品展示", page_icon="🔬")

with st.sidebar:
    st.header("👨‍💻 開發者檔案")
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=100)
    st.markdown(f"**姓名：** {dev_name}\n**班級：** {dev_class}\n**學號：** {dev_id}\n**組別：** {dev_group}")
    st.divider()
    st.subheader("🛠 技術工具")
    for skill in dev_skills:
        st.write(f"- {skill}")
    st.caption("本專案透過 GitHub CI/CD 自動化部署")

# ==========================================
# 3. 主頁面：問候與互動特效 (Logic Layer)
# ==========================================
st.title("✨ 雲端 Python 互動展示")
visitor = st.text_input("老師/委員您好，請輸入您的姓名：", placeholder="例如：林阿宏委員 或 王小明老師")

if visitor:
    # 關鍵字偵測：包含「委員」或「老師」時觸發氣球特效
    if "委員" in visitor or "老師" in visitor:
        st.balloons() # 觸發氣球噴發特效
        st.success(f"### 歡迎 {visitor} 蒞臨指導！ 👋")
    else:
        st.write(f"### Hello, {visitor}! 😊")
        st.info("提示：輸入包含「委員」或「老師」可觸發隱藏特效！")
else:
    st.info("💡 請在上方輸入框輸入姓名，啟動 Python 的互動邏輯！")
