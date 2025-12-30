# [Helper Functions] 設計仕様書

## 1. as_array

* **役割**: スカラー値を `ndarray` に変換し、NumPyの仕様による型エラーを回避する。

## 2. numerical_diff

* **役割**: 中心差分近似を用いて数値微分を計算する。
* **手順**:
1.  と  （）を計算。
2. それぞれを関数 `f` に渡し、結果の差から微分値を求めて返す。



## 3. Factory Functions (square, exp, add)

* **役割**: 各演算クラス（Square, Exp, Add）をインスタンス化して実行するラッパー関数。
