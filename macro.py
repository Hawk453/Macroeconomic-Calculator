class macro:
    def __init__(self, counter):
        self.counter = counter
        
    
    def GDPatMP(self):
        if self.counter == 1:
            TotalNationalIncome = float(input("Enter Total National Income: "))
            SalesTax = float(input("Enter Sales Tax: "))
            Depreciation = float(input("Enter Depreciation: "))
            NetForeignFactorIncome = float(input("Enter Net Foreign Factor Income: "))
            return self.IncomeGDP(TotalNationalIncome, SalesTax, Depreciation, NetForeignFactorIncome)
            
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
        
        gdp_mp = TotalNationalIncome + SalesTax + Depreciation + NetForeignFactorIncome
        return gdp_mp

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
    
            
        