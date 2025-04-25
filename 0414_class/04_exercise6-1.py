class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self) -> float:
        return self.length * self.width * self.height
    
    def getInfo(self) -> str:
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"

def get_dimensions() -> list[float]:
    while True:
        try:
            parts = list(map(float, input("請輸入長方體的長、寬、高(空白間隔): ").split()))
            if len(parts) == 3:
                return parts 
            else:
                print("輸入格式錯誤，請再試一次")
        except ValueError:
            print("輸入格式錯誤，請再試一次")

def main():
    coboid_parts = get_dimensions()
    cuboid = Cuboid(*coboid_parts)
    print("輸入的長方體資訊如下: ")
    print(cuboid.getInfo())

if __name__ == "__main__":
    main()