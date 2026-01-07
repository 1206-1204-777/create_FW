# [Variableクラス/__mul__メソッド,__add__メソッド] 単体テスト仕様書

## 1. テスト目的

`Variable` クラスのインスタンス同士で、加算と乗算が行え正しい値を返すことを確認する。

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| `Variable` | `__mul__` | mul関数のオーバーロードを行い加算がが行えるか確認 |
| `Variable` | `__add__` | add関数のオーバーロードを行い乗算が行えるか確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | test_add_forward | `x0 = Variable(np.array(3.0)), x1 = Variable(np.array(2.0))` | `y.data == 5.0`  | `assertEqual` |
| N-02 | test_mul_forward | `x0 = Variable(np.array(2.0)), x1 = Variable(np.array(2.0))` | `y.data == 4.0`  | `assertEqual` |
| N-03 | test_add_backward | `x0 = Variable(np.array(3.0)), x1 = Variable(np.array(2.0))` | `x0.grad == 1.0`. `x1.grad == 1.0` | `assertEqual` |
| N-04 | test_mul_backward |  `x0 = Variable(np.array(3.0)), x1 = Variable(np.array(2.0))` | `x0.grad == 2.0`. `x1.grad == 3.0` | `assertEqual` |

### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | test_add_error | `x0 = Variable(np.array(3.0))`と`a` を加算する | `AttributeError` が返されること |  |
| E-02 | test_mul_error | `x0 = Variable(np.array(3.0))`と`a` を乗算する | `AttributeError` が返されること |  |

## 4. 数値微分による検証 (Gradient Check)
なし
## 5. テストコード実装上の注意
なし