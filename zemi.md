# Difference between Bastankhah et al. (2014) and Pywake's BP model

## C(x)のmath domain error
Bastankhah et al(2014)の式(14)は　$C(x) = 1 - \sqrt{1 - C_T/8(\sigma/d_0)^2}$

場合によって　 $1 - C_T/8(\sigma/d_0)^2 < 0$ 　の可能性がある。

解決策の一つとしては、モデルの適用範囲を　$x>...$　にする方法がある。BPモデルはそもそもnear wakeでは成り立たないため、一定の距離を開けて計算しても問題ない。

もう一つは　$1 - C_T/8(\sigma/d_0)^2$　の部分を　$1 - min(1,C_T/8(\sigma/d_0)^2)$　にして、強制的に非負にする方法です。その方法もnear wakeでは不自然は挙動が出るが、前述のとおり、far wakeだけを重視するため問題ない。

## 速度欠損とCTの関係
Banstankhah et al(2014)では一次元運動量理論　$a = \frac{1}{2}(1 - \sqrt{1 - C_T})$　に基づいた式を提案した。この式はpywakeで「ct2a_mom1d」と呼ばれる。

ただ、pywakeのBPモデルはデフォルトでMadsenらが提案した式を使用している。この式は　$a = 0.2460C_T + 0.0586C_T^2 + 0.0883C_T^3$　、pywakeでは「ct2a_madsen」と呼ばれる。
