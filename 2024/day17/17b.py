datafolder = "data"
with open(f"{datafolder}/17", "r") as file:
    data = file.read()[:-1].split("\n")


class Program:
    def __init__(self, reg, instr):
        self.reg = reg
        self.instr = instr
        self.where = 0
        self.jump = True

    def map_operand(self, ope):
        if ope in ["0", "1", "2", "3"]:
            return int(ope)
        elif ope == "4":
            return self.reg["A"]
        elif ope == "5":
            return self.reg["B"]
        elif ope == "6":
            return self.reg["C"]

    def do_op(self, opc, ope):
        if opc == "0":
            num = self.reg["A"]
            den = 2 ** self.map_operand(ope)
            self.reg["A"] = num // den

        elif opc == "1":
            self.reg["B"] = self.reg["B"] ^ int(ope)

        elif opc == "2":
            self.reg["B"] = self.map_operand(ope) % 8

        elif opc == "3":
            if self.reg["A"] != 0:
                self.where = int(ope)
                self.jump = False

        elif opc == "4":
            self.reg["B"] = self.reg["B"] ^ self.reg["C"]

        elif opc == "5":
            # print(output)
            return self.map_operand(ope) % 8

        elif opc == "6":
            num = self.reg["A"]
            den = 2 ** self.map_operand(ope)
            self.reg["B"] = num // den

        elif opc == "7":
            num = self.reg["A"]
            den = 2 ** self.map_operand(ope)
            self.reg["C"] = num // den

    def run(self):
        output = []
        while self.where < len(self.instr):
            i = self.where
            opc = self.instr[i]
            ope = self.instr[i + 1]
            out = self.do_op(opc, ope)
            if out is not None:
                output.append(out)
            if len(output) > 0 and output[-1] != int(self.instr[len(output) - 1]):
                return ",".join([str(i) for i in output])
            if self.jump:
                self.where += 2
            self.jump = True
        return ",".join([str(i) for i in output])


def get_register_program(data):
    reg = {}
    for line in data:
        if "Register A" in line:
            reg["A"] = int(line.split(":")[1].strip())
        elif "Register B" in line:
            reg["B"] = int(line.split(":")[1].strip())
        elif "Register C" in line:
            reg["C"] = int(line.split(":")[1].strip())
        elif "Program" in line:
            instr = line.split(":")[1].strip().split(",")

    return reg, instr


reg, instr = get_register_program(data)
Ai = 0
bsf = 0
while True:
    Ai += 1
    A = Ai * 8**9 + 0o723125622
    reg["A"] = A
    p = Program(reg, instr)
    output = p.run()
    instr_str = ",".join([i for i in instr])
    if instr_str == output:
        print(A)
        break
    elif len(output.split(",")) > bsf:
        print(A, oct(A), bsf, len(instr))
        bsf = len(output.split(","))
