# District heating
dh_price_fixed = 79.23 # €/a
dh_price_var = 74.82 # €/MWh

# Gas boiler
gas_price_fixed = 60.42 # €/a
gas_price_var = 58.63 # €/MWh
gas_boiler_capex = 7000 # €
gas_boiler_service = 100 # €/a

# Heat demand & observation
heat_demand = 20000 # kWh/a
observation_period = 20 # a
interest_rate = 0.05 # 


# Calculation 

def dh_annual_cost(heat_demand, dh_price_fixed, dh_price_var):
    return dh_price_fixed + (heat_demand / 1000) * dh_price_var

def gas_annual_cost(heat_demand, gas_price_fixed, gas_price_var, gas_boiler_capex,
                    gas_boiler_service, interest_rate, observation_period):
    capex_annual = gas_boiler_capex * (interest_rate * (1 + interest_rate)**observation_period) / ((1 + interest_rate)**observation_period - 1)
    return gas_price_fixed + (heat_demand / 1000) * gas_price_var + gas_boiler_service + capex_annual
print("Annual cost (€/year):")
print(f"District heating: {dh_annual_cost(heat_demand, dh_price_fixed, dh_price_var):.2f}")
print(f"Gas Boiler:       {gas_annual_cost(heat_demand, gas_price_fixed, gas_price_var, gas_boiler_capex,
                    gas_boiler_service, interest_rate, observation_period):.2f}")

print("\nTotal costs over 20 years (€):")
print(f"District Heating: {dh_annual_cost(heat_demand, dh_price_fixed, dh_price_var) * observation_period:.2f}")
print(f"Gas Boiler:       {gas_annual_cost(heat_demand, gas_price_fixed, gas_price_var, gas_boiler_capex,
                    gas_boiler_service, interest_rate, observation_period) * observation_period:.2f}")

print("\nDistrict is the cheaper heating option for the considered example !")
def bad():print("fail")