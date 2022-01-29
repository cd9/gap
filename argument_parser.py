class ArgumentParser():

    def parse(self, expected_args, argv):

        arguments = dict() 
        num_args = len(argv)
        if (num_args-1)%2!=0:
            logger.error("Incompatible number of arguments")
            return arguments

        for arg in expected_args:
            found = False
            for i in range(1, num_args, 2):
                cand = argv[i]
                if cand == "--"+arg:
                    arguments[arg] = float(argv[i+1])
                    found = True
                    break
            if not found:
                arguments[arg] = expected_args[arg]

        return arguments
