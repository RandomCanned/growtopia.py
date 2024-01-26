__all__ = (
    "IGNORED_ATTRS",
    "ITEM_ATTR_SIZES",
    "ANSI_ESCAPE",
    "LOG_LOOP_SLEEP_TIME",
    "ITEM_EFFECT_IDS",
)

LOG_LOOP_SLEEP_TIME: float = 0.2  # time to sleep between each flush, (currently 200ms)

IGNORED_ATTRS: dict[int, list[str]] = {}

ANSI_ESCAPE: dict[str, str] = {
    "bold": "1",
    "underline": "4",
    "reverse": "7",
    "invisible": "8",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "reset": "0",
    "clear": "c",
}  # we can add more later (if we need them)

ITEM_EFFECT_IDS: dict[int, int] = {}

ITEM_ATTR_SIZES: dict[str, int] = {
    "id": 4,
    "properties": 2,
    "category": 1,
    "material_type": 1,
    "texture_hash": 4,
    "visual_effect_type": 1,
    "flags2": 4,
    "texture_x": 1,
    "texture_y": 1,
    "storage_type": 1,
    "is_stripey_wallpaper": 1,
    "collision_type": 1,
    "break_hits": 1,
    "reset_time": 4,
    "clothing_type": 1,
    "rarity": 2,
    "max_amount": 1,
    "extra_file_hash": 4,
    "audio_volume": 4,
    "seed_base_index": 1,
    "seed_overlay_index": 1,
    "tree_base_index": 1,
    "tree_leaves_index": 1,
    "seed_colour": 4,
    "seed_overlay_colour": 4,
    "ingredient": 4,
    "grow_time": 4,
    "flags3": 2,
    "is_rayman": 2,
    "overlay_object": 8,
    "flags4": 4,
    "reserved": 68,
    "flags5": 4,
    "bodypart": 9,
    "flags6": 4,
    "growpass_property": 4,
    "can_player_sit": 1,
    "sit_player_offset_x": 4,
    "sit_player_offset_y": 4,
    "sit_overlay_x": 4,
    "sit_overlay_y": 4,
    "sit_overlay_offset_x": 4,
    "sit_overlay_offset_y": 4,
}
