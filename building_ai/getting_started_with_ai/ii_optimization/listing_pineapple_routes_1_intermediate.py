"""In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

Have a look at the program further down the page. Go ahead and run it. You'll see that the first thing it prints is PAN AMS AMS AMS AMS. Nice for the sailors but bad for pineapple lovers anywhere else but Amsterdam.

Each port is denoted by a number instead of a string: PAN is 0, AMS is 1 and so on. It is often easier to work with integer numbers instead of strings when programming. Keep this mapping in mind when we interpret the results of the program.

Fix the program by adding an if statement that checks that the route includes all of the ports. In other words, check that each of the numbers 0, 1, 2, 3, 4 are included in the list route.

Do not change the print statement given in the template (although you can add more print statements for debugging purposes)."""


def main():
    port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if set(route) == set(port_names):  # Another Option -> if len(set(route)) == len(port_names):
                        print(' '.join([port_names[i] for i in route]))


main()
