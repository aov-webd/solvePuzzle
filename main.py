import itertools
import matplotlib.pyplot as plt
import numpy as np


class Figure:
    def __init__(self, coords, num_rot, num_flips):
        self.fig_initial = coords
        self.fig_rotated = coords
        self.fig_modified = np.zeros((10, 6), dtype=int)
        # self.fig_modified[0:coords.shape[0], 0:coords.shape[1]] = coords

        self.all_rotations = np.arange(0, num_rot, 1)
        self.all_flips = np.arange(0, num_flips, 1)

        self.flip = 0
        self.rotation = 0
        self.shift_x = 0
        self.shift_y = 0

        self.states = list()

    def get_state_nums(self, rot):
        self.fig_rotated = self.fig_initial
        for i in range(0, rot):
            self.fig_rotated = np.rot90(self.fig_rotated)

        size_x = self.fig_rotated.shape[1]
        size_y = self.fig_rotated.shape[0]
        shifts_x = np.arange(0, 7-size_x, 1)
        shifts_y = np.arange(0, 11-size_y, 1)

        self.states = itertools.product(shifts_x, shifts_y, self.all_flips)
        return np.arange(0, len(list(self.states)), 1)

    def set_state(self, state):
        self.shift_x = state[0]
        self.shift_y = state[1]
        self.flip = state[2]

        if self.flip:
            fig_modified_small = np.fliplr(self.fig_rotated)
        else:
            fig_modified_small = self.fig_rotated

        size_x = fig_modified_small.shape[1]
        size_y = fig_modified_small.shape[0]
        self.fig_modified = np.zeros((10, 6), dtype=int)
        self.fig_modified[self.shift_y:self.shift_y+size_y, self.shift_x:self.shift_x+size_x] = fig_modified_small


def solve():
    figures = list()
    figures.append(Figure(np.array(
        [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 1]]), 2, 2))
    figures.append(Figure(np.array(
        [[0, 1, 0, 0],
         [1, 1, 1, 1]]), 4, 2))
    figures.append(Figure(np.array(
        [[1, 1, 0, 0],
         [0, 1, 1, 1]]), 4, 2))
    figures.append(Figure(np.array(
        [[1, 0, 0],
         [1, 0, 0],
         [1, 1, 1]]), 4, 1))
    figures.append(Figure(np.array(
        [[1, 0, 0, 0],
         [1, 1, 1, 1]]), 4, 2))
    figures.append(Figure(np.array(
        [[0, 1, 0],
         [1, 1, 1],
         [0, 1, 0]]), 1, 1))
    figures.append(Figure(np.array(
        [[1, 1, 1, 1, 1]]), 2, 1))
    figures.append(Figure(np.array(
        [[0, 0, 1],
         [1, 1, 1],
         [0, 1, 0]]), 4, 2))
    figures.append(Figure(np.array(
        [[1, 0, 0],
         [1, 1, 0],
         [0, 1, 1]]), 4, 1))
    figures.append(Figure(np.array(
        [[0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]]), 4, 1))
    figures.append(Figure(np.array(
        [[1, 0, 1],
         [1, 1, 1]]), 4, 1))
    figures.append(Figure(np.array(
        [[1, 1, 0],
         [1, 1, 1]]), 4, 1))

    rotations = list()
    for x in figures:
        rotations.append(x.all_rotations)
    p_rotations = itertools.product(*rotations)

    states = list()

    for rot in p_rotations:
        for i_fig in range(0, len(figures)):
            states.append(figures[i_fig].get_state_nums(rot[i_fig]))

        p_states = itertools.product(*states)
        for state in p_states:
            print("s")

    for cur_figure in figures:
        for rot in cur_figure.all_rotations:
            curs_states = list(cur_figure.get_states(rot))
            for state in curs_states:
                state_with_rot = list(state)
                state_with_rot.append(rot)
                cur_figure.set_state(state_with_rot)

                fig_sum = np.zeros((10, 6), dtype=int)

                for x in figures:
                    fig_sum = fig_sum + x.fig_modified
                plt.imshow(fig_sum)
                plt.show()

    # iter_failed = 1
    # iteration = 0
    # while iter_failed == 1:
    #     iter_failed = 0
    #
    #
    #         if np.amax(fig_sum) > 1:
    #             iter_failed = 1
    #             break
    #
    #     iteration += 1
    #
    # power = 500
    # for x in figures:
    #     fig_sum = fig_sum + x.fig_modified*power
    #     power += 80

    plt.imshow(fig_sum)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    solve()
