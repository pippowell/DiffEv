
def dating_fitness(trex: list) -> float:
    """
    This function maps a T-Rex candidate solution to their dating fitness value
    :param trex: A vector representing a candidate solution for a T-Rex
    :return: float, dating fitness value
    """
    [brain_size, teeth_size, height, weight, camouflage_level, claw_size, aggression] = trex

    value = (brain_size * 200 * 1-(100/(aggression+1))) + \
            (teeth_size + claw_size)/(teeth_size-claw_size) + \
            (height / weight) - \
            (75 - camouflage_level)
    return value
