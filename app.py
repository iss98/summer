import streamlit as st
import openai

#openai api key
openai.api_key = st.secrets["api_key"]

#페이지 레이아웃 설정
st.set_page_config(layout="wide")

#페이지의 메인 이름
st.title("0814 여름학교 ChatGPT API 실습")

# #가로 줄
st.divider()

st.header("수업이 끝났습니다. 질문해주세요")

# #헤더 
st.header("예시 자료")

# #텍스트 출력하기
text = '''
특정 온도 이하가 되면 전기저항이 0이 되는 물질을 초전도체라고 한다. 초전도체는 자기장주1의 특성에 따라 자기장이 들어가지 못하는 제1종 초전도체와 자기장이 침투하지만 초전도성을 유지하는 제2종 초전도체로 구분된다. 제1종 초전도체는 나이오븀(Nb)주2, 바나듐(V)주3 등 금속 원소이며, 제2종 초전도체는 합금, 화합물 등이 해당된다.

특히 제2종 초전도체는 내부에 자기장이 들어가면서도 무저항을 유지하는 성질을 가지고 있다. 초기에 발견된 제2종 초전도체는 NbTi, Nb₃Sn 등 합금이 있다. 이는 액체 헬륨으로 냉각해야 할 정도의 낮은 온도(영하 260도 이하)에서 초전도성을 나타내므로 ‘저온 초전도체’라고 부른다.

1987년부터 발견되기 시작한 세라믹 계열 초전도체 역시 제2종 초전도체인데, 합금계보다는 수십도 높은 온도에서 초전도성을 나타내므로 ‘고온 초전도체’라고 부른다.
'''
st.write(text)
# # st.write("~~~") 의 형태로도 출력 가능

# #링크 넣기
st.markdown("[위키피디아 링크](https://ko.wikipedia.org/wiki/%EC%84%B8%EC%A2%85)")

# #학생들이 텍스트 입력하는 곳 만들기
# #조사한 자료를 research에 저장
research = st.text_input("조사해온 자료를 입력해주세요 : ")

st.write(research)

st.divider()

# #ChatGPT API 활용하기 response를 불러오는 함수 만들기
@st.cache_data #반복 수행을 막아줌
def gptapi(persona, user):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content" : persona},
        {"role": "user", "content": user}
    ],
    max_tokens = 200,
    temperature = 1
    )
    return response["choices"][0]["message"]["content"]

# #prompt 설정하기
persona_prompt1 = '''
너는 물리선생님이야.
학생들이 조사해온 자료를 2문장으로 요약해줘. 
'''

persona_prompt2 = '''
너는 물리선생님이야. 
학생들이 조사해온 자료의 요약본을 보고, 학생들의 이해를 확인할 수 있는 문제를 2개 만들어줘
'''

# #클릭해야 실행되도록 버튼 만들기
if st.button("요약본 보고 질문받기"): 
    #복잡한 단계는 나누어 진행하기
    step1 = gptapi(persona_prompt1, research)
    st.write(step1)

    step2 = gptapi(persona_prompt2, step1)
    st.write(step2)