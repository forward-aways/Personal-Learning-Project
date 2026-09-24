class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or []

    def add(self, song):
        self.songs.append(song)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self.songs)} songs)"

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)

    def __eq__(self, other):
        return isinstance(other, Playlist) and self.songs == other.songs

    def __hash__(self):
        return hash((self.name, tuple(self.songs)))


pl = Playlist("我的歌单")
pl.add("晴天")
pl.add("稻香")
pl.add("七里香")

print(len(pl))                    # 3
print(pl[0])                      # 晴天
print("稻香" in pl)               # True
print(pl)                         # Playlist('我的歌单', 3 songs)

for song in pl:                   # 能 for 遍历
    print(song)

pl2 = Playlist("别人的歌单", ["晴天", "稻香", "七里香"])
print(pl == pl2)                  # True（只看歌曲内容）