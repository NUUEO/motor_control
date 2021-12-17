pulses = 0.002511161

class Command():
    def __init__(self):
        pass

    def scan(self):
        cmd = []
        for i in range(16):
            j = str(hex(i))
            j = j.replace("0x","")
            cmd.append(str(j)+"in")
        return cmd

    def ma(self,channel=0,deg=0.0): #絕對移動度數
        data = str(hex(round(deg/pulses))) #將角度除以每次脈沖的度數

        # 字串處理，將16進位的0x移除，並且補足八位元
        data = data.replace('0x','')
        while  len(data) < 8:
            data = '0'+ data
        data = data.upper()
        # 將header與馬達編號轉為字串寫入
        header = str(channel)+"ma"
        return header+str(data)

    def mr(self,channel=0,deg=0.0): #相對移動度數
        data = str(hex(round(deg/pulses))) #將角度除以每次脈沖的度數

        # 字串處理，將16進位的0x移除，並且補足八位元
        data = data.replace('0x','')
        while  len(data) < 8:
            data = '0'+ data
        data = data.upper()
        # 將header與馬達編號轉為字串寫入
        header = str(channel)+"mr"
        return header+str(data)

    def set_jog_step_size(self,channel=0,deg=3): #設定吋動角度
        data = str(hex(round(deg/pulses)))
        data = data.replace('0x','')
        while  len(data) < 8:
            data = '0'+ data
        data = data.upper()
        # 將header與馬達編號轉為字串寫入
        header = str(channel)+"sj"
        return header+str(data)

    def forward(self,channel=0): #正轉
        header = str(channel)+"fw"
        return header
    def backward(self,channel=0):#反轉
        header = str(channel)+"bw"
        return header

    def home(self,channel=0): #回原點
        return str(channel)+"ho1"

    def clean(self,channel=0): #利用旋轉進行清潔
        return str(channel)+"cm"

    def stop(self,channel=0): #停止運作
        return str(channel)+"st"

    def optimize(self,channel=0): #優化諧振
        return str(channel)+"om"

if __name__=='__main__':
    c =Command()
    print(c.scan())
    print(c.ma(1,350))
    print(c.home(1))
    print(c.set_jog_step_size(1,30))
