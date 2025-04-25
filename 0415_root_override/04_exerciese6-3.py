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

class House(Cuboid):
    def __init__(self, length=1.0, width=1.0, height=1.0, material=""):
        super().__init__(length, width, height)
        self.material = material
    
    def getInfo(self) -> str:
        return super().getInfo() + f", 材質: {self.material}"

def get_positive_int() -> int:
    while True:
        try:
            value = int(input("請問有幾間房屋?  "))
            if value > 0:
                return value
            else:
                print("輸入格式錯誤，請再試一次")
        except ValueError:
            print("輸入格式錯誤，請再試一次")

def generate_houses_list(n: int) -> list[House]:
    return [House(*get_params(i)) for i in range(n)]

def get_params(index: int) -> list[float | str]:
    while True:
        params = list(input(f"請輸入第{index+1}間房屋的長、寬、高與材質(空白間隔): ").split())
        if len(params) == 4:
            material = params.pop()
            if material.upper() not in ('A', 'B', 'C'):
                print("輸入格式錯誤，請再試一次")
                continue
            try:
                # params = [float(p) for p in params]
                params = list(map(float, params))
                params.append(material.upper())
                return params
            except ValueError:
                print("輸入格式錯誤，請再試一次")
        else:
            print("輸入格式錯誤，請再試一次")

def main():
    houses_num = get_positive_int()
    houses_list = generate_houses_list(houses_num)
    print(f"輸入的{houses_num}間房屋資訊如下: ")
    print(Cuboid.getCuboidsInfo(houses_list))

if __name__ == "__main__":
    main()