#!/usr/bin/env python3

from caamse import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()