from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime

@dataclass
class Scenario:
    rank: int
    leaderboardId: int
    scenarioName: str
    aimType: str
    authors: list[str]
    description: str
    plays: int
    entries: int

@dataclass
class Score:
    steamId: str
    score: float
    rank: int
    steamAccountName: str
    kovaaksPlusActive: bool
    fov: int
    hash: str
    cm360: float
    epoch: int
    kills: int
    score: float
    avgFps: float
    avgTtk: float
    fovScale: str
    vertSens: float
    horizSens: float
    resolution: str
    sensScale: str
    accuracyDamage: int
    challengeStart: datetime
    scenarioVersion: str
    clientBuildVersion: str
    webappUsername: str

@dataclass
class PlayerSearchResult:
    username: str
    avatar: str

@dataclass
class PlaylistScenario:
    scenarioName: str
    playCount: int

@dataclass
class Playlist:
    playlistName: str
    playlistCode: str
    playlistId: int
    authorName: str
    description: str
    scenarioList: list[PlaylistScenario]
    authorSteamId: str
    subscribers: str
    webappUsername: str
    steamAccountName: str

@dataclass
class Profile:
    playerId: int
    username: str
    created: datetime
    steamId: str
    clientBuildVersion: str
    lastAccess: datetime
    steamAccountName: str
    steamAccountAvatar: str
    admin: bool
    coach: bool
    staff: bool
    videos: list[str]
    # ...
    



class LeaderboardFilter(Enum):
    GLOBAL = 1
    VIP = 2
    FRIENDS = 3
    MY_POSITION = 4

class UnsupportedFilter(Exception): pass
class NoCredentials(Exception): pass