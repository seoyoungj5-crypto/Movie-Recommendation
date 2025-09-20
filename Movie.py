import streamlit as st
import requests
# TMDb API 키 (여기에 본인의 API 키를 입력하세요)
API_KEY = "f4b796c8df8ce5b73aaa006cc62c555d"
BASE_URL = "https://api.themoviedb.org/3"

# 인기 영화 가져오기 함수
def get_popular_movies():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ko-KR&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []

# Streamlit 앱 시작
st.set_page_config(page_title="인기 영화 추천기", layout="wide")

st.title("🎬 최근 인기 영화 추천")

# 영화 리스트 가져오기
movies = get_popular_movies()

if not movies:
    st.error("영화를 불러오는 데 실패했습니다. API 키를 확인하세요.")
else:
    for movie in movies:
        cols = st.columns([1, 3])  # 포스터, 설명

        # 포스터 이미지
        with cols[0]:
            if movie["poster_path"]:
                st.image(f"https://image.tmdb.org/t/p/w200{movie['poster_path']}")
            else:
                st.write("이미지 없음")

        # 영화 정보
        with cols[1]:
            st.subheader(movie["title"])
            st.markdown(f"**개봉일:** {movie.get('release_date', '미정')}")
            st.markdown(f"**평점:** ⭐ {movie['vote_average']} / 10")
            st.write(movie["overview"])
        
        st.markdown("---")