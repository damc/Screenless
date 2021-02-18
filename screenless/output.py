class Output:
    def run(self):
        pass

    def output(self, output):
        pass

    def exit(self):
        pass

    def __call__(self, output):
        self.output(output)
