if __name__ == "__main__":
    """Only perform actions when invoked directly!"""
    from Simulator import Simulator
    from Controller import Controller
    import inspect
    from functools import wraps

    def log(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                print("Entering: [%s] with parameters %s" % (func.__name__, args))
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Exception in %s : %s" % (func.__name__, e))
            finally:
                print("Exiting: [%s]" % func.__name__)
        return wrapped

    def trace(cls):
        for name, m in inspect.getmembers(cls, inspect.isfunction):
            setattr(cls, name, log(m))
        return cls

    Simulator = trace(Simulator)
    Controller = trace(Controller)
    simulator = Simulator(True) # use Simulator(False) to disable the GUI

    lijstje = dir(Controller)
    for l in lijstje:
        x = eval("Controller." + l)
        print("Controller."+str(x))
        print(inspect.getdoc(x), "\n")

    #print(simulator)
    simulator.run()
    # print('Dir of simulator: ', dir(simulator), '\n')
    # print("Dir of simulator controller: ", dir(simulator._Simulator__controller), '\n')
    # print("Vars of simulator controller: ", vars(simulator._Simulator__controller), "\n")
    # print("Dir of simulator controller sensor: ", dir(simulator._Simulator__controller._Controller__sensors), "\n")
    # print("Dir of simulator controller effector: ", dir(simulator._Simulator__controller._Controller__effectors), "\n")
