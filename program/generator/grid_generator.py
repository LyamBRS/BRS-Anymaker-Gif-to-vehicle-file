import sys
from ..prints.debug import BrLogs

def generate_grid(frames, width, height, fps, durations, color_value=79):
    BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Generating wall + indicators")

    # --- WALL CONSTANTS ---
    X_WALL = 7
    X_INDICATOR = 6

    Y_MIN = 6
    Y_MAX = Y_MIN + height-1

    # Centering like your working examples
    z_min = int(-((width-1) // 2) + 3)
    z_max = z_min + (width-1)

    # --- MICROCONTROLLER (fixed) ---
    DATA_PORT_ID = 3

    # --- WALL NODES (4 only) ---
    nodes = [
        {"id": 1, "pos": [X_WALL, Y_MIN, z_min]},
        {"id": 2, "pos": [X_WALL, Y_MIN, z_max]},
        {"id": 3, "pos": [X_WALL, Y_MAX, z_max]},
        {"id": 4, "pos": [X_WALL, Y_MAX, z_min]},
    ]

    # --- EDGES ---
    edges = [
        {"n0": 1, "n1": 2},
        {"n0": 2, "n1": 3},
        {"n0": 3, "n1": 4},
        {"n0": 4, "n1": 1},
    ]

    # --- SINGLE PLATE ---
    plates = [
        {
            "id": 1,
            "nodes": [3, 4, 1, 2]
        }
    ]

    # --- BASE GRID COMPONENT (wall surface) ---
    components = [
        {
            "def": 0,
            "id": 1,
            "colors": [color_value] * 10,
            "is_anchored": True
        },
        {
            "def": 2,
            "id": 2,
            "colors": [color_value] * 10,
            "pos": [
                8,
                3,
                3
            ],
            "rot": [
                0,
                0,
                1,
                0,
                -1,
                0,
                1,
                0,
                0
            ],
            "global_data": [
                {
                    "name": "ticks",
                    "data_value": {
                        "_type": "s32",
                        "type": "type_s32",
                        "data_value": 0
                    }
                },
                {
                    "name": "frames",
                    "data_value": {
                        "_type": "s32",
                        "type": "type_s32",
                        "data_value": 0
                    }
                },
                {
                    "name": "last_frame",
                    "data_value": {
                        "_type": "s32",
                        "type": "type_s32",
                        "data_value": get_last_frame(frames, fps, durations)
                    }
                },
                {
                    "name": "ticks_per_frames",
                    "data_value": {
                        "_type": "s32",
                        "type": "type_s32",
                        "data_value": 0
                    }
                }
            ],
            "script": generate_script(frames, width, height, fps, durations)
        },
        {
            "def": 3,
            "id": DATA_PORT_ID,
            "colors": [color_value] * 10,
            "pos": [
                8,
                4,
                3
            ]
        },
        {
            "def": 4,
            "id": 4,
            "colors": [color_value] * 10,
            "pos": [
                8,
                4,
                6
            ],
            "rot": [
                0,
                -1,
                0,
                1,
                0,
                0,
                0,
                0,
                1
            ],
            "acc": {
                "item": {
                    "_type": "battery_a",
                    "id": 1668,
                    "energy": 14379064.50007799
                }
            }
        },
        {
            "def": 5,
            "id": 5,
            "colors": [color_value] * 10,
            "pos": [
                8,
                3,
                5
            ],
            "rot": [
                -1,
                0,
                0,
                0,
                0,
                -1,
                0,
                -1,
                0
            ]
        },
        {
            "def": 5,
            "id": 6,
            "colors": [color_value] * 10,
            "pos": [
                8,
                3,
                2
            ],
            "rot": [
                -1,
                0,
                0,
                0,
                0,
                -1,
                0,
                -1,
                0
            ]
        }
    ]

    # --- INDICATORS ---
    BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Generating indicators")

    current_id = len(components)+1
    indicator_ids = []

    Y_TOP = Y_MAX
    Z_LEFT = z_max

    for row in range(height):
        for col in range(width):

            y = Y_TOP - row
            z = Z_LEFT - col

            components.append({
                "def": 1,
                "id": current_id,
                "colors": [color_value] * 10,
                "pos": [X_INDICATOR, y, z],
                "rot": [
                    0, 1, 0,
                    -1, 0, 0,
                    0, 0, 1
                ],
                "user_defined_alias": f"l{row}_{col}"
            })

            indicator_ids.append(current_id)
            current_id += 1

        BrLogs.note(f"      - row {row} done")
        sys.stdout.write("\033[1A\r")
        sys.stdout.flush()

    print("")
    BrLogs.success("      - Indicators generated")

    # --- DATA LINKS (ALL INDICATORS → MICROCONTROLLER) ---
    data_links = [
        {
            "p0": {
                "comp": comp_id,
                "pos": 1
            },
            "p1": {
                "comp": DATA_PORT_ID
            },
            "points": []
        }
        for comp_id in indicator_ids
    ]

    # --- FINAL JSON ---
    data = {
        "definitions": {
            "components": [
                "building_floor_sq",
                "light_indicator_a",
                "microcontroller",
                "data_port_straight",
                "battery_a",
                "electric_port_straight"
            ]
        },
        "vehicles": {
            "vehicles": [
                {
                    "id": 60,
                    "transform": {
                        "m": [
                            -0.040758695872208484, 0.0, 0.999169024008766,
                            0.0, 1.0, 0.0,
                            -0.999169024008766, 0.0, -0.040758695872208484
                        ],
                        "t": [
                            0.3347481235396117,
                            -0.4400000000000004,
                            -0.49233222862676485
                        ]
                    },
                    "nodes": nodes,
                    "edges": edges,
                    "plates": plates,
                    "plate_paint": [],
                    "grids": [
                        {
                            "components": components
                        }
                    ],
                    "electric_links": [
                        {
                            "p0": {
                                "comp": 5
                            },
                            "p1": {
                                "comp": 6
                            },
                            "points": []
                        }
                    ],
                    "mechanical_links": [],
                    "liquid_links": [],
                    "gas_links": [],
                    "belt_links": [],
                    "data_links": data_links,
                    "loot_locations": [],
                    "creature_locations": [],
                    "motion_type": "static"
                }
            ]
        }
    }

    BrLogs.success(" - data was created")
    return data


def generate_meta(width, height):
    # Obtained by checking the difference between multiple width and heights created manually
    SCALE = 0.081

    min_x = -0.06000000476837153
    max_x = 0.6200000047683716

    min_y = 0.11999998241662979
    max_y = min_y + (height * SCALE)

    # Referenced objects were asymetrical
    min_z = -0.06000000476837164 - (width * SCALE * 0.5)
    max_z = 0.6200000047683716 + (width * SCALE * 0.5)

    data = {
        "vehicles": {
            "vehicles": [
                {
                    "id": 60,
                    "transform": {
                        "m": [
                            -0.040758695872208484, 0.0, 0.999169024008766,
                            0.0, 1.0, 0.0,
                            -0.999169024008766, 0.0, -0.040758695872208484
                        ],
                        "t": [
                            0.3347481235396117,
                            -0.4400000000000004,
                            -0.49233222862676485
                        ]
                    },
                    "bounds": {
                        "min": [min_x, min_y, min_z],
                        "max": [max_x, max_y, max_z]
                    }
                }
            ]
        }
    }

    BrLogs.success(" - meta was created")
    return data



def generate_frame_script(frames_data, width, height, fps, durations):

    lines = []

    if fps is not None:
        ticks_per_frame = max(1, round(60/fps))

    # start with everything OFF
    prev = [[1 for _ in range(width)] for _ in range(height)]

    for f_idx, frame in enumerate(frames_data):

        if fps is None:
            ms = durations[f_idx]
            frame_tick = int(ms * 60 / 1000)
        else:
            sys.exit()
            frame_tick = f_idx*ticks_per_frame

        lines.append(f"\tif (var frames == {frame_tick})")
        lines.append("\t{")

        for row in range(height):
            for col in range(width):

                alias = f"l{row}_{col}"
                state = "true" if frame[row][col] == 1 else "false"
                prev_state = "true" if prev[row][col] == 1 else "false"

                if prev_state != state:
                    lines.append(
                        f"\t\tin {alias}.is_illuminated = {state}"
                    )

        lines.append("\t}\n")

        # update previous frame
        prev = frame

    return "\n".join(lines)

def generate_script(frames_data, width, height, fps, durations):

    last_frame = get_last_frame(frames_data, fps, durations)

    BASE_SCRIPT = f"define var integer ticks\ndefine var integer last_frame\ndefine var integer frames\ndefine var integer ticks_per_frames\nvar ticks = 0\nvar last_frame = {last_frame}\nvar frames = 0\nvar ticks_per_frames = 0\non_tick\n{{\n\tvar frames = var frames + 1\n\tif (var frames > var last_frame)\n\t{{\n\t\tvar frames = 0\n\t}}\n"
    frame_blocks = generate_frame_script(frames_data, width, height, fps, durations)
    script = BASE_SCRIPT + frame_blocks
    return script


def get_last_frame(frames_data, fps, durations):
    if fps is not None:
        BrLogs.info(f"  - User predefined fps will be utilized: {BrLogs.BRIGHT_CYAN}{BrLogs.BOLD}{fps}")
        ticks_per_frame = max(1, round(60/fps))
        last_frame = len(frames_data) * ticks_per_frame
    else:
        total_duration = sum(durations)
        last_frame = int(total_duration * 60 / 1000)
    return last_frame