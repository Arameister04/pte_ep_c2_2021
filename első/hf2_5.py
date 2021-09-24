tibor_room = 75 #m^2
one_bucket_of_paint = 15 #m^2
one_bucket_of_paint_cost = 4300 #Ft


tibor_room_painted_two_times = tibor_room * 2
paint_needed = tibor_room_painted_two_times / one_bucket_of_paint #db
paint_costs = paint_needed * one_bucket_of_paint_cost

painter = 13 #min/1m^2
painter_finish = painter * tibor_room_painted_two_times #min
painter_cost_per_hour = 2100 #Ft
painter_full_cost = (painter_finish / 60) * painter_cost_per_hour

all_costs_plus_afa = (paint_costs + painter_full_cost) * 1.27 #Ft

print("A festő", painter_full_cost, "forintért festi ki Tibor szobáját.")
print("A végösszeg az ÁFA hozzáadásával ennyi lesz:", all_costs_plus_afa ,"Ft.")


