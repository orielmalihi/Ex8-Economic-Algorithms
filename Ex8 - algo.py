from typing import List




class Uniform:
    def __init__(self, low:float, high:float):
        self.low = low
        self.high = high


def max_revenue_auction1(agent1: Uniform, value: float):
    """
    :param agent1:
    :param value:
    :return: whether or not he wins. if he does win the function will print hoe much
    the agent would need to pay.
    >>> agent1 = Uniform(10,30)
    >>> max_revenue_auction1(agent1, 15.1)
    Agent 1 wins and pays 15.0
    >>> max_revenue_auction1(agent1, 14.9)
    No agent wins
    >>> agent1 = Uniform(30,50)
    >>> max_revenue_auction1(agent1, 40)
    Agent 1 wins and pays 30
    """
    revenue = uniform_revenue(agent1, value)
    if revenue > 0:
        if agent1.high/2.0 < agent1.low:
            print("Agent 1 wins and pays "+str(agent1.low))
        else:
            print("Agent 1 wins and pays "+str(agent1.high/2.0))
    else:
        print("No agent wins")


def uniform_revenue(agent: Uniform, value: float) -> float:
    return 2*value - agent.high


def max_revenue_auction2(agent1: Uniform, value1: float, agent2: Uniform, value2: float):
    """
    :param agent1:
    :param value1:
    :param agent2:
    :param value2:
    :return: who is the winner (if there is any) and how much he has to pay.
    >>> agent1 = Uniform(10,30)
    >>> agent2 = Uniform(20,40)
    >>> max_revenue_auction2(agent1, 23, agent2, 27)
    Agent 1 wins and pays 22
    >>> max_revenue_auction2(agent1, 21, agent2, 27)
    Agent 2 wins and pays 26
    >>> agent1 = Uniform(20, 40)
    >>> agent2 = Uniform(25, 60)
    >>> max_revenue_auction2(agent1, 30, agent2, 35)
    Agent 1 wins and pays 25
    >>> max_revenue_auction2(agent1, 30, agent2, 42)
    Agent 2 wins and pays 40
    """
    revenue1 = uniform_revenue(agent1, value1)
    revenue2 = uniform_revenue(agent2, value2)
    max_revenue = max(revenue1, revenue2)
    if max_revenue < 0:
        print("No agent wins")
    elif max_revenue == revenue1:
        payment = 0
        while revenue1 > revenue2:
            value1 -= 1
            revenue1 = uniform_revenue(agent1, value1)
            if revenue1 <= revenue2:
                payment = value1
        print("Agent 1 wins and pays "+str(payment))
    elif max_revenue == revenue2:
        payment = 0
        while revenue2 > revenue1:
            value2 -= 1
            revenue2 = uniform_revenue(agent2, value2)
            if revenue2 <= revenue1:
                payment = value2
        print("Agent 2 wins and pays "+str(value2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
