# Markdown
Markdown 是目前非常普遍用來撰寫文檔的語言，一開始的目標就是使用「易讀易寫的純文字格式編寫文件」，此初衷讓使用者可以專注在文字的本身，而不需要透過其它工具來切換格式。以 Word 撰寫文檔來說，就必須透過上方的工具列來切換標題、列表、粗體、斜體等等；而 Markdown 並沒有這樣的工具列，完全都是使用標示符號來完成這些需求。
常見應用
大部分情況下 Markdown 是用來撰寫程式語言相關的文檔，因為純文字的特性與程式碼一致，且可搭配標示符號來改變呈現格式，像是在 Github 的文件中使用 readme.md 的 Markdown 格式，則會預設作為該儲存庫的介紹。

## 學習 Markdown
基本概念：Markdown 可以輸出成 HTML 的格式，所以各種標示也會對應 HTML 的標籤，就顯示的結構上可區分為兩大類：區塊、行內。

區塊：此類別會讓內容獨立形成一個區塊，區塊內的 全部文字都是套用同樣的格式，標題、引用、清單都是屬於此類型，而區塊可以疊加使用，如引用內可以包含標題。
行內：套用此類別的內容可插入於區塊內，如：強調文字、斜體字、文字連結等等，要特別注意插入圖片也是屬於此類別（與 HTML 特性相符合）。

每個 Markdown 環境所能接受的語法都略有不同，像是部分工具、環境雖然接受使用 Markdown 撰寫，但標題上只接受三個以下的層級（正確為六個層級），所以實際上還是需以運行的環境為主，而本篇介紹的則是介紹通用的使用方式。

區塊元素
此類別會讓內容獨立形成一個區塊，區塊內的 全部文字都是套用同樣的格式，標題、引用、清單都是屬於此類型，而區塊可以疊加使用，如引用內可以包含標題。

標題
總共分為六個層級，依據 HTML 的結構會轉為 <h1> ~ <h6>，形式上是在文字前方補上不同數量的 #，# 數量越少層級越高，反之則是越低，以下方結構來說 # 標題 1 是層級最高，且視覺上最大的標題。

# 標題 1
## 標題 2
### 標題 3
#### 標題 4
##### 標題 5
###### 標題 6

文字段落
當沒有加上任何標示符號時，該區塊的文字就是文字段落區塊，而段落與段落之間會保留一行空白空間，在接下一段的內容。

## 這是標題
這是一段文字段落

這是第二行的文字段落，還是要勉強自己，笑起來處子般通紅；看人突然好想你，顯露所有鋒芒堅

引用
引用的寫法與樣式都類似於 Email 中的回文原文，只要在文章前面補上 > 的符號即可。

> 這裡是一段引用文字

清單
清單分為一般列表及包含數字符號的列表，兩種都包含多個層級，只要加上一個縮排或兩個空格就可以新增一個層級。

一般列表的使用彈性較高，-、+、* 等符號後方加上一個空白後都可以轉為列表，要表示下一個層級可多一個縮排或是兩個空白即可。

- 這是清單
+ 這也是清單
* 這同樣是清單
	- 清單子項目

包含數字符號的列表則是使用 數字 + .作為開頭，列表中的第一個數字是數字列表的起始序號，而後方的數字不需要按照順序，如：1. 2. 2. 結果依然會是 1. 2. 3.；另外縮排的規則與一般列表相同。

1. 數字型清單
2. 第二個數字清單
2. 數字清單不需要連續數字
	3. 數字清單子項目
    後方的數字不需要按照順序。

2. 數字清單從 2 開始
3. 第 3

如果段落文字需要以數字 + . 作為開頭，可以改為 數字 + 反斜線 + .，範例如下。

2019\. 避免 `數字.` 轉為數字型清單的方法

區塊程式碼
作為許多開發者撰寫文本的工具，插入程式碼片段也是合情合理的。Markdown 中會使用三個連續的反引號（`）開頭及結尾做為區塊的程式碼，並且可以在首行的位置補上該段程式碼的語言類別，藉此輸出具有 Highlight 的程式碼。

三個連續的反引號（`）用在開頭結尾，即可作為區塊程式碼。

for (let i = 0; i < 10; i++) {
  setTimeout(function () {
    console.log('這執行第' + i + '次');
  }, 0);
}

分隔線
分隔線，可以使用三個連續符號表示（-、*，部分環境亦可使用 _）

---
***
___

表格
雖然 Markdown 有提供表格的符號，但實際運用上並不是很方便，如果環境許可我大多會直接使用 HTML 的表格標籤替代 Markdown 的表格。Markdown 的表個就像是使用符號 “畫” 一個表格，實際撰寫時對其很麻煩。

下圖為表格的範例。

| thead 1 | thrad 2 | thread 3 |
|---------|---------|----------|
| td      | td      | td       |

行內元素
套用此類別的內容可插入於區塊內，如：強調文字、斜體字、文字連結等等，要特別注意插入圖片也是屬於此類別（與 HTML 特性相符合）。

斜體
斜體字與強調文字使用上是很接近的，可以使用 * 或 _ 符號套用在文字的前後方，即可將文字改為斜體字；而將 * 或 _ 使用連續兩個加在文字的前後方則會是強調文字。

以下為斜體文字的範例，另外在 * 或 _ 的前後補上空白會維持原本的符號，就不會套用斜體效果。

還是要*勉強自己*，笑起來處子般通紅；看人_突然好想你_，顯露所有鋒芒堅持方向，顯露所有鋒芒

強調
以下為強調文字的範例，使用兩個 * 或 _套用在文字的前後方 。** 或 __ 的前後補上空白會維持原本的符號，一樣不會套用強調效果。

還是要**勉強自己**，笑起來處子般通紅；看人__突然好想你__，顯露所有鋒芒堅持方向，顯露所

行內程式碼
與區塊程式碼一樣使用反引號，在此改為單一個反引號加在文字的前後方即可。

還是要勉強自己，笑起來處子般通紅；看人 `<strong>` 突然好想你 `</strong>`，顯露所有鋒芒堅持方向，顯露所有鋒芒堅持方向，在我活的地方為什麼你，我嘆了嘆氣 `var a = 0`。

連結
連結的結構略有不同，會分為前後兩個片段符號：

前者為 [ ]：中括號內需要補上連結的顯示文字。
後者為 ( )：小括號內補上的是連結路徑。
以下為連結範例：Google

[Google](https://www.google.com.tw/)

圖片
圖片要特別注意是屬於行內元素，因此圖片也可以放在文字段落之中（與 HTML 中的 img 標籤邏輯一致），不過大多情況下會將圖片作為獨立區塊使用。

圖片也與連結結構接近，只不過前方多了 !。

![ ]：與連結結構接近，但前方緊貼著 ! 符號。中括號的內容也並非必填，其文字內容通常作為 hover 後的提示文字或作為 SEO 增強使用。
( )：圖片連結位置。
![unsplash 圖片](https://images.unsplash.com/photo-1573900941478-7cc800f708f3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80)
實際運作範例：圖片

參考文章：

https://markdown.tw