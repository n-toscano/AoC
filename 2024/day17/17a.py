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
            return None

        elif opc == "1":
            self.reg["B"] = self.reg["B"] ^ int(ope)
            return None

        elif opc == "2":
            self.reg["B"] = self.map_operand(ope) % 8
            return None

        elif opc == "3":
            if self.reg["A"] == 0:
                return None
            else:
                self.where = int(ope)
                self.jump = False
                return None

        elif opc == "4":
            self.reg["B"] = self.reg["B"] ^ self.reg["C"]
            return None

        elif opc == "5":
            return self.map_operand(ope) % 8

        elif opc == "6":
            num = self.reg["A"]
            den = 2 ** self.map_operand(ope)
            self.reg["B"] = num // den
            return None

        elif opc == "7":
            num = self.reg["A"]
            den = 2 ** self.map_operand(ope)
            self.reg["C"] = num // den
            return None

    def run(self):
        output = []
        while self.where < len(self.instr):
            i = self.where
            opc = self.instr[i]
            ope = self.instr[i + 1]
            out = self.do_op(opc, ope)
            if out is not None:
                output.append(out)
            if self.jump:
                self.where += 2
            self.jump = True
        return ",".join([str(i).strip(" ") for i in output])


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
p = Program(reg, instr)
print(p.run())
