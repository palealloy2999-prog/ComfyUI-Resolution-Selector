import math
from enum import Enum

from typing_extensions import override

from comfy_api.latest import ComfyExtension, io


class AspectRatio(str, Enum):
    SQUARE = "1:1 square"
    PORTRAIT_3_4 = "3:4 portrait"
    PORTRAIT_5_8 = "5:8 portrait"
    PORTRAIT_9_16 = "9:16 portrait"
    PORTRAIT_9_21 = "9:21 portrait"
    LANDSCAPE_4_3 = "4:3 landscape"
    LANDSCAPE_3_2 = "3:2 landscape"
    LANDSCAPE_16_9 = "16:9 landscape"
    LANDSCAPE_21_9 = "21:9 landscape"


ASPECT_RATIOS: dict[str, tuple[int, int]] = {
    AspectRatio.SQUARE: (1, 1),
    AspectRatio.PORTRAIT_3_4: (3, 4),
    AspectRatio.PORTRAIT_5_8: (5, 8),
    AspectRatio.PORTRAIT_9_16: (9, 16),
    AspectRatio.PORTRAIT_9_21: (9, 21),
    AspectRatio.LANDSCAPE_4_3: (4, 3),
    AspectRatio.LANDSCAPE_3_2: (3, 2),
    AspectRatio.LANDSCAPE_16_9: (16, 9),
    AspectRatio.LANDSCAPE_21_9: (21, 9),
}

MEGAPIXELS = ["0.2", "0.3", "0.4", "0.5", "0.6", "0.8", "1.0", "1.2", "1.5", "1.8", "2.0", "2.2", "2.5", "2.8", "3.0"]
MULTIPLES = [8, 16, 32, 64]


def resolve_aspect_ratio(aspect_ratio: str | AspectRatio) -> tuple[int, int]:
    ratio_key = AspectRatio(aspect_ratio) if not isinstance(aspect_ratio, AspectRatio) else aspect_ratio
    return ASPECT_RATIOS.get(ratio_key, ASPECT_RATIOS[AspectRatio.SQUARE])


class CustomResolutionSelector(io.ComfyNode):
    """Calculate width and height using a curated set of aspect ratios."""

    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="CustomResolutionSelector",
            display_name="Resolution Selector (Custom)",
            category="utilities",
            description="Calculate width and height from a custom aspect ratio and megapixel target.",
            inputs=[
                io.Combo.Input(
                    "aspect_ratio",
                    options=AspectRatio,
                    default=AspectRatio.SQUARE,
                    tooltip="The aspect ratio for the output dimensions.",
                ),
                io.Combo.Input(
                    "megapixels",
                    options=MEGAPIXELS,
                    default="0.8",
                    tooltip="Target total megapixels.",
                ),
                io.Combo.Input(
                    id="multiple",
                    options=MULTIPLES,
                    default=16,
                    tooltip="Round each output dimension to the nearest selected multiple.",
                ),
            ],
            outputs=[
                io.Int.Output("width", tooltip="Calculated width in pixels."),
                io.Int.Output("height", tooltip="Calculated height in pixels."),
            ],
        )

    @classmethod
    def execute(cls, aspect_ratio: str, megapixels: str, multiple: int) -> io.NodeOutput:
        w_ratio, h_ratio = resolve_aspect_ratio(aspect_ratio)
        total_pixels = float(megapixels) * 1024 * 1024
        scale = math.sqrt(total_pixels / (w_ratio * h_ratio))
        width = round(w_ratio * scale / multiple) * multiple
        height = round(h_ratio * scale / multiple) * multiple
        return io.NodeOutput(width, height)


class CustomResolutionSelectorExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [CustomResolutionSelector]


async def comfy_entrypoint() -> CustomResolutionSelectorExtension:
    return CustomResolutionSelectorExtension()


WEB_DIRECTORY = "./web"

__all__ = ["WEB_DIRECTORY", "comfy_entrypoint"]
