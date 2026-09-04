# ComfyUI Resolution Selector

A custom ComfyUI node inspired by the built-in `Resolution Selector`, with a curated set of aspect ratios and a live calculated-resolution preview.

<img width="479" height="424" alt="Resolution Selector preview" src="https://github.com/user-attachments/assets/f93b9000-3475-4d47-8b72-e7644cfaf8ef" />

## Features

- Custom aspect-ratio presets for square, portrait, and landscape outputs
- Quick megapixel target selection
- Adjustable rounding multiple for output size normalization
- Real-time preview of the calculated resolution inside the node UI

## Supported aspect ratios

- 1:1 square
- 3:4 portrait
- 5:8 portrait
- 9:16 portrait
- 9:21 portrait
- 4:3 landscape
- 3:2 landscape
- 16:9 landscape
- 21:9 landscape

## Controls

- `aspect_ratio`: selects the target aspect ratio
- `megapixels`: chooses the target total megapixel count
- `multiple`: rounds the final width and height to the nearest selected multiple

Available `megapixels` values: 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.8, and 3.0.

Available `multiple` values: 8, 16, 32, and 64.

## Installation

```bash
cd custom_nodes
git clone https://github.com/palealloy2999-prog/ComfyUI-Resolution-Selector.git
```

Then restart ComfyUI and reload the browser. The node will appear as `Resolution Selector (Custom)` under the `utilities` category.

---

## 日本語

ComfyUI の標準ノード `Resolution Selector` をベースにしたカスタムノードです。用途に合わせたアスペクト比の候補と、計算結果のプレビュー表示を追加しています。

### 対応アスペクト比

- 1:1 square
- 3:4 portrait
- 5:8 portrait
- 9:16 portrait
- 9:21 portrait
- 4:3 landscape
- 3:2 landscape
- 16:9 landscape
- 21:9 landscape

### 主要な設定項目

- `aspect_ratio`: 出力したい縦横比を選択
- `megapixels`: 目標の総メガピクセル数を選択
- `multiple`: 最終的な幅と高さを指定した倍数で丸める

`megapixels` の候補: 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.8, 3.0

`multiple` の候補: 8, 16, 32, 64

### インストール方法

```bash
cd custom_nodes
git clone https://github.com/palealloy2999-prog/ComfyUI-Resolution-Selector.git
```

その後、ComfyUI を再起動してブラウザを再読込すると、`utilities` カテゴリに `Resolution Selector (Custom)` が表示されます。
