def pilot_time(risk, stamina):
    try:
        if risk == 'high':
            time = stamina - 15
        elif risk == 'medium ':
            time = stamina - 20
        return time
    except TypeError as e:
        print(f'Insert value valid in stamina {e}')
    except ValueError as e:
        print(f'Insert valid value for risk high or medium : {e}')


def calculate_lap_factor(pilot_time, lap_time):
    try:
        lap_factor = lap_time / pilot_time
        return lap_factor
    except ZeroDivisionError as e:
        print(f'Time invalid !!\n{e}')


def piloted_laps(stamina, value_lap_factor):
    try:
        estimated_piloted_laps = stamina / value_lap_factor
        return estimated_piloted_laps
    except ZeroDivisionError as e:
        print(f'Value invalid !!\n {e}')


def pit_stop_estimation(number_of_turns_of_fuel_added):
    try:
        estimated_pit = 30 + (0.235 * number_of_turns_of_fuel_added)
        return estimated_pit
    except TypeError as e:
        print(f'Insert value valid of number of number_of_turns_of_fuel_added !! \n {e}')


def num_lap_estimate(race_time, lap_time):
    try:
        time_in_seconds = race_time * 60
        estimate_lap_time = lap_time + 2
        num_laps = time_in_seconds / estimate_lap_time
        return num_laps
    except ValueError as e:
        print(f'Input value valid !! \n {e}')
    except ZeroDivisionError as e:
        print(f'Input invalid !! \n {e}')
