from main import dh_annual_cost, gas_annual_cost  

def test_dh_annual_cost():
    result = dh_annual_cost(20000, 79.23, 74.82)
    assert round(result, 2) == 1575.63

def test_gas_annual_cost():
    result = gas_annual_cost(20000, 60.42, 58.63, 7000, 100, 0.05, 20)
    assert round(result, 2) == 1789.05
