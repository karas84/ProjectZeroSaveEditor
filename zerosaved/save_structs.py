# type: ignore

from enum import Enum
from ctypes import (
    LittleEndianStructure,
    Union,
    c_uint32,
    c_int32,
    c_int64,
    c_uint64,
    c_uint8,
    c_short,
    c_float,
    c_ushort,
    c_char_p,
    c_char,
    sizeof,
)


class LittleEndianStructureFieldsFromTypeHints(type(LittleEndianStructure)):
    def __new__(cls, name, bases, namespace):
        annotations = namespace.get("__annotations__", {})
        namespace["_pack_"] = 1
        namespace["_fields_"] = list(annotations.items())
        return type(LittleEndianStructure).__new__(cls, name, bases, namespace)


class CStructure(LittleEndianStructure, metaclass=LittleEndianStructureFieldsFromTypeHints):
    pass


class UnionFieldsFromTypeHints(type(Union)):
    def __new__(cls, name, bases, namespace):
        annotations = namespace.get("__annotations__", {})
        namespace["_pack_"] = 1
        namespace["_fields_"] = list(annotations.items())
        return type(Union).__new__(cls, name, bases, namespace)


class CUnion(Union, metaclass=UnionFieldsFromTypeHints):
    pass


def POINTER(*args, **kwargs):
    return c_uint32


# make int 4 bytes and long 8 bytes
c_int = c_int32
c_uint = c_uint32
c_long = c_int64
c_ulong = c_uint64
c_void_p = POINTER(c_uint32)

# add missing types
c_uchar = c_uint8
c_uchar_p = POINTER(c_uchar)
c_short_p = POINTER(c_short)
c_ushort_p = POINTER(c_ushort)
c_int_p = POINTER(c_int)
c_uint_p = POINTER(c_uint)
c_long_p = POINTER(c_long)
c_ulong_p = POINTER(c_ulong)
c_float_p = POINTER(c_float)


class MC_DATA_STR(CStructure):
    addr: c_uchar_p
    size: c_int


class MC_GAME_HEADER(CStructure):
    map_flg: c_uint
    msn_no: c_uint
    room_no: c_uint
    hour: c_uint
    minute: c_uint
    sec: c_uint
    frame: c_uint
    msn_flg: c_uchar
    language: c_uchar
    clear_flg: c_uchar
    difficult: c_uchar


class MC_ALBUM_HEADER(CStructure):
    map_flg: c_uint
    photo_num: c_uint
    type: c_uint
    pad: c_uint * 5


class MC_HEADER(CUnion):
    game: MC_GAME_HEADER
    album: MC_ALBUM_HEADER


class OPTION_WRK(CStructure):
    pad_mode: c_uchar
    pad_move: c_uchar
    key_type: c_uchar
    sound_mode: c_uchar
    bgm_vol: c_short
    bgm_vol_bak: c_short
    se_vol: c_short
    field7_0xa: c_uint8
    field8_0xb: c_uint8
    padding: c_uint


class INGAME_WRK(CStructure):
    game: c_uchar
    mode: c_uchar
    init_flg: c_uchar
    stts: c_uchar
    msn_no: c_uchar
    difficult: c_uchar
    clear_count: c_uchar
    rg_pht_cnt: c_uchar
    ghost_cnt: c_short
    field9_0xa: c_uint8
    field10_0xb: c_uint8
    pht_cnt: c_uint
    high_score: c_uint
    total_point: c_uint
    padding: c_uint


class MSN_LOAD_DAT(CStructure):
    file_no: c_short
    file_type: c_uchar
    tmp_no: c_uchar
    addr: c_uint


class sceCdCLOCK(CStructure):
    stat: c_uchar
    second: c_uchar
    minute: c_uchar
    hour: c_uchar
    pad: c_uchar
    day: c_uchar
    month: c_uchar
    year: c_uchar


class TIME_WRK(CStructure):
    start: sceCdCLOCK
    real: sceCdCLOCK
    real_ofs: c_ulong
    game: c_ulong
    one_game: c_ulong
    play: c_ulong
    area: c_ulong
    room: c_ulong
    finder: c_ulong
    swalk: c_ulong
    nwalk: c_ulong
    fwalk: c_ulong
    run: c_ulong
    stop: c_ulong
    zerohour: c_ulong
    no_pad: c_ulong
    padding: c_ulong


class P_INT(CUnion):
    pu8: c_uchar_p
    pu16: c_short_p
    pu32: c_uint_p
    pu64: c_ulong_p
    ps8: c_char_p
    ps16: c_ushort_p
    ps32: c_int_p
    ps64: c_long_p
    wrk: c_long


class MOVE_BOX(CStructure):
    job_no: c_uchar
    pos_no: c_uchar
    wait_time: c_uchar
    idx: c_uchar
    loop: c_short
    reserve: c_short
    se: c_int
    field7_0xc: c_uint8
    field8_0xd: c_uint8
    field9_0xe: c_uint8
    field10_0xf: c_uint8
    pos: c_float * 4
    tpos: c_float * 4
    spd: c_float * 4
    rot: c_float * 4
    rspd: c_float * 4
    trot: c_float * 4
    pos_mid: c_float * 4
    comm_add: P_INT
    comm_add_top: c_long


class SPOT_WRK(CStructure):
    pos: c_float * 4
    direction: c_float * 4
    diffuse: c_float * 4
    intens: c_float
    power: c_float
    pad: c_float * 2


class POINT_WRK(CStructure):
    pos: c_float * 4
    diffuse: c_float * 4
    power: c_float
    pad: c_float * 3


class PARARELL_WRK(CStructure):
    direction: c_float * 4
    diffuse: c_float * 4


class LIGHT_PACK(CStructure):
    parallel_num: c_int
    point_num: c_int
    spot_num: c_int
    pad: c_int
    ambient: c_float * 4
    parallel: PARARELL_WRK * 3
    point: POINT_WRK * 3
    spot: SPOT_WRK * 3


class PROOM_INFO(CStructure):
    se_foot: c_uchar
    room_no: c_uchar
    room_old: c_uchar
    pad: c_uchar
    camera_no: c_short
    camera_no_old: c_short
    camera_btl: c_short
    camera_btl_old: c_short
    camera_drm: c_short
    camera_drm_old: c_short
    camera_door: c_short
    camera_door_old: c_short
    camera_door_did: c_short
    camera_door_rid: c_uchar
    cam_type: c_uchar
    hight: c_float


class DOPEN_POS(CStructure):
    door_id: c_short
    flag: c_uchar
    room_no: c_uchar
    field3_0x4: c_uint8
    field4_0x5: c_uint8
    field5_0x6: c_uint8
    field6_0x7: c_uint8
    field7_0x8: c_uint8
    field8_0x9: c_uint8
    field9_0xa: c_uint8
    field10_0xb: c_uint8
    field11_0xc: c_uint8
    field12_0xd: c_uint8
    field13_0xe: c_uint8
    field14_0xf: c_uint8
    dov: c_float * 4


class PLYR_WRK(CStructure):
    sta: c_uint
    mvsta: c_uint
    mode: c_uchar
    cam_type: c_uchar
    anime_no: c_uchar
    cond: c_uchar
    cond_tm: c_short
    flash_tm: c_short
    aphoto_tm: c_short
    dmg: c_short
    hp: c_short
    ap_timer: c_short
    dwalk_tm: c_short
    fh_no: c_short
    fh_deg: c_float
    spd: c_float
    spd_ud: c_float
    prot: c_float
    frot_x: c_float
    charge_deg: c_float
    charge_rate: c_float
    charge_num: c_uchar
    rock_trgt: c_uchar
    film_no: c_uchar
    dmg_cam_flag: c_uchar
    hp_num: c_uchar
    mode_save: c_uchar
    move_mot: c_uchar
    atk_no: c_uchar
    near_ene_no: c_uchar
    photo_charge: c_uchar
    dmg_type: c_uchar
    spe1_dir: c_uchar
    pr_set: c_char
    po_set: c_char
    reserve: c_uchar * 2
    field36_0x48: c_uint8
    field37_0x49: c_uint8
    field38_0x4a: c_uint8
    field39_0x4b: c_uint8
    field40_0x4c: c_uint8
    field41_0x4d: c_uint8
    field42_0x4e: c_uint8
    field43_0x4f: c_uint8
    mv: c_float * 4
    op: c_float * 4
    rock_adj: c_float * 4
    bwp: c_float * 4
    cp_old: c_float * 4
    soulp: c_float * 4
    spot_rot: c_float * 4
    spot_pos: c_float * 4
    shadow_direction: c_float * 4
    psave: c_float * 4
    fhp: c_float * 5 * 4
    fp: c_ushort * 2
    field56_0x144: c_uint8
    field57_0x145: c_uint8
    field58_0x146: c_uint8
    field59_0x147: c_uint8
    field60_0x148: c_uint8
    field61_0x149: c_uint8
    field62_0x14a: c_uint8
    field63_0x14b: c_uint8
    field64_0x14c: c_uint8
    field65_0x14d: c_uint8
    field66_0x14e: c_uint8
    field67_0x14f: c_uint8
    move_box: MOVE_BOX
    mylight: LIGHT_PACK
    pr_info: PROOM_INFO
    field71_0x3cc: c_uint8
    field72_0x3cd: c_uint8
    field73_0x3ce: c_uint8
    field74_0x3cf: c_uint8
    dop: DOPEN_POS
    se_deadly: c_int
    padding: c_uint
    field78_0x3f8: c_uint8
    field79_0x3f9: c_uint8
    field80_0x3fa: c_uint8
    field81_0x3fb: c_uint8
    field82_0x3fc: c_uint8
    field83_0x3fd: c_uint8
    field84_0x3fe: c_uint8
    field85_0x3ff: c_uint8


class AENE_INFO_DAT(CStructure):
    dat_no: c_uchar
    soul_no: c_uchar
    dir: c_short
    px: c_short
    py: c_ushort
    pz: c_short
    adpcm_tm: c_short
    adpcm_no: c_int
    rng: c_short
    mdl_no: c_short
    anm_no: c_short
    point_base: c_short
    se_no: c_uint
    se_foot: c_int


class ENE_DAT(CStructure):
    attr1: c_uint
    dst_gthr: c_short
    way_gthr: c_uchar
    atk_ptn: c_uchar
    wspd: c_uchar
    rspd: c_uchar
    hp: c_short
    atk_rng: c_short
    hit_rng: c_short
    chance_rng: c_short
    hit_adjx: c_ushort
    atk_p: c_short
    atk_h: c_short
    atk: c_uchar
    atk_tm: c_uchar
    mdl_no: c_short
    anm_no: c_short
    field17_0x1e: c_uint8
    field18_0x1f: c_uint8
    se_no: c_uint
    adpcm_no: c_uint
    dead_adpcm: c_int
    point_base: c_short
    hint_pic: c_uchar
    aura_alp: c_uchar
    area: c_uchar * 6
    dir: c_short
    px: c_short
    py: c_ushort
    pz: c_short
    field30_0x3e: c_uint8
    field31_0x3f: c_uint8


class MPOS(CStructure):
    p0: c_float * 4
    p1: c_float * 4
    p2: c_float * 4
    p3: c_float * 4
    p4: c_float * 4
    p5: c_float * 4
    p6: c_float * 4
    p7: c_float * 4
    p8: c_float * 4
    p9: c_float * 4


class ENE_WRK(CStructure):
    sta: c_uint
    sta2: c_uint
    hp: c_short
    dmg: c_short
    dmg_old: c_short
    atk_tm: c_short
    type: c_uchar
    dat_no: c_uchar
    act_no: c_uchar
    anime_no: c_uchar
    field10_0x14: c_uint8
    field11_0x15: c_uint8
    field12_0x16: c_uint8
    field13_0x17: c_uint8
    field14_0x18: c_uint8
    field15_0x19: c_uint8
    field16_0x1a: c_uint8
    field17_0x1b: c_uint8
    field18_0x1c: c_uint8
    field19_0x1d: c_uint8
    field20_0x1e: c_uint8
    field21_0x1f: c_uint8
    move_box: MOVE_BOX
    dat: POINTER(ENE_DAT)
    field24_0xb4: c_uint8
    field25_0xb5: c_uint8
    field26_0xb6: c_uint8
    field27_0xb7: c_uint8
    field28_0xb8: c_uint8
    field29_0xb9: c_uint8
    field30_0xba: c_uint8
    field31_0xbb: c_uint8
    field32_0xbc: c_uint8
    field33_0xbd: c_uint8
    field34_0xbe: c_uint8
    field35_0xbf: c_uint8
    mpos: MPOS
    mylight: LIGHT_PACK
    dist_p_e: c_float
    dist_c_e: c_float
    pra_per: c_float
    pr_anime: c_float
    pra_time: c_short
    bloop: c_short
    bjob_no: c_uchar
    bpos_no: c_uchar
    bwait_time: c_uchar
    recog_tm: c_uchar
    bcomm_add: P_INT
    bcomm_add_top: c_long
    tr_rate: c_uchar
    ajob_no: c_uchar
    apos_no: c_uchar
    await_time: c_uchar
    field54_0x35c: c_uint8
    field55_0x35d: c_uint8
    field56_0x35e: c_uint8
    field57_0x35f: c_uint8
    acomm_add: P_INT
    acomm_add_top: c_long
    pdf: c_void_p
    d_pd: c_float
    pdf2: c_void_p
    d_pd2: c_float
    nee: c_void_p
    nee_rate: c_float
    nee_size: c_float
    nee_col: c_uint
    se_omen: c_int * 2
    field69_0x398: c_uint8
    field70_0x399: c_uint8
    field71_0x39a: c_uint8
    field72_0x39b: c_uint8
    field73_0x39c: c_uint8
    field74_0x39d: c_uint8
    field75_0x39e: c_uint8
    field76_0x39f: c_uint8
    adjp: c_float * 4
    pp: c_float * 4
    sp: c_float * 4
    si: c_float * 4
    bep: c_float * 4
    in_finder_tm: c_short
    area: c_uchar * 6
    tr_time: c_short
    tr_max: c_uchar
    dmg_type: c_uchar
    room_no: c_uchar
    se_area_no: c_char
    ani_reso: c_uchar
    ani_reso_tm: c_uchar
    fp: c_ushort * 2
    fp2: c_ushort * 3 * 2
    eroot: c_uchar * 2
    plight_svo: c_uchar
    slight_svo: c_uchar
    plight_svm: c_uchar * 2
    slight_svm: c_uchar * 2
    pa_radius: c_float
    aie: POINTER(AENE_INFO_DAT)
    stm_slow: c_short
    stm_view: c_short
    stm_stop: c_short
    tr_rate2: c_uchar
    field104_0x427: c_uint8
    field105_0x428: c_uint8
    field106_0x429: c_uint8
    field107_0x42a: c_uint8
    field108_0x42b: c_uint8
    field109_0x42c: c_uint8
    field110_0x42d: c_uint8
    field111_0x42e: c_uint8
    field112_0x42f: c_uint8


class MAP_WRK(CStructure):
    dat_adr: c_int
    floor: c_uchar
    load_area: c_uchar
    now_room: c_uchar
    next_room: c_uchar
    room_update_flg: c_uchar
    mirror_flg: c_uchar
    flr_exist: c_uchar * 4
    field8_0xe: c_uint8
    field9_0xf: c_uint8
    padding: c_uint


class AP_WRK(CStructure):
    stts: c_uchar
    gtime: c_uchar
    rtime: c_uchar
    ptime: c_uchar
    atime: c_uchar * 11
    room_fg: c_uchar * 42
    sound: c_uchar
    pic_num: c_uchar
    raze: c_uchar
    fg_mode: c_uchar
    fgst_no: c_uchar
    gg_mode: c_uchar
    ggst_no: c_uchar
    zh_mode: c_uchar
    zh_efct: c_uchar
    fg_pos: c_uchar * 2 * 3
    fg_set_num: c_uchar
    fg_se_empty: c_uchar * 3
    gg_room: c_uchar * 5
    pg_req: c_uchar * 5
    ggst_cnt: c_uchar
    field21_0x57: c_uint8
    fgst_cnt: c_short
    dgst_cnt: c_short
    zh_ap: c_short
    fg_ap: c_short


class EVENT_WRK(CStructure):
    mode: c_uchar
    evt_no: c_uchar
    movie_on: c_uchar
    next_msn: c_uchar
    msg_init: c_uchar
    use_item: c_uchar
    get_item: c_uchar
    btl_ene: c_uchar
    end_ev: c_uchar
    btl_lock: c_uchar
    pht_2d: c_uchar
    pht_furn: c_uchar
    pht_ev: c_uchar * 10
    pos_req: c_uchar * 16
    spev_tmp: c_uchar * 4
    gst_door: c_uchar * 2
    face_stts: c_uchar * 4


class DOOR_MDATA(CStructure):
    sgd_door: c_uint_p
    mno_door: c_short
    field2_0x6: c_uint8
    field3_0x7: c_uint8


class ROOM_MDATA(CStructure):
    sgd_room: c_uint_p
    sgd_furn: c_uint_p * 30
    mno_room: c_short
    mno_furn: c_short * 30
    room_id: c_uchar
    field5_0xbb: c_uint8


class AREA_WRK(CStructure):
    rmd: ROOM_MDATA * 6
    dmd: DOOR_MDATA * 20
    field2_0x508: c_uint8
    field3_0x509: c_uint8
    field4_0x50a: c_uint8
    field5_0x50b: c_uint8
    field6_0x50c: c_uint8
    field7_0x50d: c_uint8
    field8_0x50e: c_uint8
    field9_0x50f: c_uint8
    tmp_after_pos: c_float * 4
    area_no: c_uchar
    area_bak: c_uchar
    room: c_uchar * 6
    rgst: c_uchar * 5
    ev_se: c_uchar
    fg_max: c_uchar
    field17_0x52f: c_uint8
    padding: c_uint
    field19_0x534: c_uint8
    field20_0x535: c_uint8
    field21_0x536: c_uint8
    field22_0x537: c_uint8
    field23_0x538: c_uint8
    field24_0x539: c_uint8
    field25_0x53a: c_uint8
    field26_0x53b: c_uint8
    field27_0x53c: c_uint8
    field28_0x53d: c_uint8
    field29_0x53e: c_uint8
    field30_0x53f: c_uint8


class FURN_ATTR_FLG(CStructure):
    flg: c_uint
    padding: c_uint


class DOOR_STTS_KEEP(CStructure):
    mdl_no: c_short
    attr: c_short
    stts: c_uchar
    stts_map: c_uchar
    room_id: c_uchar
    field5_0x7: c_uint8
    padding: c_uint


class PGOST_WRK(CStructure):
    req_no: c_uchar
    pgst_no: c_uchar
    ev_no: c_uchar
    stts: c_uchar
    time: c_uchar


class CAM_CUSTOM_WRK(CStructure):
    charge_range: c_uchar
    charge_max: c_uchar
    charge_speed: c_uchar
    func_sub: c_uchar * 5
    func_spe: c_uchar * 5
    set_sub: c_uchar
    set_spe: c_uchar
    field7_0xf: c_uint8
    point: c_ulong


class EN_ST_WANDER_SOUL(Enum):
    ST_WANSO_VACANT = 0
    ST_WANSO_INIT = 1
    ST_WANSO_WANDER = 2
    ST_WANSO_SET_MOVE = 3
    ST_WANSO_MOVE = 4
    ST_WANSO_SPEED_DOWN = 5
    ST_WANSO_SPLINE = 6
    ST_WANSO_FLOAT = 10
    ST_WANSO_WAIT = 11
    ST_WANSO_TELLIN = 12
    ST_WANSO_ADPCM_OUT = 13
    ST_WANSO_TELL = 14
    ST_WANSO_EXTINCT = 20
    SOUL_LIGHT_WAIT = 21
    SOUL_LIGHT_BIGGER = 22
    SOUL_LIGHT_LESSER = 23
    SOUL_LIGHT_END = 24
    SOUL_LIGHT_VANISH_IN = 30
    SOUL_LIGHT_VANISH = 31
    SOUL_LIGHT_APPEAR_IN = 32
    SOUL_LIGHT_APPEAR = 33


class WANDER_SOUL_WRK(CStructure):
    state: c_uint  # EN_ST_WANDER_SOUL
    vanish: c_uint  # EN_ST_WANDER_SOUL
    id: c_uchar
    disp_flg: c_uchar
    turn: c_uchar
    move_flg: c_uchar
    count: c_short
    field7_0xe: c_uint8
    field8_0xf: c_uint8
    spl_speed: c_float
    field10_0x14: c_uint8
    field11_0x15: c_uint8
    field12_0x16: c_uint8
    field13_0x17: c_uint8
    field14_0x18: c_uint8
    field15_0x19: c_uint8
    field16_0x1a: c_uint8
    field17_0x1b: c_uint8
    field18_0x1c: c_uint8
    field19_0x1d: c_uint8
    field20_0x1e: c_uint8
    field21_0x1f: c_uint8
    sp_mat: c_float * 4 * 4
    ori_pos: c_float * 4
    disp_pos: c_float * 4
    speedv: c_float * 4
    accelv: c_float * 4
    type: c_uchar
    message_id: c_uchar
    face_id: c_short
    adpcm_id: c_short
    spl_flg: c_uchar
    field32_0xa7: c_uint8
    destination: c_float_p  # FIXME * 4),
    room_no: c_uchar
    field35_0xad: c_uint8
    field36_0xae: c_uint8
    field37_0xaf: c_uint8
    dist: c_float
    eff_buff: c_void_p
    wanso_wait_time: c_uint
    srate: c_float
    arate: c_float
    lightpower: c_float
    field44_0xc8: c_uint8
    field45_0xc9: c_uint8
    field46_0xca: c_uint8
    field47_0xcb: c_uint8
    field48_0xcc: c_uint8
    field49_0xcd: c_uint8
    field50_0xce: c_uint8
    field51_0xcf: c_uint8


class FURN_DAT_SAVE(CStructure):
    eventflg: c_uchar
    data: c_uchar


class GLIST_INDEX(CStructure):
    disp_flg: c_char
    new_flg: c_char


class CLEAR_BONUS(CStructure):
    costume: c_uchar
    clear_info: c_uchar


class STAGE_WRK(CStructure):
    rank: c_uchar
    field1_0x1: c_uint8
    best_time: c_short
    field3_0x4: c_uint8
    field4_0x5: c_uint8
    field5_0x6: c_uint8
    field6_0x7: c_uint8
    best_shot: c_long


class PICTURE_WRK(CStructure):
    adr_no: c_uchar
    msn_no: c_uchar
    room: c_uchar
    status: c_uchar
    subject: c_short * 3 * 2
    score: c_uint
    time: sceCdCLOCK


class SAVE_RANK(CStructure):
    pic_inf: PICTURE_WRK * 10
    pic_num: c_short
    best_score: c_short


class MC_HEADER_CHECKSUM(CStructure):
    checksum: c_int32
    dummy: c_uint8 * 12


class MC_GAMEDATA(CStructure):
    checksum: MC_HEADER_CHECKSUM
    mc_header: MC_HEADER
    opt_wrk: OPTION_WRK
    ingame_wrk: INGAME_WRK
    load_dat_wrk: MSN_LOAD_DAT * 40
    time_wrk: TIME_WRK
    plyr_wrk: PLYR_WRK
    ene_wrk: ENE_WRK * 4
    map_wrk: MAP_WRK
    ap_wrk: AP_WRK
    ev_wrk: EVENT_WRK
    event_stts: c_uchar * 250
    find_stts: c_uchar * 250
    poss_item: c_uchar * 200
    poss_file: c_uchar * 4 * 50
    flm_exp_flg: c_uchar * 5
    item_ap: c_short * 300 * 2
    area_wrk: AREA_WRK
    furn_attr_flg: FURN_ATTR_FLG * 500
    door_keep: DOOR_STTS_KEEP * 300
    room_pass: c_uchar * 42
    pg_wrk: PGOST_WRK
    cam_custom_wrk: CAM_CUSTOM_WRK
    f_dat_save: FURN_DAT_SAVE * 430
    wander_soul_wrk: WANDER_SOUL_WRK
    glist_index: GLIST_INDEX * 108
    cribo: CLEAR_BONUS
    stage_wrk: STAGE_WRK * 20
    save_rank: SAVE_RANK
    DAT_01a9f000: c_uint8 * 0x6400
    DAT_01be2380: c_uint8 * 0x84120
    _align_pad: c_uint8 * 2


struct_expected_sizes = [
    0x20,
    0x10,
    0x1C,
    0x140,
    0x88,
    0x400,
    0x10C0,
    0x14,
    0x60,
    0x30,
    0xFA,
    0xFA,
    0xC8,
    0xC8,
    0x5,
    0x4B0,
    0x540,
    0xFA0,
    0xE10,
    0x2A,
    0x5,
    0x18,
    0x35C,
    0xD0,
    0xD8,
    0x2,
    0x140,
    0x11C,
    0x6400,
    0x84120,
]

_errors: list[str] = []
for (field_name, field_type), expected_size in zip(MC_GAMEDATA._fields_[1:], struct_expected_sizes):
    actual_size = sizeof(field_type)
    if actual_size != expected_size:
        _errors.append(
            f"{field_name:20s} {hex(actual_size):8s} {hex(expected_size):8s} {actual_size-expected_size:+5d}"
        )

if _errors:
    raise RuntimeError("\n" + "\n".join(_errors) + "\n")
