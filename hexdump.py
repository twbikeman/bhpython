src = "Jane Austen was a country parson's daughter who lived most of her life in a tiny English village. She began writing her first novel, Sense and Sensibility, when she was still in her late teens. When she wrote the original version of her second and most famous novel, Pride and Prejudice (originally entitled First Impressions), she was not yet twenty-one. At that time she had never been away from home, except for a few years at a girls' boarding school before the age of ten. And yet, although she had seen almost nothing of the world beyond Steventon, the town where she grew up, she was able to write a witty, worldly novel of love, money, and marriage."

def hexdump(src, length = 16):
    result = []
    digits = 4
    for i in range(0, len(src), length):
        s = src[i : i + length]
        hexa = " ".join(["{:0{digits}X}".format(ord(x), digits = digits) for x in s])
        text = " ".join([x if  0x20 <= ord(x) < 0x7F else '.' for x in s])
        
        result.append("{:04X}   {:<{width}s} {}".format(i, hexa, text, width = length * (digits + 1)))
    print('\n'.join(result))       

if __name__ == "__main__":
    hexdump(src);