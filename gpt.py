# pip install openai
import openai  # for generating embeddings
import os  # for environment variables

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4o"

def chatGpt(query):

    system = '''
## 일반 지시 사항 ##
질문인지 지시인지를 구분하고
질문이면 '질문', 지시이면 '지시'라고 답변해줘.
지시인 경우에는 지시내용을 실행하는 AutoCAD LISP 코드를 생성해줘.
 
LISP 코드 생성시 함수로 만들지 말고 바로 실행되는 LISP 코드로 생성해
LISP 코드 생성시 주석은 빼고 생성해

## 참고 LISP 코드 ##
그리기 지시인 경우에 위치와 크기는 아래 코드를 참고해서, 사용자의 추가 입력을 받지 않도록 생성해.
```
  ;; 현재 뷰의 중심과 크기를 가져옵니다.
  (setq viewCenter (getvar "VIEWCTR"))
  (setq viewSize (getvar "VIEWSIZE"))
 
  ;; 사각형의 너비와 높이를 계산합니다.
  ;; viewSize는 너비와 높이를 갖는 리스트가 아니라 하나의 실수 값이므로 이를 절반으로 나눕니다.
  (setq halfWidth (/ viewSize 4.0))
  (setq halfHeight (/ viewSize 4.0))
 
  ;; 중심을 기준으로 50% 크기의 사각형을 설정합니다.
  (setq pt1 (list (- (car viewCenter) halfWidth) (- (cadr viewCenter) halfHeight)))
  (setq pt2 (list (+ (car viewCenter) halfWidth) (+ (cadr viewCenter) halfHeight)))
  (setq pt3 (list (car pt1) (cadr pt2)))
  (setq pt4 (list (car pt2) (cadr pt1)))
```
    '''

    res = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': system},
            {'role': 'user', 'content': query},
        ],
        model=GPT_MODEL,
        temperature=0,
    )

    return res.choices[0].message.content