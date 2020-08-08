try:
    from app import App
except ImportError:
    from .app import App


if __name__ == '__main__':
    app = App()
    app.start()
    