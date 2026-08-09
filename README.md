# ComfyUI Resolution Selector

ComfyUI's standard `Resolution Selector`, with a custom set of aspect ratios and a live calculated-resolution display.
<img width="479" height="424" alt="image" src="https://github.com/user-attachments/assets/f93b9000-3475-4d47-8b72-e7644cfaf8ef" />


## Aspect ratios

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

`megapixels` offers 0.4 through 1.0 in 0.1 steps, followed by 1.2, 1.5, 1.8, and 2.0. Its default is 0.8. `multiple` offers 8, 16, 32, and 64, with 16 as the default.

Restart ComfyUI and reload the browser after installation. The node is available as `Resolution Selector (Custom)` in the `utilities` category.


