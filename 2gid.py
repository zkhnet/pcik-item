import struct
import sys

out = ""
cLen = 368
argc = len(sys.argv)

if argc == 2:
    out = sys.argv[1] + ".gid"
elif argc == 3:
    out = sys.argv[2]
else:
    raise ValueError

bin = open(sys.argv[1], "rb")
bin.seek(0, 2)
size = bin.tell()
if size < cLen or size % cLen != 0:
    bin.close()
    raise ValueError

count = int(size / cLen)
bin.seek(0)

sid = open(out, "wb")

for i in range(count):
    item = struct.unpack("<i32si64siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii64s", bin.read(cLen))
    temp = struct.pack(
        "<20si40siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii50siii",
        item[1][0:19],
        item[2],
        item[3][0:39],
        item[4],
        item[5],
        item[10],
        item[11],
        item[12],
        item[13],
        item[14],
        item[16],
        item[17],
        item[18],
        item[19],
        item[20],
        item[21],
        item[22],
        item[23],
        item[24],
        item[25],
        item[26],
        item[27],
        item[28],
        item[29],
        item[30],
        item[31],
        item[32],
        item[33],
        item[6],
        item[34],
        item[35],
        item[36],
        item[37],
        item[15],
        item[38],
        item[39],
        item[40],
        item[41],
        item[42],
        item[43],
        item[44],
        item[45],
        item[46],
        item[47],
        item[48],
        item[49],
        item[50],
        item[51],
        item[52],
        item[53],
        item[54][0:49],
        item[7],
        item[8],
        item[9]
    )
    sid.write(temp)

bin.close()
sid.close()