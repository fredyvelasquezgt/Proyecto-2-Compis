
class Terceto():

    def __init__(self, o=None, x=None, y=None, r=None, l=None):
        self.o = o
        self.x = x
        self.y = y
        # self.r = r
        self.l = l

    def keys(self):
        return ["l", "o", "x", "y"]
        return ["l", "r", "o", "x", "y"]

    def values(self):
        l = self.l if self.l != None else ""
        y = self.y if self.y != None else ""

        return [l, self.o, self.x, y]
        return [l, self.r, self.o, self.x, y]


class ThreeAddressCode():

    def __init__(self):
        self.tercetos = []

    def add(self, o=None, x=None, y=None, r=None, l=None):

        if type(o) not in [type(None), int, str]:
            o = str(o)

        if type(x) not in [type(None), int, str]:
            x = str(x)

        if type(y) not in [type(None), int, str]:
            y = str(y)

        if type(r) not in [type(None), int, str]:
            r = str(r)

        if type(l) not in [type(None), int, str]:
            l = str(l)

        if not r:
            # Compiler Three Address Code Reference
            r = "_r{i}".format(i=len(self.tercetos))

        # if not l:
        #     # Compiler Three Address Code Label
        #     l = "l_{i}".format(i=len(self.tercetos))

        terceto = Terceto(o, x, y, r, l)
        self.tercetos.append(terceto)

        return terceto, r

    def generate_code(self):
        with open("output/code.tac", "w") as f:
            for terceto in self.tercetos:
                l = terceto.l
                # r = terceto.r
                r = "_r{i}".format(i=self.tercetos.index(terceto))
                o = terceto.o
                x = terceto.x
                y = terceto.y

                instruction = "{l} := ".format(l=l) if l else "\t"

                if o == "<-" and not y:
                    # Save value in memory
                    f.write(instruction + "{r} <- {x}\n".format(l=l, r=r, x=x))
                elif o == "<-" and y:
                    f.write(instruction + "{r} <- {y} @ {x}\n".format(l=l, r=r, x=x, y=y))
                elif o == "call":
                    # Goto
                    f.write(instruction + "{r} <- goto {x} ({y})\n".format(l=l, r=r, x=x, y=y))
                elif o == "goto" and not y:
                    # Goto
                    f.write(instruction + "goto {x}\n".format(l=l, r=r, x=x))
                elif o == "goto" and y:
                    # Conditional goto
                    f.write(instruction + "goto {x} if {y}\n".format(l=l, r=r, x=x, y=y))
                elif not y:
                    # Unary operation
                    f.write(instruction + "{r} <- {o} {x}\n".format(
                        l=l,
                        r=r,
                        x=x,
                        o=o,
                    ))
                else:
                    f.write(instruction + "{r} <- {x} {o} {y}\n".format(
                        l=l,
                        r=r,
                        x=x,
                        o=o,
                        y=y,
                    ))
