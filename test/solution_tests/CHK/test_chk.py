from solutions.CHK import checkout_solution


class TestSum():
    def test_chk(self):
        assert checkout_solution.checkout("AA") == 100

    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
    
    def test_chk(self):
        assert checkout_solution.checkout("AAA") == 130
    
    def test_chk(self):
        assert checkout_solution.checkout("AAABB") == 175
    
    def test_chk(self):
        assert checkout_solution.checkout("A") == 50
    
    def test_chk(self):
        assert checkout_solution.checkout("B") == 30
    
    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
    
    def test_chk(self):
        assert checkout_solution.checkout("AAAA") == 180
    
    def test_chk(self):
        assert checkout_solution.checkout("AAAAA") == 230

    def test_chk(self):
        assert checkout_solution.checkout("BBB") == 75

        