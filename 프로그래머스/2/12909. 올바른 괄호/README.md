# [level 2] 올바른 괄호 - 12909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909) 

### 성능 요약

메모리: 10.2 MB, 시간: 5.71 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 69.5<br/>효율성: 30.5<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 06월 23일 23:07:45

### 문제 설명

<p>괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어</p>

<ul>
<li>"()()" 또는 "(())()" 는 올바른 괄호입니다.</li>
<li>")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.</li>
</ul>

<p>'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 100,000 이하의 자연수</li>
<li>문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"()()"</td>
<td>true</td>
</tr>
<tr>
<td>"(())()"</td>
<td>true</td>
</tr>
<tr>
<td>")()("</td>
<td>false</td>
</tr>
<tr>
<td>"(()("</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1,2,3,4<br>
문제의 예시와 같습니다.</p>

# ✏️ 풀이 방식

올바른 괄호 문제는 스택을 활용하는 문제이고, 왼쪽 괄호가 나오면 스택에 추가하고 오른쪽 괄호가 나오면 스택에서 pop을 해주는 식으로 풀면 된다.

1. 오른쪽 괄호부터 시작하는 경우 (False)
2. 순회가 다 끝났는데 스택에 왼쪽 괄호가 남아있는경우 (False)
3. 모든 괄호가 짝이 다 맞아서 마지막에 스택이 비게 된 경우 (True)
<br/>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
> <br/>
> 참고한 블로그: https://msiqoc.tistory.com/27
