from typing import TypedDict, List, Optional


class VideoInfo(TypedDict):
    comment: int
    typeid: int
    play: int
    pic: str
    subtitle: str
    description: str
    copyright: str
    title: str
    review: int
    author: str
    mid: int
    created: int
    length: str
    video_review: int
    aid: int
    bvid: str
    hide_click: bool
    is_pay: int
    is_union_video: int
    is_steins_gate: int
    is_live_playback: int
    meta: Optional[None]
    is_avoided: int
    attribute: int
    is_charging_arc: bool
    vt: int
    enable_vt: int
    vt_display: str
    playback_position: int


class VList(TypedDict):
    vlist: List[VideoInfo]


class Data(TypedDict):
    list: VList


class RootDict(TypedDict):
    data: Data
    code: int
    message: str
    ttl: int
