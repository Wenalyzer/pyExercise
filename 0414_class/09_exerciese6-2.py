class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self) -> float:
        return self.length * self.width * self.height
    
    def getInfo(self) -> str:
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"
    
    @staticmethod
    def getCuboidsInfo(cuboids: list["Cuboid"]) -> str:
        return "\n".join(c.getInfo() for c in cuboids)

def get_positive_int() -> int:
    while True:
        try:
            value = int(input("請問有幾個長方體?  "))
            if value > 0:
                return value
            else:
                print("輸入格式錯誤，請再試一次")
        except ValueError:
            print("輸入格式錯誤，請再試一次")

def generate_cuboids_list(n: int) -> list[Cuboid]:
    return [Cuboid(*get_dimensions(i)) for i in range(n)]

def get_dimensions(index: int) -> list[float]:
    while True:
        try:
            parts = list(map(float, input(f"請輸入第{index+1}個長方體的長、寬、高(空白間隔): ").split()))
            if len(parts) == 3:
                return parts
            else:
                print("輸入格式錯誤，請再試一次")
        except ValueError:
            print("輸入格式錯誤，請再試一次")

def main():
    cuboid_num = get_positive_int()
    cuboids_list = generate_cuboids_list(cuboid_num)
    print(f"輸入的{cuboid_num}個長方體資訊如下: ")
    print(Cuboid.getCuboidsInfo(cuboids_list))

if __name__ == "__main__":
    main()