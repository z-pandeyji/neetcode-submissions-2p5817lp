class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])

        # cars.sort(reverse=True)
        for i in range(n):
            max_idx = i
            for j in range(i+1, n):
                if cars[j][0] > cars[max_idx][0]:
                    max_idx = j
            temp = cars[i]
            cars[i] = cars[max_idx]
            cars[max_idx] = temp

        fleet = 0
        stack = []

        for i in range(n):
            pos = cars[i][0]
            spd = cars[i][1]

            time = (target - pos) / spd

            if len(stack) == 0 or time > stack[len(stack) - 1]:
                stack.append(time)
                fleet += 1
            else:
                continue
        return fleet



        