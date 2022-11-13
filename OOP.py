class Coffee:
    def __init__(self, turi, tami, narxi):
        self.turi=turi
        self.tami=tami
        self.narxi=narxi


c1 = Coffee("SUTLI COFFEE;, ", "tami: zo'r,", "narxi: 2")
c2 = Coffee("QORA COFFEE; ", "tami: yaxshi,", "narxi: 2")


print(c1.turi, c1.tami, c1.narxi)
print(c2.turi, c2.tami, c2.narxi)