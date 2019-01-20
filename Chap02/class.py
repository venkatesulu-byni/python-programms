#!/usr/bin/env python3


class Duck:
    s = 'Quaaack!'
    w = 'Walks like a duck.'
    def quack(self):
        print(self.s)

    def walk(self):
        print(self.w)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
