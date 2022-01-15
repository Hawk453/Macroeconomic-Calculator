class macro:
    def __init__(self, counter):
        self.counter = counter
        
    
    def GDPatMP(self):
        if self.counter == 1:
            self.TotalNationalIncome = float(input("Enter Total National Income: "))
            self.SalesTax = float(input("Enter Sales Tax: "))
            self.Depreciation = float(input("Enter Depreciation: "))
            self.NetForeignFactorIncome = float(input("Enter Net Foreign Factor Income: "))
            return self.IncomeGDP(self.TotalNationalIncome, self.SalesTax, self.Depreciation, self.NetForeignFactorIncome)
            
        elif self.counter == 2:
            C = float(input("Enter Consumption: "))
            G = float(input("Enter Government Spending: "))
            I = float(input("Enter Investment: "))
            NX = float(input("Enter Net Exports: "))
            X = float(input("Enter exports otherwise '0': "))
            M = float(input("Enter imports otherwise '0': "))
            return self.ExpenditureGDP(C, G, I, NX, X, M)
            
        else:
            print("Input is wrong")
    
    def IncomeGDP(self, TotalNationalIncome, SalesTax, Depreciation, NetForeignFactorIncome):
        
        try:
            gdp_mp = TotalNationalIncome + SalesTax + Depreciation + NetForeignFactorIncome
            return gdp_mp
        except:
            print("Error at IncomeGDP")

    def ExpenditureGDP(self, C, G, I, NX = 0, X =0, M=0):
        if NX == 0:
            gdp_mp = C + G + I + X - M
            
        else:
            gdp_mp = C + G + I + NX
            
        return gdp_mp
    
    def GDPatFC(self, NetIndirectTax = 0, IndirectTax = 0, Subsidy = 0):
        if NetIndirectTax == 0:
            gdp_fc = self.GDPatMP() - (IndirectTax - Subsidy)
        else:
            gdp_fc = self.GDPatMP() - NetIndirectTax
        
        return gdp_fc
    
    def NDPatMP(self):
        if self.counter == 1:
            ndp_mp = self.GDPatMP() - self.Depreciation
            return ndp_mp
        elif  self.counter == 2:
            ndp_mp = self.GDPatMP()
            return ndp_mp
        else:
            print("Depreciation is required")
    
    def NDPatFC(self, NetIndirectTax = 0):

        try:
            ndp_fc = self.NDPatMP() - NetIndirectTax
            return ndp_fc
        except:
            print("Error at NDPatFC")
    
    def GNPatMP(self):

        try:
            gnp_mp = self.GDPatMP() + self.NetForeignFactorIncome
            return gnp_mp
        except:
            print("Error at GNPatMP")
    
    def GNPatFC(self, NetIndirectTax = 0):

        try:
            gnp_fc = self.GNPatMP() - NetIndirectTax
            return gnp_fc
        except:
            print("Error at GNPatFC")
    
    def NNPatMP(self):

        try:
            nnp_mp = self.GNPatMP() + self.Depreciation
            return nnp_mp
        except:
            print("Error at NNPatMP")

    def NNPatFC(self, NetIndirectTax):

        try:
            nnp_fc = self.NNPatMP() - NetIndirectTax
            return nnp_fc
        except:
            print("Error at NNPatFC")