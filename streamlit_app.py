import streamlit as st
import pandas as pd

def generate_matrix():
    # สร้าง Matrix 10x10 (ตัวเลข 00-99)
    matrix = [[f"{i * 10 + j:02}" for j in range(10)] for i in range(10)]
    return matrix

def flatten_matrix(matrix):
    # แปลง Matrix เป็น List
    return [num for row in matrix for num in row]

def filter_069(numbers):
    # เลือกเฉพาะตัวเลขที่มี 0, 6, หรือ 9 อยู่ในตัวเลขนั้น
    return [num for num in numbers if '0' in num or '6' in num or '9' in num]

# สร้าง Matrix ตัวเลข 00-99
matrix = generate_matrix()
all_numbers = flatten_matrix(matrix)

# ส่วนของการเลือกตัวเลขที่ต้องการขีดฆ่า
st.title("ตารางตัวเลข 10x10")
selected_numbers = st.multiselect("เลือกตัวเลขที่ต้องการขีดฆ่า:", all_numbers)

# คำนวณตัวเลขที่เหลือ
remaining_numbers = sorted(set(all_numbers) - set(selected_numbers))

# ส่วนของการเลือก "เลขที่ออกงวดที่แล้ว" จากตัวเลขที่เหลือ
last_draw_numbers = st.multiselect(
    "เลขที่ออกงวดที่แล้ว:", remaining_numbers
)

# แสดง Matrix ที่มีการขีดฆ่าตัวเลขที่ถูกเลือก
st.subheader("Matrix 10x10 พร้อมตัวเลขที่ถูกขีดฆ่า")
matrix_with_strike = [
    [num if num not in selected_numbers else "X" for num in row]
    for row in matrix
]
df_matrix = pd.DataFrame(matrix_with_strike)
st.dataframe(df_matrix)

# แสดงรายการตัวเลขที่เหลือในรูปแบบตาราง
st.subheader("รายการตัวเลขที่เหลือ")
remaining_df = pd.DataFrame(
    [remaining_numbers[i:i + 10] for i in range(0, len(remaining_numbers), 10)]
)
st.dataframe(remaining_df)

# แสดงจำนวนตัวเลขที่เหลือทั้งหมด
st.write(f"จำนวนตัวเลขที่เหลือทั้งหมด: {len(remaining_numbers)}")

# รับค่าจำนวนเงิน/ตัว (บาท) จากผู้ใช้
price_per_number = st.number_input("จำนวนเงิน/ตัว (บาท)", min_value=0.0, value=10.0)

# คำนวณจำนวนเงินทั้งหมด
total_cost = len(remaining_numbers) * price_per_number

# รับค่ารางวัล/บาท จากผู้ใช้
reward_per_baht = st.number_input("รางวัล/บาท", min_value=0.0, value=75.0)

# คำนวณเงินรางวัลที่อาจได้รับ (ต่อเลขที่ถูก)
potential_reward = reward_per_baht * price_per_number

# คำนวณจุด breaking point (จุดเท่าทุน)
breaking_point = max(0, (total_cost // potential_reward) + 1)

# แสดงผลลัพธ์
st.subheader("ผลการคำนวณ")
st.write(f"ต้องใช้เงินทั้งหมด: {total_cost:,.2f} บาท")
st.write(f"ถูกรางวัล (บาท): {potential_reward:,.2f} บาท ต่อการถูก 1 เลข")

# แสดงจำนวนตัวเลขที่ต้องตัดออกเพื่อให้ได้กำไร
st.subheader(f"เหลือตัวเลขอีก {breaking_point} (ตัว) ที่ต้องตัดออก เพื่อให้มีกำไร 1 บาทขึ้นไป")

# ส่วนของการสร้าง "ตาราง 0 6 9"
numbers_069 = filter_069(all_numbers)

st.subheader("ตาราง 0 6 9")
df_069 = pd.DataFrame(
    [numbers_069[i:i + 10] for i in range(0, len(numbers_069), 10)]
)
st.dataframe(df_069)

# แสดงจำนวนตัวเลขในตาราง 0 6 9
st.write(f"จำนวนตัวเลขในตาราง 0 6 9: {len(numbers_069)}")

# คำนวณเงินลงทุนทั้งหมดสำหรับตาราง 0 6 9
investment_069 = len(numbers_069) * price_per_number
st.write(f"ใช้เงินลงทุน (บาท) สำหรับตาราง 0 6 9: {investment_069:,.2f} บาท")
