import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="엑셀 업로드 뷰어",
    page_icon="📊",
    layout="wide"
)

st.title("📊 엑셀 데이터 업로드 및 조회")

uploaded_file = st.file_uploader(
    "엑셀 파일을 업로드하세요",
    type=["xlsx"]
)

if uploaded_file is not None:
    try:
        # 엑셀 파일 읽기
        excel_file = pd.ExcelFile(uploaded_file)

        # 시트 선택
        sheet_name = st.selectbox(
            "조회할 시트를 선택하세요",
            excel_file.sheet_names
        )

        # 선택한 시트 데이터프레임으로 읽기
        df = pd.read_excel(
            uploaded_file,
            sheet_name=sheet_name
        )

        st.success("엑셀 파일 업로드 완료")

        # 기본 정보 출력
        st.write(f"행 개수: {df.shape[0]}개")
        st.write(f"열 개수: {df.shape[1]}개")

        # 데이터 화면에 표시
        st.subheader("업로드한 엑셀 데이터")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error("엑셀 파일을 읽는 중 오류가 발생했습니다.")
        st.exception(e)

else:
    st.info("엑셀 파일을 업로드하면 데이터가 화면에 표시됩니다.")