import { app } from "../../scripts/app.js";


function parseAspectRatio(aspectRatio) {
    const match = /^(\d+):(\d+)\s+/.exec(aspectRatio ?? "");
    if (!match) return [1, 1];
    return [Number(match[1]), Number(match[2])];
}


function roundHalfEven(value) {
    const lower = Math.floor(value);
    const fraction = value - lower;
    if (fraction < 0.5) return lower;
    if (fraction > 0.5) return lower + 1;
    return lower % 2 === 0 ? lower : lower + 1;
}


function calculateResolution(aspectRatio, megapixels, multiple) {
    const [wRatio, hRatio] = parseAspectRatio(aspectRatio);
    const totalPixels = Number(megapixels) * 1024 * 1024;
    const step = Number(multiple) || 1;
    if (!Number.isFinite(totalPixels) || totalPixels <= 0 || !Number.isFinite(step) || step <= 0) {
        return "0 x 0 px";
    }
    const scale = Math.sqrt(totalPixels / (wRatio * hRatio));
    const width = roundHalfEven(wRatio * scale / step) * step;
    const height = roundHalfEven(hRatio * scale / step) * step;
    return `${width} x ${height} px`;
}


function addResolutionDisplay(node) {
    const aspectRatio = node.widgets?.find((widget) => widget.name === "aspect_ratio");
    const megapixels = node.widgets?.find((widget) => widget.name === "megapixels");
    const multiple = node.widgets?.find((widget) => widget.name === "multiple");
    if (!aspectRatio || !megapixels || !multiple) return;

    const element = document.createElement("div");
    Object.assign(element.style, {
        alignItems: "center",
        background: "var(--comfy-input-bg, #222)",
        border: "1px solid var(--border-color, #555)",
        borderRadius: "8px",
        boxSizing: "border-box",
        color: "var(--input-text, #ddd)",
        display: "flex",
        fontSize: "16px",
        fontWeight: "600",
        height: "100%",
        justifyContent: "center",
        width: "100%",
    });

    const update = () => {
        element.textContent = calculateResolution(aspectRatio.value, megapixels.value, multiple.value);
    };

    for (const widget of [aspectRatio, megapixels, multiple]) {
        const callback = widget.callback;
        widget.callback = function () {
            const result = callback?.apply(this, arguments);
            update();
            return result;
        };
    }

    node.addDOMWidget("calculated_resolution", "resolution-display", element, {
        getMinHeight: () => 44,
        getMaxHeight: () => 44,
        hideOnZoom: false,
        serialize: false,
    });
    node.customResolutionSelectorUpdate = update;
    update();

    const size = node.computeSize();
    node.setSize([Math.max(node.size[0], size[0], 260), Math.max(node.size[1], size[1])]);
}


app.registerExtension({
    name: "ComfyUI.CustomResolutionSelector",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "CustomResolutionSelector") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            const result = onNodeCreated?.apply(this, arguments);
            addResolutionDisplay(this);
            return result;
        };

        const onConfigure = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function () {
            const result = onConfigure?.apply(this, arguments);
            queueMicrotask(() => this.customResolutionSelectorUpdate?.());
            return result;
        };
    },
});
