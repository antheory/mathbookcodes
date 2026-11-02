# Readme

『中谷彰宏，"機械工学のための数理モデリングと現象解析入門"（2026），コロナ社』に関連するPythonコード含んでいます．

## 書籍情報 / Book Information
本書籍の公式サポートコードを公開しているリポジトリです。

* **書籍名**: 機械工学のための数理モデリングと現象解析入門
* **著者**: 中谷 彰宏（大阪大学教授）
* **出版社**: コロナ社
* **発行年**: 2026年
* **書籍詳細（出版社URL）**: [`https://coronasha.co.jp/np/isbn/9784339061376/`](https://www.coronasha.co.jp/np/isbn/9784339061376/)
* **著者によるサポートページ**：[`https://www-md-mech.eng.osaka-u.ac.jp/~nakatani/Lectures/Math_Model_Analysis/`](https://www-md-mech.eng.osaka-u.ac.jp/~nakatani/Lectures/Math_Model_Analysis/)
  
## 要約

以下に各フォルダーの説明を記します．

- 書籍掲載のプログラムは，[`src/`](src/)にあります．初版第1刷p.191のプログラム6-22（FDM：メインルーチン）
に2次元配列の添字の誤記があります．電子版の[`プログラム6-22`](src/program6-22.py)は修正済みです．
- 書籍に掲載した各プログラムを組み合わせて，実行可能なPythonコードを作成するための例として[`シェルスクリプト`](script/)を置いています（展開したプログラムの相対パスは適宜書き換えて活用してください．）
- 書籍に記した[`減衰振り子の運動（damped_pendulum/)`](damped_pendulum/)，
[`熱伝導方程式の数値解（heateq/）`](heateq/)，
[`波動方程式の数値解（waveeq/）`](waveeq/)，
[`ラプラス方程式の数値解（laplaceeq/）`](laplaceeq/)に上記のシェルスクリプトで作成したコードを置いています．なお，ラプラス方程式の数値解については，(x,y,u)のグラフ出力部分を追加したコードと，差分パッチを[`配下にあるフォルダー（laplaceeq/3dplot/）`](laplaceeq/3dplot/)に置いています．

## 動作環境と実行方法 / Requirements & Usage

### 必要環境

* **Python**: 3.10 以上（推奨）
* **外部ライブラリ**（使用するサンプルに応じて必要）:
  * `numpy`（数値計算用）
  * `matplotlib`（グラフ描画・シミュレーション可視化用）
  * `scipy`（科学技術計算用）
* **GUIを使用するサンプルの追加要件**:
  * Tkinter（Pythonの `tkinter` モジュール）および、その動作に必要な Tcl/Tk
  * 減衰振り子のサンプルなどで使用します。導入方法と確認方法は下記を参照してください。

### ライブラリのインストールと通常実行

リポジトリをクローンまたはダウンロードし、リポジトリの
ルートディレクトリ（`README.md` があるフォルダー）で実行してください。

```bash
# リポジトリのクローン
git clone https://github.com/antheory/mathbookcodes
cd mathbookcodes

# 使用するPython環境に外部ライブラリをインストール
python -m pip install numpy matplotlib scipy

# ラプラス方程式の差分法（FDM）の実行
python laplaceeq/laplaceeq-fdm.py
```

以下の説明では、Python 3を起動するコマンドを `python` と表記します。
環境に応じて `python3` などに読み替え、インストールと実行には同じPython環境を使用してください。

`laplaceeq/` にある各手法のファイル名は次のとおりです。

| 手法 | ファイル |
| --- | --- |
| 差分法（FDM） | `laplaceeq/laplaceeq-fdm.py` |
| 境界要素法（BEM） | `laplaceeq/laplaceeq-bem.py` |
| 有限要素法（FEM） | `laplaceeq/laplaceeq-fem.py` |
| モンテカルロ法（MC） | `laplaceeq/laplaceeq-mc.py` |

ほかの手法を実行する場合は、実行コマンドのファイル名を上表に従って変更してください。
ファイル名のハイフンと英字の大文字・小文字に注意してください。

### Jupyter Notebookでの実行

Jupyter Notebookを使用する場合は、必要なライブラリを導入したPython環境を
カーネルとして選択してください。Jupyter自体は別途用意する必要があります。

Notebookの作業ディレクトリをリポジトリのルートディレクトリにして、
セル内で次のように実行します。

```python
%run laplaceeq/laplaceeq-fdm.py
```

`%run` はIPython/Jupyterのマジックコマンドです。
ターミナルで実行する場合は、前節の `python` コマンドを使用してください。

### Tkinter（Tcl/Tk）の確認と導入

TkinterはTcl/Tkを利用するPythonの標準GUIインターフェースですが、
Pythonの配布形態やOSによっては含まれておらず、別途導入が必要です。
上記の `python -m pip install numpy matplotlib scipy` では、
TkinterやTcl/Tkは導入されません。

GUIを使用するサンプルを実行する前に、同じPython環境で次を実行してください。

```bash
python -m tkinter
```

確認用のウィンドウが開けば、TkinterとTcl/Tkが利用できます。
`tkinter` または `_tkinter` が見つからない場合は、使用しているPythonの
配布元やOSの案内に従って、Tkinter対応のパッケージやコンポーネントを導入してください。
`pip install tkinter` で導入するものではありません。

また、GUIの表示にはデスクトップなどの画面表示環境が必要です。
リモートサーバーや画面表示のない環境では、Tkinterが導入済みでも
ウィンドウを開けない場合があります。Jupyterから実行する場合も、
カーネルが動作する環境でこれらの条件を満たす必要があります。

詳細は [Python公式ドキュメント：tkinter](https://docs.python.org/ja/3/library/tkinter.html)
を参照してください。

## 免責事項 / Disclaimer
* 本リポジトリで提供しているソースコードやデータ（以下、「本コンテンツ」）は、学習および研究の補助を目的として提供されています。
* 本コンテンツの正確性や完全性、特定の目的への適合性について、著者および出版社は明示的・黙示的を問わず、いかなる保証もいたしません。
* 本コンテンツを利用したこと、または利用できなかったことによって生じた直接的・間接的な損害（データの損失、業務の中断、計算結果の誤りなどを含むがこれらに限定されない）について、著者および出版社は一切の責任を負いません。
* 本コンテンツは、予告なしに変更、削除、または公開を停止することがあります。

## 利用規約とライセンス / License
本リポジトリのソースコードは **MIT License** のもとで公開されています。
学習・研究・業務目的での利用（複製、改変、実行、再配布）は自由ですが、利用の際は著作権表示（LICENSEファイルの同梱）が必要です。詳細は同梱の `LICENSE` ファイルをご確認ください。

