"""
sss
"""

from sisagua.index import app

server = app.server

if __name__ == '__main__':
    app.run_server(
        # debug=True,
        # port=8051,
    )
