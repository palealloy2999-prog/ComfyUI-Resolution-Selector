# ComfyUI Resolution Selector

This custom node is based on ComfyUI's standard `Resolution Selector`, with a curated aspect-ratio list and a live preview of the calculated resolution.

## English

### Aspect ratios

- 1:1 square
- 3:4 portrait
- 5:8 portrait
- 9:16 portrait
- 9:21 portrait
- 4:3 landscape
- 3:2 landscape
- 16:9 landscape
- 21:9 landscape

`aspect_ratio`, `megapixels`, and `multiple` determine the `width` and `height` outputs. The result panel on the node updates immediately when one of these values changes.

`megapixels` offers 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.8, and 3.0. Its default is 0.8. `multiple` offers 8, 16, 32, and 64, with 16 as the default.

### Installation

```bash
git clone https://github.com/your-user/ComfyUI-Resolution-Selector.git custom_nodes/ComfyUI-Resolution-Selector
```

Then restart ComfyUI and reload the browser. The node is available as `Resolution Selector (Custom)` in the `utilities` category.

---

## 日本語

### アスペクト比

- 1:1 square
- 3:4 portrait
- 5:8 portrait
- 9:16 portrait
- 9:21 portrait
- 4:3 landscape
- 3:2 landscape
- 16:9 landscape
- 21:9 landscape

`aspect_ratio`、`megapixels`、`multiple` の値によって `width` と `height` が決まります。ノード上の結果表示は、いずれかの値が変わるとすぐに更新されます。

`megapixels` は 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.8, 3.0 を選択できます。デフォルトは 0.8 です。`multiple` は 8, 16, 32, 64 を選択でき、デフォルトは 16 です。

### インストール方法

```bash
git clone https://github.com/your-user/ComfyUI-Resolution-Selector.git custom_nodes/ComfyUI-Resolution-Selector
```

その後、ComfyUI を再起動してブラウザを再読込してください。このノードは `utilities` カテゴリに `Resolution Selector (Custom)` として追加されます。
