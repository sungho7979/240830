import streamlit as st
import pandas as pd
from datetime import datetime

# 애플리케이션 제목
st.title("학생 정보 및 도서 조사")

# 학생 정보 입력
st.header("학생 정보")
student_id = st.text_input("학번을 입력하세요:")
student_name = st.text_input("학생 성명을 입력하세요:")
career_aspiration = st.text_input("진로 희망을 입력하세요:")

# 도서 정보 입력
st.header("도서 정보")
book_title = st.text_input("도서명을 입력하세요:")
book_author = st.text_input("저자를 입력하세요:")
book_publisher = st.text_input("출판사를 입력하세요:")

# 제출 버튼
if st.button("제출"):
    # 데이터 검증
    if not (student_id.strip() and student_name.strip() and career_aspiration.strip() and
            book_title.strip() and book_author.strip() and book_publisher.strip()):
        st.error("모든 필드를 입력해 주세요.")
    else:
        # 입력된 정보를 DataFrame으로 변환
        data = {
            "학번": [student_id],
            "학생 성명": [student_name],
            "진로 희망": [career_aspiration],
            "도서명": [book_title],
            "저자": [book_author],
            "출판사": [book_publisher]
        }
        df = pd.DataFrame(data)

        # CSV 파일로 저장
        csv_file = 'student_and_book_info.csv'
        df.to_csv(csv_file, index=False)

        # 성공 메시지
        st.success("정보가 성공적으로 제출되었습니다.")
        
        # 제출된 정보 출력
        st.subheader("제출된 정보")
        st.write(df)

        # CSV 파일 다운로드 버튼
        st.download_button(
            label="CSV 파일 다운로드",
            data=df.to_csv(index=False),
            file_name=csv_file,
            mime='text/csv'
        )

# 페이지 끝에 메타데이터 및 추가 정보 표시
st.sidebar.info("이 앱은 학생 정보와 도서 정보를 수집하고 저장하는 도구입니다.")
