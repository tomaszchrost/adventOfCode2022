def compare_ints(left, right):
    if left < right:
        return True
    elif left > right:
        return False
    else:
        # conclusion has not been made yet
        return None


def compare_lists(left, right):
    for i in range(len(left)):
        if i == len(right):
            return False

        comparison = in_right_order(left[i], right[i])
        if comparison is not None:
            return comparison
    if len(left) < len(right):
        return True
    else:
        # conclusion has not been made yet
        return None


def in_right_order(left, right):
    if type(left) == int and type(right) == int:
        return compare_ints(left, right)
    elif type(left) == list and type(right) == list:
        return compare_lists(left, right)
    if type(left) == int:
        return in_right_order([left], right)
    else:
        return in_right_order(left, [right])


def sum_of_indices_in_order(signals):
    sum_of_indices = 0
    for i in range(len(signals)):
        if in_right_order(signals[i][0], signals[i][1]):
            sum_of_indices += i + 1
    return sum_of_indices


class Signal:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return in_right_order(self.value, other.value)


def get_decoder_key(signals):
    # signals is now object of Signal type
    divider_packs = (Signal([[2]]), Signal([[6]]))
    for divider_pack in divider_packs:
        signals.append(divider_pack)

    signals.sort()

    return (signals.index(divider_packs[0]) + 1) * (signals.index(divider_packs[1]) + 1)
