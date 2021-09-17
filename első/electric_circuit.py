villanyora = 25 * 230  #W
lamp_bulb = 5 * 30  #W
ac = 1500  #W
washing_machine = 1200  #W
iron = 2000  #W

already_used_power = lamp_bulb + ac + washing_machine

print("Lekapcsol-e a megszakító:", villanyora < already_used_power + iron)