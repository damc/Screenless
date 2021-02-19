class Output:
    def output(self, output):
        pass

    def __call__(self, output):
        self.output(output)
