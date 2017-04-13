#!/usr/bin/env python

"""Generate in files based on 96x96 size hotspots."""

files = (
    (45.5, 46.8, "X_cursor"),
    (50, 46, "bd_double_arrow"),
    (16, 84, "bottom_left_corner"),
    (84, 84, "bottom_right_corner"),
    (50, 72, "bottom_side"),
    (48, 72, "bottom_tee"),
    (14.5, 10.6, "circle"),
    (23.1, 74.1, "color-picker"),
    (18.8, 11.2, "copy"),
    (44, 44, "cross"),
    (48, 48, "crossed_circle"),
    (44, 44, "crosshair"),
    (45, 50, "dnd-ask"),
    (45, 50, "dnd-copy"),
    (45, 50, "dnd-link"),
    (45, 50, "dnd-move"),
    (45, 50, "dnd-none"),
    (46, 46, "dotbox"),
    (46, 46, "fd_double_arrow"),
    (48, 50, "grabbing"),
    (47.6, 28, "hand1"),
    (36, 20, "hand2"),
    (27, 15, "left_ptr"),
    (23.2, 13.2, "left_ptr_watch"),
    (24, 50, "left_side"),
    (28, 48, "left_tee"),
    (19, 11.4, "link"),
    (21, 67, "ll_angle"),
    (72, 67, "lr_angle"),
    (19, 11, "move"),
    (28.6, 82.6, "pencil"),
    (48, 48, "plus"),
    (46, 80, "question_arrow"),
    (65, 16, "right_ptr"),
    (76, 50, "right_side"),
    (72, 48, "right_tee"),
    (50, 72, "sb_down_arrow"),
    (47, 46, "sb_h_double_arrow"),
    (24, 45.6, "sb_left_arrow"),
    (75, 45, "sb_right_arrow"),
    (51, 17, "sb_up_arrow"),
    (45, 45, "sb_v_double_arrow"),
    (50, 46, "tcross"),
    (21, 21, "top_left_corner"),
    (72, 21, "top_right_corner"),
    (50, 20, "top_side"),
    (48, 24, "top_tee"),
    (22, 25, "ul_angle"),
    (72, 25, "ur_angle"),
    (48, 46, "watch"),
    (50, 50, "xterm"),
)

for file_ in files:
    with open("%s.in" % file_[2], "w") as f:
        for size in (24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96):
            f.write("{size} {xhot} {yhot} {size}x{size}/{file_}.png\n".format(
                size = size,
                xhot = round(file_[0] / 96 * size),
                yhot = round(file_[1] / 96 * size),
                file_= file_[2]
            ))
