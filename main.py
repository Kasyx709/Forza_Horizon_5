from vehicle import Vehicle


def build_vehicle(v_name, v_wt, f_h, r_ht, f_wt_pct, t_type):
    return Vehicle(v_name, v_wt, f_h, r_ht, f_wt_pct, t_type)


if __name__ == '__main__':
    vehicle_name = "morris_fe"
    vehicle_weight = 2751
    front_height = 2.4
    rear_height = 3.1
    front_wt_pct = 54
    terrain_type = "road"
    vehicle = build_vehicle(vehicle_name, vehicle_weight, front_height, rear_height, front_wt_pct, terrain_type)
    vehicle.vehicle_attributes()
