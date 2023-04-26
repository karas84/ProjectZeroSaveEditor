# type: ignore

import os
import struct
import argparse

from ctypes import sizeof

from .save_structs import MC_GAMEDATA


def make_checksum(data: bytes):
    return sum(struct.unpack(f"{len(data)-16}B", data[16:]))


def main():
    parser = argparse.ArgumentParser(description="Project Zero Save Editor")
    parser.add_argument("save_file", metavar="save-file", type=str, help="path to save file (BESLES-50821zero[0-2])")

    args = parser.parse_args()

    with open(args.save_file, "rb") as file_h:
        sz = file_h.seek(0, os.SEEK_END)
        assert sz == sizeof(MC_GAMEDATA), f"wrong file size, expected {sizeof(MC_GAMEDATA)}"
        file_h.seek(0, os.SEEK_SET)
        save_data = file_h.read()

    mc_game_data = MC_GAMEDATA.from_buffer_copy(save_data)

    checksum = make_checksum(save_data)

    assert checksum == mc_game_data.checksum.checksum, "invalid checksum"

    print("Playdata:")
    hour = mc_game_data.mc_header.game.hour
    minute = mc_game_data.mc_header.game.minute
    sec = mc_game_data.mc_header.game.sec
    print(f"  Game Play Time: {hour:02d}:{minute:02d}:{sec:02d}")
    print(f"  Photo Shots: {mc_game_data.ingame_wrk.pht_cnt}")
    print(f"  Ghosts Driven: {mc_game_data.ingame_wrk.ghost_cnt}")
    print()

    print("Camera:")
    print(f"  Points: {mc_game_data.cam_custom_wrk.point}")
    print(f"  Range Lv.: {mc_game_data.cam_custom_wrk.charge_range + 1}")
    print(f"  Speed Lv.: {mc_game_data.cam_custom_wrk.charge_speed + 1}")
    print(f"  Max Value Lv.: {mc_game_data.cam_custom_wrk.charge_max + 1}")
    print()

    print("Items:")
    for i in range(200):
        print(f"  Item {i+1:03d}: {mc_game_data.poss_item[i]}")
    print()

    print("Rooms:")
    for i in range(42):
        print(f"  Room {i+1:03d}: {mc_game_data.room_pass[i]}")
    print()


if __name__ == "__main__":
    main()
