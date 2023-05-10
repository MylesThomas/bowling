#!/usr/bin/python
# If you have several versions of Python installed, /usr/bin/env will ensure the interpreter used is the first one on your environment's $PATH. The alternative would be to hard code something like #!/usr/bin/python; that's ok, but less flexible.
class Program:
    def __init__(self, throw_results_list=None):
        if not throw_results_list:
            print(f"\nThrows result list not provided when Program was instantiated. Simulating a perfect game... \n")
            throw_results_list = [10] * 12
        self.throw_results_list = throw_results_list

    def print_game_results(self):
        game_score_int = self.play_game(
            throws=self.throw_results_list, 
            frame=1, 
            total=0
        )
        print(f"Results from the {len(self.throw_results_list)} balls thrown: {self.throw_results_list}")
        print(f"Final score: {game_score_int} \n")

    def play_game(self, throws, frame=1, total=0):
        """
        Recursive method that calculates the score of the bowling game one frame at a time and returns the total.

        Parameters
        ----------
        throws: list
            List of elements (throws) to be totaled.

        frame: int
             Index of the frame being calculated. Default value: 1

        total: int
            Running total of the bowling game score. Default value: 0

        Returns
        ----------
        score: int
            Final calculated total of the bowling game.
        """
        ### exit case (frame 10 calculated or incomplete game)
        if frame > 10 or not throws:
            return total

        ### strike
        elif throws[0] == 10:
            # bonus = next two throws following current frame
            bonus = 0
            # edge case logic for incomplete game
            if len(throws) >= 3:
                bonus = sum(throws[1:3])
            elif len(throws) > 1:
                bonus = throws[1]
            # pop off first index, increment frame count, update total
            return self.play_game(throws[1:], frame + 1, total + 10 + bonus)

        ### spare
        elif sum(throws[0:2]) == 10:
            # bonus = next throw following current frame
            bonus = 0
            # edge case logic for incomplete game
            if len(throws) >= 3:
                bonus = throws[2]
            # pop off first two indexes, increment frame count, update total
            return self.play_game(throws[2:], frame + 1, total + 10 + bonus)

        ### closed frame
        else:
            total += sum(throws[0:2])
            # pop off first two indexes, increment frame count, update total
            return self.play_game(throws[2:], frame + 1, total)
        


if __name__ == '__main__':
    game = Program()
    game.print_game_results()