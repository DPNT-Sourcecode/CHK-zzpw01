from solutions.CHK import checkout_solution


class TestSum():
    def test_chk(self):
        assert checkout_solution.checkout("AA") == 100

    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
    
    def test_chk(self):
        assert checkout_solution.checkout("AAA") == 130

