import streamlit as st
from datetime import datetime
import pandas as pd

# 애플리케이션 제목
st.title("학생 결석 사유 입력")

# 학생 성명 입력
student_name = st.text_input("학생 성명을 입력하세요:")

# 학번 입력
student_id = st.text_input("학번을 입력하세요:")

# 결석 종류 선택
absence_type = st.selectbox(
    "결석 종류를 선택하세요:",
    ["질병결석", "인정결석", "기타결석"]
)

# 결석 날짜 선택
absence_date = st.date_input(
    "결석 날짜를 선택하세요:",
    value=datetime.today()
)

# 결석 사유 입력
reason = st.text_area("결석 사유를 서술하세요:")

# 제출 버튼
if st.button("제출"):
    if not student_name.strip() or not student_id.strip() or not reason.strip():
        st.error("학생 성명, 학번, 결석 사유를 모두 입력해 주세요.")
    else:
        # 결석 정보를 DataFrame으로 변환
        data = {
            "학생 성명": [student_name],
            "학번": [student_id],
            "결석 종류": [absence_type],
            "결석 날짜": [absence_date],
            "결석 사유": [reason]
        }
        df = pd.DataFrame(data)

        # CSV 파일로 저장
        csv_file = 'absence_data.csv'
        if st.button("저장 및 파일 다운로드"):
            df.to_csv(csv_file, index=False)
            st.success(f"결석 사유가 성공적으로 제출되었습니다. 파일이 저장되었습니다.")
            st.download_button(
                label="CSV 파일 다운로드",
                data=df.to_csv(index=False),
                file_name=csv_file,
                mime='text/csv'
            )

        # 제출된 정보 출력
        st.subheader("제출된 정보")
        st.write(df)

# 페이지 끝에 메타데이터 및 추가 정보 표시
st.sidebar.info("이 앱은 학생의 결석 사유를 수집하고 저장하는 간단한 도구입니다.")

